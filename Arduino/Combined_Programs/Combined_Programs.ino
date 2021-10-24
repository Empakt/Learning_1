// Defining the needed variables for the state of buttons and LEDs
bool b1Again = true;
bool b2Again = true;
bool led1On = false;
bool led2On = false;

// Variable for getting the input from serial monitor
char answer;

long toggleTime1 = 0;
long toggleTime2 = 0;
long debounce = 10;

void setup() {
  // Setting the modes for the buttons and LEDs
  pinMode(13, INPUT_PULLUP);
  pinMode(12, INPUT_PULLUP);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);

  // Turing the LED 1 on at the start of the program
  analogWrite(11, 5);
  led1On = true;

  Serial.begin(9600);

  // Printing even numbers in the 2 to 22 range
  for (int i = 2; i <= 22; i += 2){
    Serial.println(i);
  }
}

void loop() {
  // Printing the menu on each rerun of the loop function
  Serial.println("===================");
  Serial.println("a: Print numbers from 0 to 17 on the Serial Monitor");
  Serial.println("b: Toggle LED 1");
  Serial.println("c: Toggle LED 2");
  Serial.println("===================");

  // Emptying serial monitor of any data to answer to save memory
  while (Serial.available()){
    answer = Serial.read();
  }

  // While there is nothing on the Serial input and the program is waiting for some input, the buttons can be controlled in the meantime
  while (!Serial.available()){
    // ---------------------- Button 1 toggling both LED 1 and LED 2
    // If button is pressed LEDs change only if the button was not pressed before, because clicking the button is not instant and will be held for some time
    if(millis() - toggleTime1 > debounce){
      if (!digitalRead(13)){
        if (b1Again){
          // Changing the state of LEDs based on their current value
          if (led1On){
            // Using analogWrite for LEDs just so they do not blind me with their full power
            analogWrite(11, 0);
            led1On = false;
          }
          else{
            analogWrite(11, 5);
            led1On = true;
          }
          if (led2On){
            analogWrite(10, 0);
            led2On = false;
          }
          else{
            analogWrite(10, 5);
            led2On = true;
          }
        b1Again = false;
        }
      }
      else{
        b1Again = true;
      }
      toggleTime1 = millis();
    }
    // ---------------------- Button 2 toggling LED 2
    if (millis() - toggleTime2 > debounce){
      if (!digitalRead(12)){
        if (b2Again){
          if (led2On){
            analogWrite(10, 0);
            led2On = false;
          }
          else{
            analogWrite(10, 5);
            led2On = true;
          }
        b2Again = false;
        }
      }
      else{
        b2Again = true;
      }
      toggleTime2 = millis();
    }
  }

  // When there is input the above while loop will end, and the chosen option will do some function in the switch
  answer = Serial.read();
  switch (answer){
    case 'a':
      for (int i = 0; i <= 17; i ++){
      Serial.println(i);
      }
      break;
    case 'b':
      if (led1On){
          analogWrite(11, 0);
          led1On = false;
        }
        else{
          analogWrite(11, 5);
          led1On = true;
        }
      break;
    case 'c':
      if (led2On){
          analogWrite(10, 0);
          led2On = false;
        }
        else{
          analogWrite(10, 5);
          led2On = true;
        }
      break;
    default: break;
  }
}
