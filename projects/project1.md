## 1. Automatic Class Attendance System

Automed time and attendance tracking system shall help save time and money by eliminating manual processes. With the system, teachers can more accurately and quickly see whether a student is in the class or not.

### Requirement

#### BLE Sensor
You need one of the hardware for the project.
* 1. [Raspberry Pi 3 with Bluetooth (BLE) built-in](https://www.adafruit.com/products/3055) 
* 2. [SparkFun ESP32 Thing](https://www.sparkfun.com/products/13907)


#### Mobile App (Android or iOS)
You will also need to write some code in either iOS or Android to communite with BLE chip and your backend server.

#### Backend Server
The backend server will handle the business logic of tracking student attendance and will also have a set of REST APIs for moible app or Raspberry Pi client to communicate.

The backend server must use either NOSQL including key-value store or RDBMS to store the data.

One single web page that shows all student attendance for teachers is required.
