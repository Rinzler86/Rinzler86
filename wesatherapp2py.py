#import of needed modules 

import tkinter as tk
from tkinter import *
from security import safe_requests

#Create window for weather application
root = tk.Tk()
root.title("Weather Comparison!")
root.geometry("1000x700+450+20")
root.iconbitmap('C:\\Users\\Zeb Duffey\\Downloads\\sun_lightcloud_grain_cUB_icon.ico')

#API call for gathering weather information from outside source
api_key = "&limit=5&appid=0401ca0a9a077eef78f00fe6116b3023"
base_url = 'http://api.openweathermap.org/geo/1.0/direct?q='

temphidden = 0
temphidden1 = 0
print(temphidden)
print(temphidden1)

#preconcantenated URL for Weather calling reference
newapitest = "http://api.openweathermap.org/data/2.5/weather?appid=0401ca0a9a077eef78f00fe6116b3023&units=imperial&q="

#Text box and placement for entering local city information
cityname = Text(root, width=20, height=1, font=("Helvetica", 30), fg=("Orange"))
cityname.place(x=30,y=50,)

#Line for auto deletion once Enter Button is pressed
cityname1 = str(cityname.get("1.0", "end-1c"))

#base URL name to feed into function for global variable to reference
urlpluscity = base_url
storecity = ""

#Enter Button callback for local city textbox
def EnterButtonPress():
#retrieve enetered textbox information from user
	global storecity
	storecity = cityname.get("1.0", "end-1c")
	global urlpluscity
#concatenated url and users input
	urlpluscity = newapitest + storecity
#url gathered data conversion to json format 
	json_data = safe_requests.get(urlpluscity).json()
#debugging data prints
	print(urlpluscity)
	print(json_data)
#redundancy request 
	response = safe_requests.get(urlpluscity)
#converted to json
	data= response.json()
#accessing specific portions of retrieved json data
	main = data['main']
	formatjson = json_data['weather'][0]['description']
	formattemp = int(json_data['main']['temp'])
	formatwind = float(json_data['wind']['speed'])
#debugging data prints
	print(formattemp)
	print(formatjson)
	print(formatwind)
#configuring label text to reflect enetered local city
	entercitylabel.config(text=(f"Your Local Weather Report for {storecity}!"))
#configuring label text for weather description output
	weatheroutput.config(text=formatjson)
#automatic deletion of entered text	
	cityname.delete("1.0", "end")
#temp output GUI
	tempoutput.config(text=formattemp)
#wind output to GUI
	windoutput.config(text=formatwind)
	global temphidden
	temphidden = int(formattemp)
	print(temphidden)

#Label above city textbox
entercitylabel= Label(root, text="Enter Your Local City Here!", font=("Helvetica", 15), fg="Orange")
entercitylabel.place(x=70, y=20)

#Invisible until city is entered then the weather description output is displayed
weatheroutput = Label(root, text="", font=("Helvetica", 25), fg="Orange")
weatheroutput.place(x=250, y=240, anchor=CENTER)

#Label for weather description
weatheroutputlabel= Label(root, text="Weather Description:", font=("Helvetica", 25))
weatheroutputlabel.place(x=100, y= 170)

#Label for Temperature description
templabel = Label(root, text="Temperature:", font=("Helvetica", 25))
templabel.place(x=150, y=270)


#Invisble until city is entered then the temperature output is displayed 
tempoutput = Label(root, text="", font=("Helvetica", 25), fg="orange")
tempoutput.place(x=220, y=310)

#Label for Wind description
windlabel = Label(root, text="Windspeed(MPH):", font=("Helvetica", 25))
windlabel.place(x=120, y=370)

#Invisble until city is entered then the wind output is displayed 
windoutput = Label(root, text="", font=("Helvetica", 25), fg="orange")
windoutput.place(x=240, y=440, anchor=CENTER)


#Enter button and placement
enterbutton = Button(root, text=("Enter"), relief=RAISED, font=("Helvetica", 20),command=EnterButtonPress)
enterbutton.place(x=200, y= 100)

###################################NEW CITY CODE#######################################################

cityname1 = Text(root, width=20, height=1, font=("Helvetica", 30), fg=("Orange"))
cityname1.place(x=530,y=50,)

