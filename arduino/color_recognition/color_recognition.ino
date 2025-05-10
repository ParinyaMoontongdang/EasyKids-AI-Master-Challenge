#include <EasyKids3in1.h>

String msg;

void setup() {
  EasyKids_Setup();
  Serial.begin(115200);                       // สำหรับ debug
  Serial2.begin(115200, SERIAL_8N1, 26, 33);  // RX=21, TX=22

  Serial.println("UART2 Ready on RX=26, TX=33");
  ledSetBrightness(50);
  ledCarSetBrightness(50);
}

void loop() {
  if (Serial2.available()) {
    msg = Serial2.readStringUntil('\n');
    Serial.print("From K210: ");
    Serial.println(msg);
  }

  if(msg == "p"){
    ledFillColor(MAGENTA);
    ledCarFillColor(MAGENTA);
  }
  else if(msg == "b"){
    ledFillColor(YELLOW);
    ledCarFillColor(YELLOW);
  }
 delay(100);
}