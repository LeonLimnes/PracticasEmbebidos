/*
# ## ###############################################
#
# program: ac_control.cpp.ino
# Controls power given to an AC load
# with valures recived from I2C bus.
#
# Autor: César Martínez
#        Lisset Noriega Domínguez
# License: MIT
#
# ## ###############################################

*/

#include <Wire.h>

// Constants
#define I2C_SLAVE_ADDR 0x0A
// Digital 2 is Pin 2 in UNO
#define ZXPIN 2
// Digital 3 is Pin 3 in UNO
#define TRIAC 3
//Led o the board
#define BOARD_LED 13

// Globals
volatile bool flag = false;
float power = 0;
float triggerTime = 10.00;
float *convertionTable;
int intPower = 0;

// Prototypes
void i2c_received_handler(int count);
void i2c_request_handler(int count);
void convertPower();
void populateTable(float *convertionTable);
void zxhandle();

/**
* Setup the Arduino
*/
void setup(void){
  // Configure I2C to run in slave mode with the defined address
  Wire.begin(I2C_SLAVE_ADDR);
   // Configure the handler for received I2C data
  Wire.onReceive(i2c_received_handler);
  // Configure the handler for request of data via I2C
  Wire.onRequest(i2c_request_handler);

  // Setup the serial port to operate at 56.6kbps
  Serial.begin(57600);
  
  // Setup interupt pin (input)
  pinMode(ZXPIN, INPUT);
  attachInterrupt(0, zxhandle, RISING);
  // Setup output (triac) pin
  pinMode(TRIAC, OUTPUT);
  // Blink led on interrupt
  pinMode(BOARD_LED, OUTPUT);

  //Table that stores the corresponding trigger times for a given power factor
  convertionTable = (float*)calloc(100,sizeof(float));
  populateTable(convertionTable);
}

/**
* Handles data requests received via the I2C bus
* It will immediately reply with the power stored
*/
void i2c_request_handler(){
  Wire.write((byte*) &power, sizeof(float));
}

/**
* Handles received data via the I2C bus.
* Data is stored in local variable power.
*/
void i2c_received_handler(int count){
  float f;
  byte *fp;
  if(count != 4) return;
  fp = (byte*)&f;
  for(byte i = 0; i < count; ++i)
  fp[i] = (byte)Wire.read();
  power = f;
  convertPower();
}

void showPower(){

  char buffn[10];
  char buffer[20];
  dtostrf(intPower,10,1,buffn);
  sprintf(buffer, "Power = %s\n", buffn);
  Serial.write(buffer);

}

//Add the numerical values to the convertionTable
//in this case, adds values 5 by 5
void populateTable(float *convertionTable){
  convertionTable[0] = 10.00;
  convertionTable[5] = 7.668;
  convertionTable[10] = 7.334;
  convertionTable[15] = 7.030;
  convertionTable[20] = 6.750;
  convertionTable[25] = 6.487;
  convertionTable[30] = 6.232;
  convertionTable[35] = 5.984;
  convertionTable[40] = 5.738;
  convertionTable[45] = 5.493;
  convertionTable[50] = 5.245;
  convertionTable[55] = 4.993;
  convertionTable[60] = 4.734;
  convertionTable[65] = 4.464;
  convertionTable[70] = 4.179;
  convertionTable[75] = 3.874;
  convertionTable[80] = 3.538;
  convertionTable[85] = 3.157;
  convertionTable[90] = 2.696;
  convertionTable[95] = 2.060;
  convertionTable[100] = 1.000;   
}

//Convert the flaoting point value of power
// into an int value rounding it to the closest
// multiple of 5
int intPot(float r){
    int n = (int)r;
    int d = 5;
    int mod = n % d;
    if(mod == 0)
        return n;
    if(mod == 1 or mod == 2)
        return n-mod;
    else
        return n+(d-mod);
}

// Funciton that converts the flaot power to int and
// the gets its trigger time from the table
void convertPower(){
  intPower = intPot(power);
  triggerTime = convertionTable[intPower];

}

void loop(){
  //Dipslay the value of the current power factor used.
  showPower();
 
}

//Interruption handler whe rising edge occurs

void zxhandle(){
 
  if(intPower != 0){
    //trigger time
    delayMicroseconds(triggerTime*1000);
    digitalWrite(TRIAC, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIAC, LOW);;
  }
}
