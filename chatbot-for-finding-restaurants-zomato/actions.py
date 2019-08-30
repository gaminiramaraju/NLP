from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import zomatopy
import json

zomato_config={ "user_key":"b085b42d0a230b37f78fa205275154d2"}
result_of_last_query = ""

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant_search'

	def searchRestaurants(self, user_price_range, allRestaurants):
		rangeMin = 0
		rangeMax = 100000

		if user_price_range.isdigit():
			price = int(user_price_range)
			
			if price == 1:
				rangeMax = 499
			elif price == 2:
				rangeMin = 500
				rangeMax = 999
			elif price == 3:
				rangeMin = 1000
			elif price < 500:
				rangeMax = 499
			elif price < 1000 and price >= 500:
				rangeMin = 500
				rangeMax = 999
			else:
				rangeMin = 1000
		else:
			#default
			rangeMin = 100
			rangeMax = 999

		index = 0
		count = 0
		response = ""
		global result_of_last_query
		result_of_last_query = ""

		for restaurant in allRestaurants:
			++count
			res =  restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address'] + " has been rated [" +  restaurant['restaurant']['user_rating']['aggregate_rating'] + "/5] \n"

			# price_range = str(restaurant['restaurant']['price_range'])
			avg_c_2 = restaurant['restaurant']['average_cost_for_two']
			
			# if price_range == "1":
			
			if avg_c_2 <= rangeMax and avg_c_2 >= rangeMin:
			   
				if(index < 5):
					response = response + res

				if(index < 10):
					result_of_last_query = result_of_last_query + res
				index = index + 1

		# modifying the search results
		# if the no. of result fall short, appending the results of other price range
		if index == 0:
			response = "Oops! no restaurant found for this query. " + " search results = " + str(count)
		elif index < 5:
			# we can add restaurants from the higher range but for now i am appending an extra message 
			response = response + "\n \nFor more results please search in higher budget range...\n \n"
		elif index < 10:
			result_of_last_query = result_of_last_query + "\n \nFor more results please search in higher budget range...\n \n"

		return response

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price_range = tracker.get_slot('price_range')
		
		zomato = zomatopy.initialize_app(zomato_config)
		location_detail=zomato.get_location(loc, 1)

		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		
		cuisines_dict={
		'american':1,
		'mexican':2,
		'italian':3,
		'chinese':4,
		'north indian':5,
		'south indian':6
		}

		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 4)

		d = json.loads(results)
		response=""

		if d['results_found'] == 0:
			response= "Sorry, we didn't find any results for this query."
		else:
			dispatcher.utter_message(price_range)
			response = self.searchRestaurants(price_range, d['restaurants'])

		dispatcher.utter_message(str(response))
		return [SlotSet('location',loc)]


cities = ["Ahmedabad","Bangalore","Chennai","Delhi","Hyderabad","Kolkata","Mumbai","Pune",
"Agra","Ajmer","Aligarh","Allahabad","Amravati","Amritsar","Asansol","Aurangabad",
"Bareilly","Belgaum","Bhavnagar","Bhiwandi","Bhopal","Bhubaneswar",
"Bikaner","Bokaro Steel City","Chandigarh","Coimbatore","Cuttack","Dehradun",
"Dhanbad","Durg-Bhilai Nagar","Durgapur","Erode","Faridabad","Firozabad","Ghaziabad",
"Gorakhpur","Gulbarga","Guntur","Gurgaon","Guwahati",
"Gwalior","Hubli-Dharwad","Indore","Jabalpur","Jaipur","Jalandhar","Jammu","Jamnagar","Jamshedpur","Jhansi","Jodhpur",
"Kannur","Kanpur","Kakinada","Kochi","Kottayam","Kolhapur","Kollam","Kota","Kozhikode","Kurnool","Lucknow","Ludhiana",
"Madurai","Malappuram","Mathura","Goa","Mangalore","Meerut",
"Moradabad","Mysore","Nagpur","Nanded","Nashik","Nellore","Noida","Palakkad","Patna","Pondicherry","Raipur","Rajkot",
"Rajahmundry","Ranchi","Rourkela","Salem","Sangli","Siliguri",
"Solapur","Srinagar","Sultanpur","Surat","Thiruvananthapuram","Thrissur","Tiruchirappalli","Tirunelveli","Tiruppur",
"Ujjain","Vijayapura","Vadodara","Varanasi",
"Vasai-Virar City","Vijayawada","Visakhapatnam","Warangal"]

cities_list = [x.lower() for x in cities]

# Check if the location exists. using zomato api.if found then save it, else utter not found.
class ActionValidateLocation(Action):
	def name(self):
		return 'action_check_location'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		city = str(loc)
		dispatcher.utter_message("city is "+ city)

		if city.lower() in cities_list:
			dispatcher.utter_message('found location')
			return [SlotSet('location_match',"one")]
		else:
			dispatcher.utter_message('not found location')
			zomato = zomatopy.initialize_app(zomato_config)

			try:
				results = zomato.get_city_ID(city)
				dispatcher.utter_message(results)
				return [SlotSet('location_match',"one")]
			except:
				return [SlotSet('location_match',"zero")]


# Send email the list of 10 restaurants
class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		email = tracker.get_slot('email')
		

		import smtplib 
		s = smtplib.SMTP('smtp.gmail.com', 587) 
		s.starttls() 
		s.login("foodie.recommendations@gmail.com", "Upgrad@2019")
		message = "The details of all the restaurants you inquried \n \n"
		global result_of_last_query
		message = message + result_of_last_query
		try:
			s.sendmail("foodie.recommendations@gmail.com", str(email), message)
			s.quit()
		except:
			dispatcher.utter_message(email)

		result_of_last_query = ""
		return [AllSlotsReset()]

from rasa_core_sdk.events import AllSlotsReset
from rasa_core_sdk.events import Restarted

class ActionRestarted(Action): 	
	def name(self):
		return 'action_restart_conv'
	def run(self, dispatcher, tracker, domain):
		return[Restarted()] 

class ActionSlotReset(Action): 
	def name(self): 
		return 'action_slot_reset' 
	def run(self, dispatcher, tracker, domain): 
		return[AllSlotsReset()]
