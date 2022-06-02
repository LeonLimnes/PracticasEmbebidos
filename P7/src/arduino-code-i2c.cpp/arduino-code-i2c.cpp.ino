#include <Wire.h>

// Constants
#define I2C_SLAVE_ADDR 0x0A
#define BOARD_LED 13

// Global variables
float power = 0;

// Prototypes
void i2c_received_handler(int count);
void i2c_request_handler(int count);

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

  // Setup board led
  pinMode(BOARD_LED, OUTPUT);
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
}

void loop(){
  char buffn[10];
  dtostrf(power,10,2,buffn);
  char buffer[20];
  sprintf(buffer, "Power = %s\n", buffn);
  Serial.write(buffer);
  delay(1000);
}
