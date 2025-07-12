import requests, json
with open("Api.json", "r") as api:
	weatherAPI= json.load(api)["api"][0]["weatherapi"]
base_url="https://api.openweathermap.org/data/2.5/weather?q="
class Weather:
	def __init__(self, city):
		self.city=city
	def weather(self):
		url=base_url +self.city+"&appid=" + weatherAPI
		result= requests.get(url).json()
		if int(result["cod"])!=404:
			return result
		else:
			return False