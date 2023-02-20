#include <LiquidCrystal.h>

#define TICK 0.0000000000000000000000000000000000000000000000000000  // the amount of milliseconds between any stopwatch update
const int SWPin = 10;  
const int XPin = 0;  
const int YPin = 1;  
int seconds = 0;
int minutes = 0;
int hours = 0;
bool on = true;
// int onTime = 0;
// int offTime = 0;
// int durTime = 0;
int startTime = 0;
int DUR = 0;

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);  // RS,EN,D4,D5,D6,D7 pin of LCD respectively
#define LED_PIN 9
/*
Arduino Turn LED On/Off using Serial Commands
Created April 22, 2015
Hammad Tariq, Incubator (Pakistan)

It's a simple sketch which waits for a character on serial
and in case of a desirable character, it turns an LED on/off.

Possible string values:
a (to turn the LED on)
b (tor turn the LED off)
*/

char junk;
String inputString="";

void SSET()                    // run once, when the sketch starts
{
 Serial.begin(115200);            // set the baud rate to 9600, same should be of your Serial Monitor
 pinMode(13, OUTPUT);
//  Serial.println("hi");
}

void SYES() {
  if(Serial.available()) {
    while(Serial.available()) {
      char inChar = (char)Serial.read();
      if (inChar == '\n') {
        inputString.trim(); // remove leading/trailing whitespace
        // Serial.println(inputString);
        
        if (inputString.startsWith("start time:")) {
          startTime = inputString.substring(11).toInt();
          // Serial.print("Start time set to: ");
          // Serial.println(startTime);
        }      
        if (inputString.startsWith("duration:")) {
          DUR = inputString.substring(9).toInt();
          // Serial.print("duration set to: ");
          // Serial.println(DUR);
        }        
        if(inputString == "c") {
          lcd.setCursor(0,1);
          lcd.print("                   ");
          while(true) {
            if(analogRead(YPin) == 0) {
              on = true;
            }
            if(analogRead(YPin) == 1023) {
              on = false;
            }
        if(on == true) {
          LCD();
        }
      }
    }
        inputString = "";
      } else {
        inputString += inChar;
      }
    }

    lcd.setCursor(0,0);
    lcd.print("Start Time:");
    lcd.print(startTime);
    lcd.setCursor(0,1);
    lcd.print("Duration time:");
    lcd.print(DUR);
  }
}


// void SYES() {
//   if(Serial.available()) {
//     while(Serial.available()) {
//       char inChar = (char)Serial.read(); //read the input
//       inputString += inChar;        //make a string of the characters coming on serial
//     }
//     Serial.println(inputString);
//     while (Serial.available() > 0) { junk = Serial.read() ; }  // clear the serial buffer
    
// if (inputString.startsWith("start time:")) { // check if input starts with "start time:"
//   startTime = inputString.substring(11).toInt(); // convert the number part of input to integer and assign it to startTime
//   Serial.print("Start time set to: ");
//   Serial.println(startTime);
// }
    
//     // if(inputString == "a") {  //in case of 'a' turn the LED on
//     //   onTime ++;
//     //   if(onTime > 23) {
//     //     onTime = 0;
//     //   }
//     // }
//     // else if(inputString == "b") { //incase of 'b' turn the LED off
//     //   onTime = onTime - 1;
//     //   if(onTime < 0) {
//     //     onTime = 23;
//     //   }
//     // }
//     // if(inputString == "x") {
//     //   durTime ++;
//     // }
//     // if(inputString == "y") {
//     //   durTime = durTime - 1;
//     //   if(durTime < 0) {
//     //     durTime = 0;
//     //   }
//     // }
//     if(inputString == "c") {
//       lcd.setCursor(0,1);
//       lcd.print("                   ");
//       while(true) {
//         if(analogRead(YPin) == 0) {
//           on = true;
//         }
//         if(analogRead(YPin) == 1023) {
//           on = false;
//         }
//         if(on == true) {
//           LCD();
//         }
//       }
//     }
//     inputString = "";
//     lcd.print("           ");
//     lcd.setCursor(0,0);
//     lcd.print("ST:");
//     lcd.print(startTime);
//     // lcd.setCursor(0,1);
//     // lcd.print("Duration:");
//     // print_padded_number(DUR);
//   }
// }



void init_lcd() {
  lcd.begin(16, 2);  // sets the number of columns and rows
  pinMode(LED_PIN, OUTPUT);
  lcd.setCursor(0, 0);
}

void increment_time() {
  seconds++;

  if (seconds > 30) {
    seconds = 0;
    minutes++;
  }
  if (minutes > 59) {
    minutes = 0;
    hours++;
  }
  if (hours > 23) {
    hours = 0;
  }
}

void print_padded_number(int number) {
  if (number < 10) lcd.print("0");
  lcd.print(number);
}

void print_time() {
  lcd.setCursor(0, 1);

  digitalWrite(LED_PIN, (hours+1) > startTime && (hours) < startTime + DUR ? HIGH : LOW);

  print_padded_number(hours);
  lcd.print(":");
  print_padded_number(minutes);
  lcd.print(":");
  print_padded_number(seconds);
}



void LCDSET() {
  init_lcd();
}

void LCD() {
  increment_time();
  print_time();
  delay(TICK);
}

void JOYSET() {  
  pinMode(SWPin, INPUT); 
}  

void setup(){
  SSET();
  LCDSET();
	JOYSET();
}

void loop(){
  SYES();
}
