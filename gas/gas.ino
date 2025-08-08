void setup(){
  Serial.begin(9600);
}

void loop(){
  int gas = analogRead(A0);

    if(gas<600){
      Serial.print(gas);
      Serial.println(", OK");
    }
    else if(gas>=600){
      Serial.print(gas);
      Serial.println(", WARNING");
    }
    delay(500);
}
