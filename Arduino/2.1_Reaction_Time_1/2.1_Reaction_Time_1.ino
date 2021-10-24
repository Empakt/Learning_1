int button;
bool timeWritten = false;

void setup() {
  Serial.begin(9600);
  pinMode(7, INPUT_PULLUP);
  pinMode(11, OUTPUT);
}

void loop() {
  button = digitalRead(7);
  //Serial.println(button);
  if (button == HIGH){
    digitalWrite(11, HIGH);
    timeWritten = false;
  }
  else{
    digitalWrite(11, LOW);
    if (!timeWritten){
      Serial.print("Time of press since startup: ");
      float timeSinceStart = millis();
      Serial.println(timeSinceStart/1000);
      timeWritten = true;
    }
  }
  //delay(100);
}
