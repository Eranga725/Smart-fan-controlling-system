Smart Fan Controlling System
This project is a smart fan-controlling system using image processing and hand gesture recognition. The system uses a webcam to detect hand gestures and controls the speed and direction of a fan based on the recognized gestures.

Table of Contents
Introduction
Features
Requirements
Installation
Usage
Contributing
License
Introduction
The smart fan controlling system leverages OpenCV for image processing and hand gesture recognition. It uses a webcam to capture real-time video, detect hand gestures, and control the fan's speed and direction based on the gestures.

Features
Recognizes different hand gestures to control fan speed and direction.
Provides real-time feedback on the recognized gesture and the corresponding fan state.
Utilizes Arduino and PyFirmata for hardware control of the fan.
Requirements
Python 3.x
OpenCV
cvzone
pyfirmata
Arduino board
Installation
Clone the repository:

sh
Copy code
git clone https://github.com/your-username/smart-fan-control.git
cd smart-fan-control
Install the required Python packages:

sh
Copy code
pip install opencv-python cvzone pyfirmata
Connect your Arduino board to your computer.

Usage
Upload the standard firmata sketch to your Arduino board using the Arduino IDE. You can find the sketch in File -> Examples -> Firmata -> StandardFirmata.

Modify the comport variable in the moter.py script to match the COM port your Arduino is connected to.

Run the smart_fan_control.py script:

sh
Copy code
python smart_fan_control.py
The webcam will start, and you can control the fan using the following gestures:

All fingers down: Fan OFF
Thumb up: Fan ON at low speed
Index finger up: Fan ON at medium speed
Middle finger up: Fan ON at high speed
All fingers up: Fan ON in reverse at medium speed
