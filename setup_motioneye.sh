sudo apt update -y
sudo apt-get update -y
sudo apt-get upgrade -y
sudo cp -av ./motioneye-mqp/motioneye/ /etc/
sudo cp -av ./motioneye-mqp/sensorexamples/ /home/pi
sudo cp -av ./motioneye-mqp/Timelapse/ /home/pi
sudo cp -av ./motioneye-mqp/RaspberryPi/ /home/pi
sudo cp -av ./motioneye-mqp/dt-blob.dts /home/pi
sudo apt-get install -y ffmpeg libmariadb3 libpq5 libmicrohttpd12
sudo wget https://github.com/Motion-Project/motion/releases/download/release-4.2.2/pi_buster_motion_4.2.2-1_armhf.deb
sudo dpkg -i pi_buster_motion_4.2.2-1_armhf.deb
sudo apt-get install -y python-pip python-dev libssl-dev libcurl4-openssl-dev libjpeg-dev libz-dev
sudo pip install motioneye
sudo mkdir -p /etc/motioneye
sudo cp /usr/local/share/motioneye/extra/motioneye.conf.sample  /etc/motioneye/motioneye.conf
sudo mkdir -p /var/lib/motioneye
sudo cp /usr/local/share/motioneye/extra/motioneye.systemd-unit-local /etc/systemd/system/motioneye.service
sudo systemctl daemon-reload
sudo systemctl enable motioneye
sudo systemctl start motioneye
sudo pip install motioneye --upgrade
sudo systemctl restart motioneye
hostname -I
sudo apt-get install python-opencv -y
sudo apt-get install python3-opencv
cd ~/RaspberryPi/Motorized_Focus_Camera
chmod +x enable_i2c_vc.sh
./enable_i2c_vc.sh
sudo apt-get install at
sudo systemctl enable --now atd
sudo pip3 install --upgrade setuptools
sudo pip3 install RPI.GPIO
sudo pip3 install adafruit-blinka
sudo pip3 install adafruit-circuitpython-tsl2591
sudo pip3 install adafruit-circuitpython-as726x
sudo pip3 install adafruit-circuitpython-mprls
sudo pip3 install adafruit-circuitpython-lps35hw
sudo pip3 install adafruit-circuitpython-sgp30
sudo pip3 install adafruit-circuitpython-mcp9808
sudo pip3 install adafruit-circuitpython-bme280
sudo apt-get install bc

