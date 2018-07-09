from tkinter import *
from tkinter import ttk
import time
import datetime
import getCurrent
import getDarkskyKey


# Get darksky Key
darkskyKey = getDarkskyKey.loadDarkskyKey()

# Create the rkinger root
root = Tk()

# set the Tkinter title
root.title("Weather Cork")

# Create the label textvariable string variables
nowTime = StringVar()
nowUpdate = StringVar()
nowTemp = StringVar()
nowPrecip = StringVar()
nowHum = StringVar()
nowWS = StringVar ()

# get the current weather
currentWeather = getCurrent.getCurrentWeatherCork(darkskyKey)

def updateWeather():
    currentWeather = getCurrent.getCurrentWeatherCork(darkskyKey)
    localTime = currentWeather['time']
    nowUpdate.set("Current Weather Cork - Last updated at " + str(time.strftime("%H:%M", localTime)))
    nowTemp.set(str(currentWeather['temp']) + " C in Cork")
    nowPrecip.set(str(currentWeather['precipProb']) + "% chance of rain.")
    nowHum.set(str(currentWeather['hum']) + " humidity.")
    nowWS.set(str(str(currentWeather['windSpeed']) + " mp/h windspeed"))
    root.after(3600000, updateWeather)

def updateClock():
    nowTime.set(time.strftime("%H:%M", time.localtime(time.time())))
    root.after(1000, updateClock)

# set the current weather for the labels
updateClock()
updateWeather()

# Create the tkinter frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
# Set the frame labels for the weather
ttk.Label(mainframe, textvariable=nowTime).grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, textvariable=nowUpdate).grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainframe, textvariable=nowTemp).grid(column=2, row=3, sticky=(W, E))
ttk.Label(mainframe, textvariable=nowPrecip).grid(column=2, row=4, sticky=(W, E))
ttk.Label(mainframe, textvariable=nowHum).grid(column=2, row=5, sticky=(W, E))
ttk.Label(mainframe, textvariable=nowWS).grid(column=2, row=6, sticky=(W, E))
ttk.Button(mainframe, text="Update", command=updateWeather).grid(column=2, row=7, sticky=(W, E))
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# run the frame loop
root.mainloop()
