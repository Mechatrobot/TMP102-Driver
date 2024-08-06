#include <main.h>
#include <stdio.h>
#include <string.h>
//é"uhdu
typedef enum {TMP102_OK = 0 , TMP102_ERROR = -1}TMP102_STATE;

typedef enum {

        TMP102_ADD_V1 = 0x48 << 1,
        TMP102_ADD_V2 = 0x49 << 1,
        TEMP_POINTER = 0x0,
        TMP102_CONF = 0x01

}TMP102_REG;

typedef struct {

	TMP102_REG add ;

}TMP102_conf;



void tmp102_check_device(TMP102_conf* dev);
uint8_t read_data(TMP102_conf* dev,TMP102_conf* read);
void tmp102_config(TMP102_conf* dev,TMP102_conf* conf,uint8_t BYTE1,uint8_t BYTE2);
