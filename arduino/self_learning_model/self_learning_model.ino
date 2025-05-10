#include <EasyKids3in1.h>

String msg;

void setup() {
  EasyKids_Setup();
  Serial.begin(115200);                       // สำหรับ debug
  Serial2.begin(115200, SERIAL_8N1, 26, 33);  // RX=26, TX=33

  Serial.println("UART2 Ready on RX=26, TX=33");
  ledSetBrightness(50);
  ledCarSetBrightness(50);

  sensorNum(6);  // For 7 Sensors
  // remapSensor(1,2,3,4,5,6,0);
  blackLine();  // Black Line
  setSensorMin(580, 510, 510, 480, 1770, 3000);
  setSensorMax(4095, 4095, 4095, 4095, 4040, 4070);
  welcomeSong();
}

void loop() {
  // readSensor();

  waitForStart();
  beep();

  // lineFollowTime(20, 1.0, 1.6, 20000);
  lineFollowCross(20, 1.0, 1.6);

  ledFillColor(WHITE);
  ledCarFillColor(WHITE);
  delay(5000);
  msg = "none";

  while (1) {
    if (Serial2.available()) {
      msg = Serial2.readStringUntil('\n');
      Serial.print("From K210: ");
      Serial.println(msg);

      if (msg == "red") {
        ledFillColor(RED);
        ledCarFillColor(RED);
        delay(600);
        motorStopAll();
        break;
      } else if (msg == "green") {
        ledFillColor(GREEN);
        ledCarFillColor(GREEN);
        forward(50);
        delay(300);
        break;
      } else if (msg == "yellow") {
        ledFillColor(YELLOW);
        ledCarFillColor(YELLOW);
        turnRight(50);
        delay(300);
        break;
      } else {
        ledFillColor(WHITE);
        ledCarFillColor(WHITE);
        motorStopAll();
      }
    }
  }
  motorStopAll();
  //  delay(100);
}