#Line for auto deletion once Enter Button is pressed
cityname2 = str(cityname1.get("1.0", "end-1c"))
storedcity2 = ""
#base URL name to feed into function for global variable to reference
urlpluscity1 = base_url

#Enter Button callback for local city textbox
def EnterButtonPress2():
#retrieve enetered textbox information from user
	global storedcity2
	storedcity2 = cityname1.get("1.0", "end-1c")
	print(storedcity2)
	global urlpluscity1
#concatenated url and users input
	urlpluscity1 = newapitest + storedcity2
	print(urlpluscity1)
#url gathered data conversion to json format 
	json_data1 = safe_requests.get(urlpluscity1).json()
#debugging data prints
	print(urlpluscity1)
	print(json_data1)
#redundancy request 
	response1 = safe_requests.get(urlpluscity1)
#converted to json
	data1 = response1.json()
#accessing specific portions of retrieved json data
	main1 = data1['main']
	formatjson1 = json_data1['weather'][0]['description']
	formattemp1 = int(json_data1['main']['temp'])
	formatwind1 = float(json_data1['wind']['speed'])
#debugging data prints
	print(formattemp1)
	print(formatjson1)
	print(formatwind1)
#configuring label text to reflect enetered local city
	entercitylabel1.config(text=(f"Your Weather Report for {storedcity2}!"))
#configuring label text for weather description output
	weatheroutput1.config(text=formatjson1)
#automatic deletion of entered text	
	cityname1.delete("1.0", "end")
#temp output GUI
	tempoutput1.config(text=formattemp1)
#wind output to GUI
	windoutput1.config(text=formatwind1)
	print(temphidden)
	global temphidden1
	temphidden1 = int(formattemp1)
	print(temphidden1)

	tempcompareCOLD = -temphidden - -temphidden1
	tempcompareHOT = -temphidden1 - -temphidden
	tempcompareEQUAL = temphidden == temphidden1

	if int(temphidden) < int(temphidden1):
		comparelabel.config(text=(f"Its {tempcompareCOLD} degrees colder in {storecity} than it is in {storedcity2}!"))
		print(f"Its {tempcompareCOLD} degrees colder in {storecity} than it is in {storedcity2}!")
	elif tempcompareEQUAL == True:
		comparelabel.config(f"Its the same temperature in {storecity} as it is in {storedcity2}")
		print(f"Its the same temprature in {storecity} as it is in {storedcity2}!")
	else:
	    comparelabel.config(text=(f"Its {tempcompareHOT} degrees hotter in {storecity} than it is in {storedcity2}!"))
        

#Label above city textbox
entercitylabel1= Label(root, text="Enter City for Comparison Here!", font=("Helvetica", 15), fg="Orange")
entercitylabel1.place(x=570, y=20)

#Invisible until city is entered then the weather description output is displayed
weatheroutput1 = Label(root, text="", font=("Helvetica", 25), fg="Orange")
weatheroutput1.place(x=750, y=240, anchor=CENTER)

#Label for weather description
weatheroutputlabel1 = Label(root, text="Weather Description:", font=("Helvetica", 25))
weatheroutputlabel1.place(x=600, y= 170)

#Label for Temperature description
templabel1 = Label(root, text="Temperature:", font=("Helvetica", 25))
templabel1.place(x=650, y=270)


#Invisble until city is entered then the temperature output is displayed 
tempoutput1 = Label(root, text="", font=("Helvetica", 25), fg="orange")
tempoutput1.place(x=720, y=310)

#Label for Wind description
windlabel1 = Label(root, text="Windspeed(MPH):", font=("Helvetica", 25))
windlabel1.place(x=620, y=370)

#Invisble until city is entered then the wind output is displayed 
windoutput1 = Label(root, text="", font=("Helvetica", 25), fg="orange")
windoutput1.place(x=740, y=440, anchor=CENTER)

#Enter button and placement
enterbutton1 = Button(root, text=("Enter"), relief=RAISED, font=("Helvetica", 20),command=EnterButtonPress2)
enterbutton1.place(x=700, y= 100)

comparelabel = Label(root, text=(""), font=("Helvetica", 25), fg="blue")
comparelabel.place(x=495, y= 550, anchor=CENTER)

root.mainloop()
