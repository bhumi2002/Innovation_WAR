// https://forum.arduino.cc/index.php?topic=590442

byte servoPin = 9;

void setup()
{
  Serial.begin(9600);
  Serial.println("poor man's servo sweep");

  //turn off L13
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);

  pinMode(servoPin, OUTPUT);
  digitalWrite(servoPin, LOW);

} //setup

void loop()
{

    analogWrite(servoPin, 255);
    //delayMicroseconds(1900);    //position



} //loop
