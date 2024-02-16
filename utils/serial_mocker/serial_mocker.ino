void setup()
{
    // Setting baud rate for serial communications
    Serial.begin(9600);
}

void loop()
{
    // Reading the analog signal at pin A0
    int value = analogRead(A0);

    // Outputting the value to serial
    Serial.println(value);
}