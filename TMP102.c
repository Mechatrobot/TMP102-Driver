yyuuuuu//DriverTEMPer//fezfrf

#include <main.h>
#include <stdio.h>
#include <string.h>
#include <driver_header_file.h>

extern I2C_HandleTypeDef hi2c1;
uint8_t conf ;


void tmp102_check_device(TMP102_conf* dev)
{

	HAL_StatusTypeDef conf = HAL_I2C_IsDeviceReady(&hi2c1, dev -> add ,1,HAL_MAX_DELAY);

	if(conf == HAL_OK)
	{
	printf("Working\r\n");
	}
	else
	{
    printf("Not working\r\n");
	}
}
void tmp102_config(TMP102_conf* dev,TMP102_conf* conf,uint8_t BYTE1,uint8_t BYTE2)
{
	uint8_t FRQ[2];

	FRQ[0] = BYTE1;

	FRQ[1] = BYTE2;

	HAL_I2C_Mem_Write(&hi2c1,dev -> add = TMP102_ADD_V1,conf -> add,I2C_MEMADD_SIZE_8BIT, FRQ,2,HAL_MAX_DELAY);


}
uint8_t read_data(TMP102_conf* dev,TMP102_conf* read)
{
    uint8_t temp_data[2];

    float temp;

    HAL_I2C_Mem_Read(&hi2c1,dev -> add = TMP102_ADD_V1,read -> add,I2C_MEMADD_SIZE_8BIT, temp_data,2, HAL_MAX_DELAY);

	uint16_t raw = (temp_data[0] << 4) | (temp_data[1] >>4) ;

	temp = raw*0.0625;

	printf("T = %.2f C \r\n",temp);
    return temp ;
}


