/******************************************************
* sample code to exercise glitching a 328p
* 
* After powering up, the code will put out a short 
* identifier, then start asking for a password. (over UART)
*
* User can try as many times as they want, there is
* no limit.
*
* If correct password is entered, the user will get a
* "$>" prompt.
*
* The goal is the inject a power or other fault just
* as the password is being checked and thereby bypass
* password checking.
*******************************************************/

#define MAX_PWD_LEN 32
#define CONSOLE_BUFFER_LEN 64

static const char* PASSWORD = "myP4ssw0rd";
static bool consoleEnabled = false;

char consoleBuffer[CONSOLE_BUFFER_LEN] = {'\0'};

int simpleCLILoop(const char* prompt);
int readCommandFromUART(const char* prompt);

void setup() {
  Serial.begin(115200);
  Serial.println("************************************\r\n Test glitch target (victim), v 0.9\r\n************************************");
}

void loop() {
  // put your main code here, to run repeatedly:
  simpleCLILoop("$> ");
}


/******************************************
* This method is called continually to get
* user interactivity over UART.  If the 
* password has not yet been entered, this
* method will continually poll for it
* until it is found.
*
* This method may seem strange, and even
* a bit contrived, but it is somethine that
* I pulled almost exactly from a consumer
* IoT device.
*
* Yes, there is a stack-based buffer overflow
* here (and is in the actual device out in
* the world, too.)
******************************************/
int simpleCLILoop(const char* prompt) {

  char password[MAX_PWD_LEN] = {'\0'};
  uint8_t pwdInx;
  int readChar;
  int compareResult;

  // if password has been entered (consoleEnabled == true), then
  // skip this whole block.  Otherwise keep trying until correct
  // password has been entered.
  while (!consoleEnabled) {
    Serial.println("### Please enter password ###\r\n");  // prompt user
    pwdInx = 0;  // entered password character counter

    // loop runs continuously until <RETURN> key pressed
    while (true) {  
      if (Serial.available() > 0) {     // wait for UART rx
        readChar = Serial.read();       // get that char
        readChar &= 0xff;               // mask off lower 8 bits

        if (readChar == '\r') {         // user hit <RETURN>
          break;                        // so break out of forever while() loop
        } else if (readChar == '\b') {  // user hit <BACKSPACE>
          if (pwdInx > 0) {             // if at least one char has been entered
            --pwdInx;                   // decrement entered password char count
            Serial.print("\b \b");      // send backspace, space, backspace over UART
          }                             // to clear the last '*'
        } else {                        // not <RETURN> or <BACKSPACE>
          password[pwdInx] = readChar;  // append the this char to the user's password entry
          ++pwdInx;                     // increment the entered password char count
          Serial.print('*');            // print out an asterix
        } // testing entered UART char
      } // waiting for UART char
    } // main while() loop

    password[pwdInx] = '\0';            // null terminate user entered password

    // compare user entry to "good" password
    compareResult = strcmp(PASSWORD, password);

    if (!compareResult) {
      consoleEnabled = true;            // set bit to indicate password is good!
    }

    Serial.println("");                 // print out a newline
  } // while (!consoleEnabled)

  *consoleBuffer = '\0';
  return (readCommandFromUART(prompt));
}


/******************************************
*                                         *
******************************************/
int readCommandFromUART(const char* prompt) {
  bool enterd = false;
  int readChar = 0;
  int readInx = 0;

  Serial.print(prompt);

  while (!enterd) {
    if (Serial.available() > 0) {
      readChar = Serial.read();
      readChar &= 0xff;

      if (readChar == '\r') {
        break;
      } else if (readChar == '\b') {
        if (readInx > 0) {
          --readInx;
          Serial.print("\b \b");
        }
      } else {
        consoleBuffer[readInx] = readChar;
        ++readInx;
        Serial.print((char)readChar);

        // dont allow a buffer overflow here
        if (readInx == (CONSOLE_BUFFER_LEN - 1)) {
          break;
        }
      }
    }
  }

  consoleBuffer[readInx] = '\0';
  Serial.println("");

  if (strlen(consoleBuffer)) {
    if (!strcmp("info", consoleBuffer)) {
      Serial.println("Target info:");
      Serial.print("\t'consoleEnabled': ");
      (consoleEnabled) ? Serial.println("true") : Serial.println("false");
    } else if (!strcmp("help", consoleBuffer)) {
      Serial.println("\tThis is just a small example, there really isn't any kind of command");
      Serial.println("\tprocessing.  Only commands are 'help', 'reboot', and 'info.");
    } else if (!strcmp("reboot", consoleBuffer)) {
      // kind of a sledgehammer - jump to the reset vector to reboot.
      asm("jmp 0");
    } else {
      Serial.print("'");
      Serial.print(consoleBuffer);
      Serial.println("' isn't a supported command.");
    }
  } 

  return (strlen(consoleBuffer));
}