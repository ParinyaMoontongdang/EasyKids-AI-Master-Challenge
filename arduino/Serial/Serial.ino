#include <EasyKids3in1.h>

void setup() {
  EasyKids_Setup();
  beginSerialRX();
  
  ledSetBrightness(50);
  ledCarSetBrightness(50);

  welcomeSong();
  beep();
}

void loop() {
  String data = readDataString();
  Serial.println(data);

  if(data == "on"){
    ledFillColor(MAGENTA);
    ledCarFillColor(MAGENTA);
  }
  else if(data == "off"){
    ledFillColor(BLACK);
    ledCarFillColor(BLACK);
  }
}