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
      - camera adapter
 - write out controls in the flask app so the buttons can be used to move the roomba around
 - alternative buttons that just let the roomba control itself
 - camera functionality?