int pinOut = 10;
int pinA = 8;
int pinB = 9;




void setup() {
  // put your setup code here, to run once:
  pinMode(pinOut, OUTPUT);
  pinMode(pinA, INPUT);
  pinMode(pinB, INPUT);


}

void loop() {
  // AND Gate
  boolean pinAState = digitalRead(pinA);
  boolean pinBState = digitalRead(pinB);
  boolean pinOutState;
  // and
  pinOutState =pinAState & pinBState;
  pinOutState = pinAState ^ pinBState;
  digitalWrite(pinOut, pinOutState);

  // XOR
  //pinOutState = pinAState ^ pinBState;


}
