void setup() {
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(3, OUTPUT);
}

void loop() {
  // red light
  analogWrite(10, 0);
  analogWrite(11, 10);
  analogWrite(5, 0);
  analogWrite(3, 30);
  delay(4000);
  // yellow light before green
  analogWrite(11, 0);
  analogWrite(10, 10);
  analogWrite(3, 0);
  analogWrite(5, 10);
  delay(2000);
  // green light
  analogWrite(10, 0);
  analogWrite(9, 30);
  analogWrite(5, 0);
  analogWrite(6, 10);
  delay(4000);
  // yellow light before red
  analogWrite(9, 0);
  analogWrite(10, 10);
  analogWrite(6, 0);
  analogWrite(5, 10);
  delay(2000);
}
