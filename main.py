from tkinter import *
from tkinter import ttk
from datetime import date
import time
import datetime
import getCurrent
import getForecast
import getDarkskyKey


# Get darksky Key
darkskyKey = getDarkskyKey.loadDarkskyKey()

# Create the rkinger root
root = Tk()

# set the Tkinter title
root.title("Weather Cork")

# Create the label for current weather textvariable string variables
nowTime = StringVar()
nowUpdate = StringVar()
nowTemp = StringVar()
nowPrecip = StringVar()
nowHum = StringVar()
nowWS = StringVar ()

# Create the labels for the forecast text variable string variables
forecastTime = StringVar()
forecastUpdate = StringVar()
forecastSummary = StringVar()
forecastMaxTemp = StringVar()
forecastMinTemp = StringVar()
forecastPrecipProb = StringVar()
forecastPrecipIn = StringVar()
forecastSunrise = StringVar()
forecastSunset = StringVar()

# Set the times to check for updates
timeToCheck = int(time.time())
forecastToCheck = int(time.time())

# Create the tkinter frame and tabs
tabControl = ttk.Notebook(root)
tabCurrent = ttk.Frame(tabControl)
tabForecast = ttk.Frame(tabControl)

# Create the grid for the weather data with tkinter
def setGrid():
    # Set the frame labels for the current weather
    ttk.Label(tabCurrent, textvariable=nowTime).grid(column=1, row=1, sticky=(W, E))
    ttk.Label(tabCurrent, textvariable=nowUpdate).grid(column=1, row=2, sticky=(W, E))
    ttk.Label(tabCurrent, textvariable=nowTemp).grid(column=1, row=3, sticky=(W, E))
    ttk.Label(tabCurrent, textvariable=nowPrecip).grid(column=1, row=4, sticky=(W, E))
    ttk.Label(tabCurrent, textvariable=nowHum).grid(column=1, row=5, sticky=(W, E))
    ttk.Label(tabCurrent, textvariable=nowWS).grid(column=1, row=6, sticky=(W, E))
    ttk.Button(tabCurrent, text="Update", command= lambda: updateWeather()).grid(column=1, row=7, sticky=(W, E))
    for child in tabCurrent.winfo_children(): child.grid_configure(padx=5, pady=5)

    # Set the frame labels for the forecasted weather
    ttk.Label(tabForecast, textvariable=nowTime).grid(column=1, row=1, sticky=(W, E))
    ttk.Label(tabForecast, textvariable=forecastUpdate).grid(column=1, row=2, sticky=(W, E))
    ttk.Label(tabForecast, textvariable=forecastSummary).grid(column=1, row=3, sticky=(W, E))
    ttk.Label(tabForecast, textvariable=forecastMaxTemp).grid(column=1, row=4, sticky=(W, E))
    ttk.Label(tabForecast, textvariable=forecastMinTemp).grid(column=1, row=5, sticky=(W, E))
    ttk.Label(tabForecast, textvariable=forecastPrecipProb).grid(column=1, row=6, sticky=(W, E))
    ttk.Label(tabForecast, textvariable=forecastPrecipIn).grid(column=1, row=7, sticky=(W, E))
    ttk.Label(tabForecast, textvariable=forecastSunrise).grid(column=1, row=8, sticky=(W, E))
    ttk.Label(tabForecast, textvariable=forecastSunset).grid(column=1, row=9, sticky=(W, E))
    ttk.Button(tabForecast, text="Update", command= lambda: updateForecastWeather()).grid(column=1, row=10, sticky=(W, E))
    for child in tabCurrent.winfo_children(): child.grid_configure(padx=5, pady=5)



def updateWeather():
    # access the global variable that sets when updates come
    global timeToCheck
    timeToCheck = time.time()
    localTime = time.localtime()

    # access the function that gets the weather and stores it in a DB
    currentWeather = getCurrent.getCurrentWeatherCork(darkskyKey)
    # set the label variables to the correct details
    nowUpdate.set("Current Weather Cork - Last updated at " + str(time.strftime("%H:%M", localTime)))
    nowTemp.set(str(currentWeather['temp']) + " C in Cork")
    nowPrecip.set(str((100 * currentWeather['precipProb'])) + "% chance of rain.")
    nowHum.set(str(currentWeather['hum']) + " humidity.")
    nowWS.set(str(str(currentWeather['windSpeed']) + " mp/h windspeed"))
    # if it's not the first time being run it goes to check the auto-updates

    # goes to check the update
    updateWeatherCheck()

# Call to update the forecasted weather details
def updateForecastWeather():
    # access the global variable that sets when updates come
    global forecastTimeToCheck
    forecastTimeToCheck = time.time()
    localTime = time.localtime()

    # access the function that gets the weather and stores it in a DB
    forecastWeather = getForecast.getForecastCork(darkskyKey)
    forecastSummary.set(forecastWeather['summary'])

    # set the label variables to the correct details
    forecastUpdate.set("Forecast Weather Cork - Last updated at " + str(time.strftime("%H:%M", localTime)))
    forecastMaxTemp.set("Max temperature is "+ str(forecastWeather['tempHigh']) + "C for Cork")
    forecastMinTemp.set("Min temperature is "+ str(forecastWeather['tempLow']) + "C for Cork")
    forecastPrecipProb.set((str(100 *forecastWeather['precipProb'])) + "% chance of rain.")
    forecastPrecipIn.set(str(forecastWeather['precipInt']) + " level intensity of rain.")
    forecastSunrise.set("Sunrise is at: " + str(time.strftime("%H:%M", time.localtime(forecastWeather['sunrise']))))
    forecastSunset.set("Sunset is at: " + str(time.strftime("%H:%M", time.localtime(forecastWeather['sunset']))))

    # Goes to check the update
    updateForecastWeatherCheck()

# Keeps checking to see when the last update was then calls a new update when the time has come
def updateWeatherCheck():
        currentTime = int(time.time())
        global timeToCheck
        if (currentTime - timeToCheck) > 1800:
            updateWeather()
        else:
            root.after(5000, updateWeatherCheck)

# Keeps checking to see when the last update was then calls a new update when the time has come
def updateForecastWeatherCheck():
        currentTime = int(time.time())
        global forecastTimeToCheck
        if (currentTime - forecastTimeToCheck) > 14400:
            updateForecastWeather()
        else:
            root.after(5000, updateForecastWeatherCheck)

# The clock for the wdiget
def updateClock():
    nowTime.set(time.strftime("%H:%M", time.localtime(time.time())))
    root.after(1000, updateClock)

# set the current weather for the labels
updateClock()
updateWeather()
updateForecastWeather()
setGrid()

# adds the tabs
tabControl.add(tabCurrent, text='Current Weather')
tabControl.add(tabForecast, text='Forecasted Weather')
tabControl.pack(expand=1, fill="both")

root.mainloop()
