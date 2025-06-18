#include <EasyKids3in1.h>
void setup() {
  EasyKids_Setup();
  display.setRotation(0);
  displayClear();

  display.setTextSize(3);
  display.setCursor(80, 70);
  display.setTextColor(TFT_PINK);
  display.setFreeFont(Sarabun14TH);
  display.println(String("พบ"));

  display.setTextSize(4);
  display.setCursor(0, 180);
  display.setTextColor(TFT_PINK);
  display.setFreeFont(Sarabun14TH);
  display.println(String("ช่างยนต์"));
}

void loop() {

}