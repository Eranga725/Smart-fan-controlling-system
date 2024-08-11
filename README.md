# Smart-fan-controlling-system
The Smart Fan Controlling System is an innovative project that uses image processing and hand gesture recognition to control the speed and direction of a fan. By leveraging a webcam, OpenCV, and the cvzone library, this system captures real-time video to detect hand gestures, which are then translated into commands for the fan.

# Table of Contents
<ul style="list-style-type:disc;">
  <li>Recognizes different hand gestures to control fan speed and direction.</li>
  <li>Provides real-time feedback on the recognized gesture and the corresponding fan state.</li>
  <li>Utilizes Arduino and PyFirmata for hardware control of the fan.</li>
</ul>

# Introduction
The smart fan controlling system leverages OpenCV for image processing and hand gesture recognition. It uses a webcam to capture real-time video, detect hand gestures, and control the fan's speed and direction based on the gestures.

# Features
<ul style="list-style-type:disc;">
  <li>Recognizes different hand gestures to control fan speed and direction.</li>
  <li>Provides real-time feedback on the recognized gesture and the corresponding fan state.</li>
  <li>Utilizes Arduino and PyFirmata for hardware control of the fan.</li>
</ul>

# Requirements
<ul style="list-style-type:disc;">
  <li>Python 3.x</li>
  <li>OpenCV</li>
  <li>pyfirmata</li>
  <li>Arduino board</li>
</ul>

# Installation
<ol type="1">
  <li>Clone the repository:</li>
  <ul style="list-style-type:disc;">
    <li>git clone https://github.com/Eranga725/Smart-fan-controlling-system</li>
    <li>cd smart-fan-control</li>
  </ul>
  <br>
  <li>
    Install the required Python packages:
  <ul style="list-style-type:disc;">
    <li>pip install opencv-python cvzone pyfirmata</li>
  </ul>    
  </li>
<br>
<li>Connect your Arduino board to your computer.</li>
