void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
}

void loop() {
  Serial.println("===================");
  Serial.println("a: morse S");
  Serial.println("b: morse O");
  Serial.println("c: morse SOS");
  Serial.println("===================");
  while (!Serial.available()){
    char answer = Serial.read();

    switch (answer){
      case 'a': Serial.println("Morse S chosen");
      break;

      case 'b': Serial.println("Morse O chosen");
      break;
      
      case 'c': Serial.println("Morse SOS chosen");
      break;

      default: break;
    }
  }
}
