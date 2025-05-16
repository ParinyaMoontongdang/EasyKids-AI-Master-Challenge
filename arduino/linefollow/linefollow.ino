#include <EasyKids3in1.h>

void setup() {
  EasyKids_Setup();

  sensorNum(6); // For 7 Sensors
  blackLine(); // Black Line

  setSensorMin(975, 900, 385, 1229, 912, 723, 688);  // Black Line Value >>> A0 A1 A2 A3 A4 A5 A6
  setSensorMax(4023, 3875, 2380, 4065, 4023, 3460, 3226);  // White Line Value >>> A0 A1 A2 A3 A4 A5 A6

  beginSerialRX();

  
}

void loop() {

  // Serial.print(readDataString());

  // readSensor();  //Show Value 7 Sensor via LCD Display

  waitForStart(); 
  beep(); 

  DashedLineTime(20, 1.3, 1.5, 20000);
  // lineTime(20, 1.3, 1.5, 20000); //lineFollowTime (Speed, KP, KD, Time(ms));
  DashedLineCross(20, 1.3, 1.5); //lineFollowCross(Speed, KP, KD);
  // lineFollowTimer(35, 1.0, 1.0, 5000); //lineFollowTime (Speed, KP, KD, Time(ms));
  // lineFollowTurnLeft(30);// lineTurnLeft(Speed);
 
}
