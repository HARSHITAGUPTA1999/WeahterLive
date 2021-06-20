

import tkinter as tk
import tkinter.font as font
import tkinter.messagebox
import requests
HEIGHT = 500
WIDTH = 500


root = tk.Tk()
def fun(entry):
    print("button clicked...!", entry)

def format_response(weather):
    try:

        name = weather['name']
        des = weather['weather'][0]['description']
        temp = weather['main']['temp']
        humid = weather['main']['humidity']

        final_str = 'City: %s\nConditions: %s\nTemperature(°C): %s\nHumidity: %s\n' % (name, des, temp, humid)
        return final_str
    except:
        print("Enter a valid city")


def weather_today(city):
    weather_key = '73280127bae987a047336f21307c94dc'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params={ 'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response(weather)


#api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}
#api.openweathermap.org/data/2.5/forecast?zip={zip code},{country code}&appid={your api key}
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
bag_image = tk.PhotoImage(file='weather3.png')
larger_image = bag_image.zoom(2, 2)
bag_label = tk.Label(root, image=larger_image)
bag_label.place(relx=0, rely=0, relwidth=1, relheight=1)
frame = tk.Frame(root, bg='#ffcce6', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.65, relheight=0.1, anchor='n')
myfont = font.Font(family='Calibri', size=12)
entry = tk.Entry(frame, font=myfont)
entry.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Weather Today", bg='white', command=lambda: weather_today(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.28, relheight=1)
#button.bind("<Button-1>", fun)
#lower frame
lower_frame = tk.Frame(root, bg='#ffcce6', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.65, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=myfont, anchor='nw', justify='left', bd=4)
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
