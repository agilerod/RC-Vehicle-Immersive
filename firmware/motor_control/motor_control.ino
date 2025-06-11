/*
 * Motor Control for RC Vehicle Immersive Project
 * Arduino Nano ESP32
 * 
 * Controls:
 * - ESC for motor control (PWM)
 * - Servo for steering (PWM)
 * 
 * Communication:
 * - Serial (UART) from Jetson Nano
 * - Format: "S<steering>T<throttle>\n"
 *   where steering and throttle are -100 to 100
 */

#include <Arduino.h>
#include <ESP32Servo.h>
#include <WiFi.h>
#include <ArduinoOTA.h>
#include "config.h"

// Pin definitions
const int STEERING_PIN = 9;    // Servo control pin
const int THROTTLE_PIN = 10;   // ESC control pin

// Control limits
const int MIN_PULSE = 1000;    // Minimum pulse width (microseconds)
const int MAX_PULSE = 2000;    // Maximum pulse width (microseconds)
const int NEUTRAL_PULSE = 1500; // Neutral position pulse width

// Control objects
Servo steeringServo;
Servo throttleESC;

// Control variables
int steeringValue = 0;
int throttleValue = 0;

// Serial parsing
String inputString = "";
bool stringComplete = false;

// Servo object
Servo servoDireccion;

// Control variables
int angulo = 90;         // Initial center position

void setup() {
  // Initialize Serial
  Serial.begin(SERIAL_BAUD);
  Serial.println("RC Vehicle Control System");
  Serial.println("Available commands:");
  Serial.println("S<angle>: Set steering angle (0-180)");
  Serial.println("T<speed>: Set throttle (-100 to 100)");
  Serial.println("C: Center steering (90 degrees)");
  Serial.println("TEST: Run full sweep test");

  // Configure LED
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  // Configure Servo
  ESP32PWM::allocateTimer(0);
  ESP32PWM::allocateTimer(1);
  ESP32PWM::allocateTimer(2);
  ESP32PWM::allocateTimer(3);
  
  servoDireccion.setPeriodHertz(SERVO_FREQ);
  if (!servoDireccion.attach(SERVO_PIN, SERVO_MIN_PULSE, SERVO_MAX_PULSE)) {
    Serial.println("Error: Failed to initialize servo");
    while (1) {
      digitalWrite(LED_PIN, HIGH);
      delay(100);
      digitalWrite(LED_PIN, LOW);
      delay(100);
    }
  } else {
    Serial.println("Servo initialized successfully");
    servoDireccion.write(angulo);
    delay(1000); // Wait for servo to stabilize
  }

  // Configure WiFi
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to WiFi...");
  
  int wifiTimeout = 0;
  while (WiFi.status() != WL_CONNECTED && wifiTimeout < 20) {
    delay(500);
    Serial.print(".");
    wifiTimeout++;
  }
  
  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("\nConnected!");
    Serial.print("IP: ");
    Serial.println(WiFi.localIP());
  } else {
    Serial.println("\nError: Could not connect to WiFi");
  }

  // Configure OTA
  ArduinoOTA
    .onStart([]() {
      String type;
      if (ArduinoOTA.getCommand() == U_FLASH)
        type = "sketch";
      else // U_SPIFFS
        type = "filesystem";
      Serial.println("Starting update " + type);
    })
    .onEnd([]() {
      Serial.println("\nUpdate completed");
    })
    .onProgress([](unsigned int progress, unsigned int total) {
      Serial.printf("Progress: %u%%\r", (progress / (total / 100)));
    })
    .onError([](ota_error_t error) {
      Serial.printf("Error[%u]: ", error);
      if (error == OTA_AUTH_ERROR) Serial.println("Authentication failed");
      else if (error == OTA_BEGIN_ERROR) Serial.println("Begin failed");
      else if (error == OTA_CONNECT_ERROR) Serial.println("Connection failed");
      else if (error == OTA_RECEIVE_ERROR) Serial.println("Receive failed");
      else if (error == OTA_END_ERROR) Serial.println("End failed");
    });

  ArduinoOTA.begin();
  Serial.println("OTA ready");
}

void loop() {
  ArduinoOTA.handle();

  // Handle serial commands
  if (stringComplete) {
    processCommand(inputString);
    inputString = "";
    stringComplete = false;
  }
  
  // Update motor positions
  updateMotors();
  
  // Small delay to prevent overwhelming the serial port
  delay(10);
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      stringComplete = true;
    } else {
      inputString += inChar;
    }
  }
}

void processCommand(String command) {
  command.trim();
  
  if (command.startsWith("S")) {
    // Steering command
    int newAngle = command.substring(1).toInt();
    if (newAngle >= 0 && newAngle <= 180) {
      angulo = newAngle;
      servoDireccion.write(angulo);
      Serial.print("Steering set to ");
      Serial.println(angulo);
    } else {
      Serial.println("Error: Angle must be between 0 and 180");
    }
  }
  else if (command == "C") {
    // Center steering
    angulo = 90;
    servoDireccion.write(angulo);
    Serial.print("Steering centered at ");
    Serial.println(angulo);
  }
  else if (command == "TEST") {
    // Full sweep test
    Serial.println("Starting sweep test...");
    for (int i = 0; i <= 180; i += 5) {
      servoDireccion.write(i);
      Serial.print("Angle: ");
      Serial.println(i);
      digitalWrite(LED_PIN, HIGH);
      delay(100);
      digitalWrite(LED_PIN, LOW);
      delay(100);
    }
    for (int i = 180; i >= 0; i -= 5) {
      servoDireccion.write(i);
      Serial.print("Angle: ");
      Serial.println(i);
      digitalWrite(LED_PIN, HIGH);
      delay(100);
      digitalWrite(LED_PIN, LOW);
      delay(100);
    }
    Serial.println("Sweep test completed");
  }
  else {
void parseCommand(String command) {
  // Expected format: "S<steering>T<throttle>\n"
  int sIndex = command.indexOf('S');
  int tIndex = command.indexOf('T');
  
  if (sIndex != -1 && tIndex != -1) {
    // Extract steering value
    String steeringStr = command.substring(sIndex + 1, tIndex);
    steeringValue = steeringStr.toInt();
    
    // Extract throttle value
    String throttleStr = command.substring(tIndex + 1);
    throttleValue = throttleStr.toInt();
    
    // Constrain values
    steeringValue = constrain(steeringValue, -100, 100);
    throttleValue = constrain(throttleValue, -100, 100);
  }
}

void updateMotors() {
  // Convert -100 to 100 range to pulse width
  int steeringPulse = map(steeringValue, -100, 100, MIN_PULSE, MAX_PULSE);
  int throttlePulse = map(throttleValue, -100, 100, MIN_PULSE, MAX_PULSE);
  
  // Update servo positions
  steeringServo.writeMicroseconds(steeringPulse);
  throttleESC.writeMicroseconds(throttlePulse);
} 