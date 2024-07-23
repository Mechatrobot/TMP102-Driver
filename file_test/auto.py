from git import Repo # Open my repository
import pandas as pd
import os
from datetime import datetime
import pytz
from styleframe import StyleFrame
from openpyxl import load_workbook
from openpyxl.styles import Alignment

url_repo = "https://github.com/Mechatrobot/TMP102-Driver"
local_file = "C:/Users/se93297/Desktop/TMP102-Driver-main"

if not os.path.exists(local_file) :
  Repo.clone_from(url_repo,local_file);       #clone the repo into the local if it doesn't exist.
else :
  #repo = Repo(local_file)
  origin = Repo(local_file).remotes.origin #remote the repo to local directory
  origin.pull()   # pull the changes into the local repository
commits =  list(Repo(local_file).iter_commits('main'))
#print(commits)
commit_data = []
for commit in commits :
   timezonedate = pytz.timezone("Africa/Casablanca")
   commit_date = commit.committed_datetime.astimezone(timezonedate)#convert the timezone to UTC.
   commit_data.append({
                       'Filename' : Repo(local_file).git.show(commit, name_only=True, format="%n"),
                       'Commiter' : commit.author.name,
                       'Email': commit.author.email,
                       'SHA' : commit.hexsha,
                       'Date of committement' : commit_date.strftime('%Y-%m-%d %H:%M:%S'), #string format
                       'Message' : commit.message.strip()
                      })
   #print(commit.hexsha)
data_frame = pd.DataFrame(commit_data) #convert commit data to DataFrame to put it on excel
excel_file = os.path.join('C:/Users/se93297/Desktop/TMP102-Driver-main/file_test','commits_list.xlsx')  # create the excel file
data_frame.to_excel(excel_file, index=False, sheet_name= 'Commits') #assign DataFrame to excel
files = []
files.append({'File': 'num.py','SHA':  '','Revision du scenario' : '1.0'})
files.append({'File': 'auto.py','SHA':'','Revision du scenario' : '2.6'})
files.append({'File': 'test.c','SHA':'','Revision du scenario' : '4.1'})
data_frame2 = pd.DataFrame(files)
#data_frame2['Revision du scenario'] = data_frame2['Revision du scenario'].astype(float)
#print(data_frame2)
filename_extract = data_frame2['File'].tolist()
filename_commithistory = data_frame['Filename'].tolist()
SHA_extract = data_frame2['SHA'].tolist()
SHA_commithistory = data_frame['SHA'].tolist()
#print(filename_extract)
#print(filename_commithistory)
#for filename in filename_commithistory :
#    if filename in filename_extract :
#        print('good')
#print(data_frame2[data_frame2.columns[0]])
for i in range(len(filename_extract)) :
  for j in range(len(filename_commithistory)) :
    if filename_extract[i] in filename_commithistory[j] :
       #SHA_var = SHA_extract[i]
       SHA_extract[i] = SHA_commithistory[j] + ';' + SHA_extract[i]
       data_frame2['SHA'] = SHA_extract
       data_frame2['SHA'] = data_frame2['SHA'].str.replace(";","\n")
       #display(HTML(data_frame2.to_html().replace(";","<br>")))
       #if filename_extarct[i] in data_frame2['File'].values :
       #data_frame2.loc[data_frame2['File'] == filename_extract[i], 'Revision du scenario'] += 0.1

#data_frame2.update(data_frame)
print(data_frame2)
display(data_frame2)
excel_updated_file = os.path.join('C:/Users/se93297/Desktop/TMP102-Driver-main/file_test','Updated_commits.xlsx')
#data_frame2.to_excel(excel_updated_file, index=False, sheet_name= 'Commits')  # create the excel file
StyleFrame(data_frame2).to_excel(excel_updated_file,sheet_name = 'TEST').close()
wb = load_workbook(excel_updated_file)
ws = wb['TEST']
ws.column_dimensions['B'].width = 64
#format = wb.add_format()
#format.set_align('left')
#ws.set_column('B', 10, format)
#for letter in ['A','B'] :
#  max_width = 0
#  for index in range(1,ws.max_row + 1) :
#    if len(ws[f'{letter}{index}'].value) > max_width  :
#         max_width = len(ws[f'{letter}{index}'].value)
#         print(max_width)
#  ws.column_dimensions[letter].width = max_width
#for row in range(1,ws.max_row+1):
#    for col in range(1,ws.max_column+1):
#        cell=ws.cell(row, col)
#        cell.alignment = Alignment(horizontal='left')
wb.save(excel_updated_file)
data_frame2['Revision du scenario'] = data_frame2['Revision du scenario'].astype(float)
data_frame2['Revision du scenario'] += 0.1
print(data_frame2['Revision du scenario'])
#print(SHA_commithistory)
