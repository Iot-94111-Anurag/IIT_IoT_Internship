#include <WiFi.h>

#define MQ2_ANALOG_PIN 34  // Analog pin
#define MQ2_DIGITAL_PIN 15 // Digital pin

void setup() {
  Serial.begin(115200);

  pinMode(MQ2_DIGITAL_PIN, INPUT);
  analogReadResolution(12); // 0-4095 for ESP32
}

void loop() {
  // Read digital output
  int digitalValue = digitalRead(MQ2_DIGITAL_PIN);
  Serial.print("Digital Output: ");
  Serial.println(digitalValue); // 1 = no gas, 0 = gas detected

  // Read analog output
  int analogValue = analogRead(MQ2_ANALOG_PIN);
  float voltage = analogValue * (3.3 / 4095.0); // Convert to voltage
  Serial.print("Analog Output: ");
  Serial.print(analogValue);
  Serial.print(" | Voltage: ");
  Serial.println(voltage);

  // Simple threshold logic
  if (analogValue > 2000) { // adjust threshold based on calibration
    Serial.println("WARNING: Gas/Smoke Detected!");
  }

  delay(2000);
}