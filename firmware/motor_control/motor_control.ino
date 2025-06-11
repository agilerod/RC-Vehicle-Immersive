#include <Arduino.h>
#include <ESP32Servo.h>
#include <WiFi.h>
#include <ArduinoOTA.h>
#include "config.h"

// Create servo object
Servo servoDireccion;

// Control variables
int angulo = 90;  // Center position
String inputString = "";      // String to hold incoming data
bool stringComplete = false;  // Whether the string is complete

void setup() {
  // Initialize serial communication
  Serial.begin(SERIAL_BAUD_RATE);
  inputString.reserve(200);

  // Configure LED
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  // Initialize servo
  ESP32PWM::allocateTimer(0);
  servoDireccion.setPeriodHertz(SERVO_FREQUENCY);
  if (!servoDireccion.attach(SERVO_PIN, SERVO_PULSE_WIDTH_MIN, SERVO_PULSE_WIDTH_MAX)) {
    Serial.println("Error: Failed to attach servo!");
    while (1) {
      digitalWrite(LED_PIN, HIGH);
      delay(100);
      digitalWrite(LED_PIN, LOW);
      delay(100);
    }
  }
  servoDireccion.write(angulo);  // Center the servo

  // Connect to WiFi
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to WiFi");
  int timeout = 0;
  while (WiFi.status() != WL_CONNECTED && timeout < 20) {
    delay(500);
    Serial.print(".");
    timeout++;
  }
  Serial.println();

  if (WiFi.status() == WL_CONNECTED) {
    Serial.print("Connected! IP address: ");
    Serial.println(WiFi.localIP());
    digitalWrite(LED_PIN, HIGH);
  } else {
    Serial.println("Failed to connect to WiFi");
    digitalWrite(LED_PIN, LOW);
  }

  // Configure OTA
  ArduinoOTA.setHostname("rc-vehicle");
  ArduinoOTA.onStart([]() {
    String type = (ArduinoOTA.getCommand() == U_FLASH) ? "sketch" : "filesystem";
    Serial.println("Start updating " + type);
    digitalWrite(LED_PIN, HIGH);
  });
  
  ArduinoOTA.onEnd([]() {
    Serial.println("\nEnd");
    digitalWrite(LED_PIN, LOW);
  });
  
  ArduinoOTA.onProgress([](unsigned int progress, unsigned int total) {
    Serial.printf("Progress: %u%%\r", (progress / (total / 100)));
  });
  
  ArduinoOTA.onError([](ota_error_t error) {
    Serial.printf("Error[%u]: ", error);
    if (error == OTA_AUTH_ERROR) Serial.println("Auth Failed");
    else if (error == OTA_BEGIN_ERROR) Serial.println("Begin Failed");
    else if (error == OTA_CONNECT_ERROR) Serial.println("Connect Failed");
    else if (error == OTA_RECEIVE_ERROR) Serial.println("Receive Failed");
    else if (error == OTA_END_ERROR) Serial.println("End Failed");
  });
  
  ArduinoOTA.begin();
  Serial.println("OTA Ready");
}

void processCommand(String command) {
  command.trim();
  
  if (command.startsWith("S")) {
    // Steering command
    int newAngle = command.substring(1).toInt();
    if (newAngle >= 0 && newAngle <= 180) {
      angulo = newAngle;
      servoDireccion.write(angulo);
      Serial.print("Steering set to: ");
      Serial.println(angulo);
    }
  }
  else if (command == "C") {
    // Center steering
    angulo = 90;
    servoDireccion.write(angulo);
    Serial.println("Steering centered");
  }
  else if (command == "T") {
    // Sweep test
    Serial.println("Starting sweep test");
    for (int i = 0; i <= 180; i += 10) {
      servoDireccion.write(i);
      delay(100);
    }
    for (int i = 180; i >= 0; i -= 10) {
      servoDireccion.write(i);
      delay(100);
    }
    servoDireccion.write(90);
    Serial.println("Sweep test complete");
  }
}

void loop() {
  ArduinoOTA.handle();
  
  if (stringComplete) {
    processCommand(inputString);
    inputString = "";
    stringComplete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    inputString += inChar;
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
} 