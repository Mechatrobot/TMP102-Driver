from git import Repo # Open my repository
import pandas as pd
import os
from datetime import datetime
import pytz

url_repo = "https://github.com/Mechatrobot/TMP102-Driver"
local_file = "./TMP102-Driver-main"

if not os.path.exists(local_file) :
  Repo.clone_from(url_repo,local_file);       #clone the repo into the local if it doesn't exist.
else :
  #repo = Repo(local_file)
  origin = Repo(local_file).remotes.origin #remote the repo to local directory
  origin.pull()   # pull the changes into the local repository
commits =  list(Repo(local_file).iter_commits('main'))
commit_data = []
for commit in commits :
   timezonedate = pytz.timezone("Africa/Casablanca")
   commit_date = commit.committed_datetime.astimezone(timezonedate)#convert the timezone to UTC.
   commit_data.append({
                       'Commiter' : commit.author.name,
                       'Email': commit.author.email,
                       'SHA' : commit.hexsha,
                       'Date of committement' : commit_date.strftime('%Y-%m-%d %H:%M:%S'), #string format
                       'Message' : commit.message.strip()
                      })

data_frame = pd.DataFrame(commit_data) #convert commit data to DataFrame to put it on excel
excel_file = os.path.join(local_file,'commits_list.xlsx')  # create the excel file
data_frame.to_excel(excel_file, index=False, sheet_name= 'Commits') #assign DataFrame to excel
