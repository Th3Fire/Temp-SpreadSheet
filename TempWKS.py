import gspread,datetime
from oauth2client.service_account import ServiceAccountCredentials
from time import sleep
from ds18b20 import DS18B20

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('Temp-3914c1792c0b.json', scope) ## Temp-3914c1792c0b.json replace Your Json file
gc = gspread.authorize(credentials)

wks = gc.open("Temp").sheet1  ## Temp replace your Work sheet name

def main():
	sensor = DS18B20()
	
	while True:
		time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
		temperatures = sensor.get_temperatures([DS18B20.DEGREES_C, DS18B20.DEGREES_F, DS18B20.KELVIN])
		
		print time
       		print("Degrees Celsius: %f" % temperatures[0])
       		print("Kelvin: %f" % temperatures[2])
	 	print("Degrees Fahrenheit: %f" % temperatures[1])
		print("Adding row please wait...")
		
		x = 0
		try:
			for values in wks.col_values(1):  ## loop count row
    				x = x + 1
			rowToAdd = [time, temperatures[0], temperatures[2], temperatures[1]] ## your data want to send
			wks.resize(x)
			wks.append_row(rowToAdd)
			print("Add row done !!!")
			print("==================================")
			sleep(5)
		except:
			print("Exit.")
			print("Bye...")
			break;

if __name__ == "__main__":
	main()
