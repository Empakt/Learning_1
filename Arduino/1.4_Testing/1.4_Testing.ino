char x;
String info;
int y;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  x = 'a';
  info = "poggers";
  y = 69;
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(x);
  Serial.println(info);
  Serial.println(y);
  delay(1000);
}
