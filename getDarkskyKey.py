import configparser

def loadDarkskyKey():
    # Open the config file to read in the Darksky key
    config = configparser.ConfigParser()
    config.read('config.ini')
    darkskyKey = config['darksky']['darkskyKey']
    return darkskyKey
