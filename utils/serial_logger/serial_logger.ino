// The values from each analog pin
int a0;
int a1;
int a2;
int a3;
int a4;
int a5;

void setup()
{
    // Setting baud rate for serial communications
    Serial.begin(9600);
}

void loop()
{
    // Reading all analog pin values
    a0 = analogRead(A0);
    a1 = analogRead(A1);
    a2 = analogRead(A2);
    a3 = analogRead(A3);
    a4 = analogRead(A4);
    a5 = analogRead(A5);

    // Outputting to serial;

    Serial.print(a0);
    Serial.print(',');

    Serial.print(a1);
    Serial.print(',');

    Serial.print(a2);
    Serial.print(',');

    Serial.print(a3);
    Serial.print(',');

    Serial.print(a4);
    Serial.print(',');

    Serial.print(a5);
    Serial.println();
}