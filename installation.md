These are the details of how I installed the various packages used in this project

I use rmate to remotely edit the files on the raspberry pi using Sublime text locally
https://acarril.github.io/posts/ssh-sripts-st3


# Servos

Based on instructions here: https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython
and here: https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi

Run their setup script
> cd ~
sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py

Install the packages:
> sudo pip3 install adafruit-circuitpython-pca9685
sudo pip3 install adafruit-circuitpython-servokit


# Facial Recognition (CV2)

These are the commands for setting up facial recognition (these two sites have nearly identical instructions, I think the second one is the "official" one)
	https://core-electronics.com.au/tutorials/face-identify-raspberry-pi.html
	https://www.tomshardware.com/how-to/raspberry-pi-facial-recognition

> pip install picamera[array]
sudo apt-get update
sudo apt-get upgrade
sudo apt install cmake build-essential pkg-config git
sudo apt install libjpeg-dev libtiff-dev libjasper-dev libpng-dev libwebp-dev libopenexr-dev
sudo apt install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libdc1394-22-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev
sudo apt install libgtk-3-dev libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
sudo apt install libatlas-base-dev liblapacke-dev gfortran
sudo apt install libhdf5-dev libhdf5-103
sudo apt install python3-dev python3-pip python3-numpy

We must now expand the swapfile before running the next set of commands. To do this edit swapfile, change the value from 100 to 2048, then restart swapfile (we'll change this back later)
> sudo nano /etc/dphys-swapfile
sudo systemctl restart dphys-swapfile

More steps
> git clone https://github.com/opencv/opencv.git
git clone https://github.com/opencv/opencv_contrib.git
mkdir ~/opencv/build
cd ~/opencv/build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D OPENCV_EXTRA_MODULES_PATH=~/projects/opencv_contrib/modules \
-D ENABLE_NEON=ON \
-D ENABLE_VFPV3=ON \
-D BUILD_TESTS=OFF \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D OPENCV_ENABLE_NONFREE=ON \
-D CMAKE_SHARED_LINKER_FLAGS=-latomic \
-D BUILD_EXAMPLES=OFF ..
make -j$(nproc)
sudo make install
sudo ldconfig
pip install face-recognition --no-cache-dir
pip install imutils
- 

We must now return the swapfile before running the next set of commands. Edit the file again, resetting the value to 100 (from 2048).
> sudo nano /etc/dphys-swapfile
sudo systemctl restart dphys-swapfile

Grab the software to test things out
> git clone https://github.com/carolinedunn/facial_recognition


# Fix Python path

For some reason, the CV2 packages were not added to sys.path for Python3 (they worked fine for Python2).  These steps show how to add the packages to the Python3 path

Installing collected packages: face-recognition-models, dlib, face-recognition
The scripts face_detection and face_recognition are installed in '/home/pi/.local/bin' which is not on PATH.

cv2 was installed to /usr/local/lib/python3.7/site-packages/cv2 but was not in the Python3 sys.path, so I had to create a new file (basically, add /usr/local/lib to sys.path)
> /home/pi/.local/lib/python3.7/site-packages/site-packages.pth

with the contents of 
> /usr/local/lib/python3.7/site-packages

