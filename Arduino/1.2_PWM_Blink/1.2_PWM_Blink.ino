void setup() {
  pinMode(11, OUTPUT);
}

void loop() {
  analogWrite(11, 5);
  delay(1000);  
  analogWrite(11, 20);
  delay(1000);
  analogWrite(11, 50);
  delay(1000);
  analogWrite(11, 100);
  delay(1000);
  analogWrite(11, 255);
  delay(1000);
  analogWrite(11, 0);
  delay(1000);
}
