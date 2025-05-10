#include <EasyKids3in1.h>
// #include <HardwareSerial.h>

// HardwareSerial Serial2(2);  // ใช้ UART2 (ESP32 มี 3 UART)

void setup() {
  EasyKids_Setup();
  Serial.begin(115200);                       // สำหรับ debug
  Serial2.begin(115200, SERIAL_8N1, 26, 33);  // RX=26, TX=33

  Serial.println("UART2 Ready on RX=26, TX=33");
}

void loop() {
  // Serial2.println("Hello K210");

  if (Serial2.available()) {
    String msg = Serial2.readStringUntil('\n');
    Serial.print("Raw data: ");  // เช็คค่าที่อ่านได้
    Serial.println(msg);

    // ****** for read number ******
    // float number = msg.toFloat();
    // Serial.print("Converted float: ");
    // Serial.println(number, 2);
  }

  // if (sw_Start()==0) {
  //   motor(4, -50);
  // } else {
  //   motorStopAll();
  // }

 delay(100);
}