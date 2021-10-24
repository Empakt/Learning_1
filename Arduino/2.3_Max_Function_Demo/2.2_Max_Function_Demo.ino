int x = 0;
int y = 0;
int max_result;
char answer;

void setup() 
{
  Serial.begin(9600);
  PrintMenu();
}

void loop() {
    
  while (!Serial.available())
  {
  }
  
  answer = Serial.read();

  switch (answer)
  {
    case '1':
      x=readInt();
      Serial.println(x);
      PrintMenu();
    break;
    case '2':
      y=readInt();
      Serial.println(y);
      PrintMenu();
    break;
    case '3':
      max_result = max_number(x,y);
      Serial.print("Max Number is: ");  
      Serial.println(y);
      PrintMenu();      
    break;

    default:
    break;
  }

}

int max_number (int n, int m)
{
  if (n>m)
  return n;
  else
  return m;
}

int readInt(void) //will read a positive integer in the range from 0 to 32767
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
   } while (inChar != '\n');
  value = inString.toInt();
  return value;
}

void PrintMenu()
{
  Serial.println("==============================");
  Serial.println("1.  Enter first number");  
  Serial.println("2.  Enter Second Number");  
  Serial.println("3.  Find Max Number");  
  Serial.println("=============================="); 
}
