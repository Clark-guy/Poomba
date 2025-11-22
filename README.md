#Roomba control

This project is designed to control a Roomba 530 from a raspberry pi via a Roomba Create 2 USB cable
to run the flask app that lets you control the roomba, run `python app.py`
to just run a test jingle, run `python test.py`

Current TODO
 - Ensure that the roomba can store up enough power for the Pi 4. Might make more sense to use a Pi Zero for this...
    - Shopping list
      - pi zero 2 W
      - USB Micro to USB A cable
      - pin headers?
 - write out controls in the flask app so the buttons can be used to move the roomba around
 - alternative buttons that just let the roomba control itself
 - Camera mount
  - Ace hardware or something? Need just some basic brackets or something\
  - Legos are not off the table
  - just like.. bent aluminum? Or other metal... 
  - Wood? I dunno


Installs:
 - flask
 - picamera2 - apt-get
 - python3-opencv - apt-get
 - serial

To install - generate a new python venv with python -m venv venv
switch to the venv with . ./venv/bin/activate
install requirements with pip install -r requirements.txt

sudo apt install -y python3-dev ffmpeg libavformat-dev libavcodec-dev libavdevice-dev libavutil-dev libswscale-dev libswresample-dev libavfilter-dev

installed python3-picamera2 with apt instead of pip because pip was giving me shit
