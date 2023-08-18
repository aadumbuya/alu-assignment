import requests
import json

url = "https://apjoy-weather-forecast.p.rapidapi.com/forecast"

city = ""
days = ""

querystring = {"location": city,"days": days}

headers = {
	"X-RapidAPI-Key": "9fb66d6a18mshf0801c4fdb009cep14b82ejsnd0804f5c1798",
	"X-RapidAPI-Host": "apjoy-weather-forecast.p.rapidapi.com"
}

# response = requests.get(url, headers=headers, params=querystring)

# json_response = response.json()

# with open('weather-forecast_nb.json', 'w') as outfile:
# 	json.dump(json_response, outfile, indent=4)

with open('weather-forecast_nb.json') as json_file:
	json_data = json.load(json_file)

status = json_data['cod']
program = True
while program:
	if status == '200':
		print("Weather Forecast Program")
		print("-------------------------------------------")
		print("1. Search Weather Forecast")
		print("2. Exit")
		print("-------------------------------------------")
		choice = input("Enter your choice: ")
		if choice == '1':
			city = input("Enter city name: ")
			days = input("Enter number of days: ")
			querystring = {"location": city,"days": days}
			response = requests.get(url, headers=headers, params=querystring)
			json_data = response.json()
			
			status = json_data['cod']
			if status == '200':
				print("Weather Forecast for " + json_data['city']['name'] + ", " + json_data['city']['country'])
				print("---------------------------------------------------------------------")
				for i in range(0, int(days)):
					print("Date: " + json_data['list'][i]['dt_txt'])
					print("Weather: " + json_data['list'][i]['weather'][0]['main'])
					print("Description: " + json_data['list'][i]['weather'][0]['description'])
					print("Temperature: " + str(json_data['list'][i]['main']['temp']) + "°C")
					print("Pressure: " + str(json_data['list'][i]['main']['pressure']) + " hPa")
					print("Humidity: " + str(json_data['list'][i]['main']['humidity']) + "%")
					print("Wind Speed: " + str(json_data['list'][i]['wind']['speed']) + " m/s")
					print("---------------------------------------------------------------------")
			else:
				print("Error: " + json_data['message'])
		elif choice == '2':
			program = False
		else:
			print("Invalid choice")
	else:
		print("Error: " + json_data['message'])
		program = False

print("Thank you for using the Weather Forecast Program")


