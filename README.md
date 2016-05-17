## Temp-SpreadSheet
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
sudo pip install gspread oauth2client
```

## Get OAuth2 credentials
Visit on website http://gspread.readthedocs.io/en/latest/oauth2.html and follow them.

## Edit config file for ```w1-gpio```
```Note``` If you don't use DS18B20 please skip ```Clone repository``` caption.
```bash
sudo nano /boot/config.txt
```
Look at ```#dtoverlay=w1-gpio``` and uncomment ```dtoverlay=w1-gpio```

## Connect Raspberry Pi with DS18B20

![RasPi](image.png?raw=true "RasPi")

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
