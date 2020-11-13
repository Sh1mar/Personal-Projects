
#api.openweathermap.org/data/2.5/forecast?q ={city name},{country code}
import tkinter as tk
from tkinter import font
import requests
import tkinter.messagebox
root= tk.Tk()

HEIGHT =500
WIDTH =600

# Command (Functions)

def format_response(weather):
    try:
        name =(weather['name'])
        desc =(weather['weather'][0]['description'])
        temp =(weather['main']['temp'])

        final_str = 'City = %s \n Conditions = %s \n Temparature(.C)= %s' %(name,desc,temp)
    except:
        tkinter.messagebox.showinfo(root,'There was a problem retrieving data')
    return final_str
def get_weather(city):
    weather_key =''#Weather API key
    url ='https://api.openweathermap.org/data/2.5/weather'
    params ={'APPID' :weather_key, 'q':city,'units':'metric'}
    response =requests.get(url,params =params)
    weather =response.json()

    label['text'] =format_response(weather)

#Design of GUI
    
canvas =tk.Canvas(root,height =HEIGHT,width =WIDTH)
canvas.pack()

background = tk.PhotoImage(file ='landscape.png')
background_label =tk.Label(root,image =background)
background_label.place(relwidth =1,relheight= 1)

frame =tk.Frame(root,bg='cyan',bd =5)
frame.place(relx =0.5,rely =0.1,relwidth =0.75,relheight =0.1,anchor ='n')

button1 =tk.Button(frame,text ='Get Weather',bg ='red',fg ='black',command =lambda: get_weather(entry.get()))
button1.place(relx=0.7,relwidth =0.3,relheight =1)

entry =tk.Entry(frame,font =('Courier',18))
entry.place(relwidth =0.65,relheight =1) 

lower_frame=tk.Frame(root,bg  ='cyan',bd= 10)
lower_frame.place(relx =0.5,rely =0.25,relwidth =0.75,relheight =0.6,anchor ='n')

label =tk.Label(lower_frame,font =('Courier',18),anchor ='n',justify ='left',bd =4)
label.place(relwidth =1,relheigh=1)

creator_frame =tk.Frame(root, bg ='cyan',bd =5)
creator_frame.place(relx =0.01,rely =0.9,relheight =0.095,relwidth =0.2)

label1=tk.Label(creator_frame,text ='Done by Shimar')
label1.place(relwidth =1,relheigh=1,)

root.mainloop()
