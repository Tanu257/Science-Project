float duration1,duration3,distance1,distance2,duration2,distance3; 

int trigPin1 = 2;
int echoPin1 =3;
int trigPin2 = 4;
int echoPin2 =5;
int trigPin3 = 8;
int echoPin3 =9;


void setup() {
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
  pinMode(trigPin3, OUTPUT);
  pinMode(echoPin3, INPUT);
  pinMode(7,OUTPUT);

  Serial.begin(115200);

}
void loop() {
  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(10);
  
  digitalWrite(trigPin1, LOW);
  

  // measure duration of pulse from ECHO pin
  duration1 = pulseIn(echoPin1, HIGH);
  
  digitalWrite(trigPin2, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin2, LOW);
  duration2 = pulseIn(echoPin2, HIGH);
  
  digitalWrite(trigPin3, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin3, LOW);
  duration3 = pulseIn(echoPin3, HIGH);

  // calculate the distaance

  //Front
  distance1 = 0.017 *duration1;
  //Left
  distance2 = 0.017* duration2;
  //Right
  distance3 = 0.017* duration3;
 
  Serial.print(distance1);
  Serial.print("ALN");
  Serial.print(distance2);
  Serial.print("ALN");
  Serial.print(distance3);
  Serial.println("");
  
  delay(500);
  }
