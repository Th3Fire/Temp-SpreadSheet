## Temp-SpreadSheet

[![Build Status](https://drone.io/github.com/wuttinunt/Temp-SpreadSheet/status.png)](https://drone.io/github.com/wuttinunt/Temp-SpreadSheet/latest)
[![Build Status](https://travis-ci.org/wuttinunt/Temp-SpreadSheet.svg?branch=master)](https://travis-ci.org/wuttinunt/Temp-SpreadSheet)

DS18B20 temperature device

Send data from Raspberry Pi to Spreadsheets (Google Docs)

## First you need todo
* You need have Google account.
* Use Google docs service for Spreadsheet.
* Create Work Sheet

## Install package
```bash
sudo apt-get update
sudo apt-get install python-pip
sudo apt-get install git
sudo pip install gspread oauth2client PyOpenSSL
```

## Get OAuth2 credentials
Visit on website http://gspread.readthedocs.io/en/latest/oauth2.html and follow them.

## How to get credentials
1. Goto https://console.developers.google.com 
2. create project(or select the one you have)
3. In tab Google APIs look at Google Apps APIs > Drive API > Enable
4. In left sidebar menu select ```Credentials``` > Look at drop down menu Create credentials > select ```Service account key```
5. Service account > select ```New service account``` > Set name of service account > Key type > select ```JSON``` 
6. Click ```Create``` wait a second you'll get a json file.


## Edit config file for ```w1-gpio```
```Note``` If you don't use DS18B20 please skip ```Clone repository``` caption.
```bash
sudo nano /boot/config.txt
```
Look at ```#dtoverlay=w1-gpio``` and uncomment ```dtoverlay=w1-gpio```

## Connect Raspberry Pi with DS18B20

![RasPi](https://github.com/wuttinunt/temperature-thingspeak/raw/master/image.png??raw=true "RasPi")

## Install DS18B20 and Kernel Module
```bash
sudo pip install ds18b20
sudo modprobe w1-gpio
sudo modprobe w1-therm
```
Look some Directory ``` /sys/bus/w1/devices ``` you'll see directory 28-XXXXXXXXXXX
try:
```bash
cat/sys/bus/w1/devices/28-XXXXXXXXXXX/w1_slave
```
you'll see some value it's ready to work
if you don't see Directory ensure you connect Raspberry Pi with DS18B20 already.

## Clone repository
```bash
git clone https://github.com/wuttinunt/Temp-SpreadSheet.git
cd Temp-SpreadSheet
```

## Important !!!
copy json file (get from create credentials at Get OAuth2 credentials caption)
please ensure ```json file``` must at same directory with TempWKS.py.

## Run
```bash
sudo python TempWKS.py
```
