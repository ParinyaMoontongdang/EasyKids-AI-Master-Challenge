#include <EasyKids3in1.h>

int i;

void setup() {
  EasyKids_Setup();
  display3in1();
  welcomeSong();
  
  waitForStart(); 
  beep(); 
}

void loop(){
  for (i = 0; i <= 180; i++)
  {
    servo(6, i);
    Serial.println(i);
    delay(20);
  }
  for (i = 180; i >= 0; i--)
  {
    servo(6, i);
    Serial.println(i);
    delay(20);
  }
}
