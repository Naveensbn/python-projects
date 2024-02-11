from tkinter import *
import requests
root=Tk()
root.title('geo information')
root.geometry('600x600')
cityinput=StringVar()
Label(root,text="CITYNAME").grid(row=0,column=0)
Entry(root,textvariable=cityinput).grid(row=0,column=1)
def fetchdata():
    api_address = ('http://api.openweathermap.org/data/2.5/weather?'
                   'appid=3b38f7256941d04dc249f965f535ca29&q=')
    city = cityinput.get()
    url = api_address + city
    json_data = requests.get(url).json()
    lonv.set(json_data['coord']['lon'])
    latv.set(json_data['coord'].get('lat'))
    format_add = json_data['weather'][0]['main']
    format_add1 = json_data['weather'][0]['description']
    weth.set(format_add+"and "+format_add1)



Button(root,text="submit",command=fetchdata).grid(row=1,column=1)
latv=StringVar()
lonv=StringVar()
weth=StringVar()
Label(root,text="LATVAL").grid(row=2,column=0)
Entry(root,textvariable=latv).grid(row=2,column=1)
Label(root,text="LONVAL").grid(row=3,column=0)
Entry(root,textvariable=lonv).grid(row=3,column=1)
Label(root,text="WEATHERSTAUS").grid(row=4,column=0)
Entry(root,textvariable=weth).grid(row=4,column=1)

root.mainloop()
