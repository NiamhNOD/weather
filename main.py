import loadCurrent
import time

# Loop to keep the program running
while True:
    # Getting the Darksky Key
    darkskyKey = loadCurrent.loadDarkskyKey()

    # getting the weather where the function saves it in the DB
    loadCurrent.getCurrentWeatherCork(darkskyKey)

    # Sleeping until the next time it's needed
    time.sleep(3600)
