import getDarkskyKey
import getForecast
import getCurrent
import time


# Getting the Darksky Key
darkskyKey = getDarkskyKey.loadDarkskyKey()

## get the forecast for the day
getForecast.getForecastCork(darkskyKey)

# Loop to keep the program running
while True:
    # getting the weather where the function saves it in the DB
    getCurrent.getCurrentWeatherCork(darkskyKey)

    # Sleeping until the next time it's needed
    time.sleep(3600)
