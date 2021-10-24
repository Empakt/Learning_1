int userDelay = 1000, stepsCount = 10;
char answer;

void setup(){
  Serial.begin(9600);
  pinMode(11, OUTPUT);
  //Launch(userDelay, stepsCount);
}

void loop(){
  //char answer;
  Serial.println("===================");
  Serial.println("a: Countdown and launch");
  Serial.println("b: Reset ignition");
  Serial.println("c: Set countdown number");
  Serial.println("d: Set delay between countdown steps");
  Serial.println("===================");
  EmptySerial();
  while (!Serial.available()){
    //Serial.println("Waiting for input");
  }
  /*while (Serial.available()){
    answer = Serial.read();
    Serial.println(answer);
    delay(500);
  }*/

  answer = Serial.read();
  //Serial.println("Entered option: " + answer);

    switch (answer){
      case 'a':
      Launch();
      break;

      case 'b': Serial.println("Resetting ignition...");
      analogWrite(11, 0);
      break;

      case 'c':
      CountdownChange();
      break;
      
      case 'd':
      DelayChange();
      break;

      default: break;
    }
  //EmptySerial();
}

void EmptySerial(){
  while (Serial.available()){
    answer = Serial.read();
  }
}

void Launch(){
  Serial.println("Initializing countdown, everyone get to the blast shield bunker immediately !");
  Serial.print("Steps: ");
  Serial.print(stepsCount);
  Serial.print(", Delay: ");
  Serial.println(userDelay);
  int x;
  for(x = stepsCount; x>=1; x --){
    Serial.println(x);
    delay(userDelay);
  }
  Serial.println("Launching !");
  analogWrite(11, 20);
}

void CountdownChange(){
  //Serial.println("Enter the new countdown number: ");
  EmptySerial();
  while (!Serial.available()){
    //Serial.println("Waiting for input");
    //Serial.println(Serial.read());
  }
  stepsCount = Serial.parseInt();
  Serial.print("New countdown number: ");
  Serial.println(stepsCount);
}

void DelayChange(){
  //Serial.print("Enter the countdown delay: ");
  EmptySerial();
  while (!Serial.available()){
  }
  userDelay = Serial.parseInt();
  Serial.print("New countdown delay: ");
  Serial.println(userDelay);
}

/*int readInt(void) //will read a positive integer in the range from 0 to 32767
{
  String inString = "";    // string to hold input
  int inChar = ' ';
  int value;
  do
  {
    if (Serial.available() > 0)
    {
      inChar = Serial.read();
      if (isDigit(inChar))
      {
        // convert the incoming byte to a char and add it to the string:
        inString += (char)inChar;
      }
    }
    else  // no inchar is read
      {
        inChar = 0;  //not a number not a nl
      }
  }
  while (inChar != '\n');
  value = inString.toInt();
  return value;
}*/
