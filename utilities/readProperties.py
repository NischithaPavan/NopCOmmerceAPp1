import configparser

config=configparser.RawConfigParser() #Raw config is method and we created object

config.read(".\\Configurations\\config.ini")

class readConfig:

    @staticmethod
    def getApplicationURL(): #this is just class so no need to specify self
        url=config.get('common info', 'baseurl') # assign to variable called url
        return url

    @staticmethod
    def getUserEmail():  # this is just class so no need to specify self
        username = config.get('common info', 'username')  # assign to variable called url
        return username

    @staticmethod
    def getUserPassword():  # this is just class so no need to specify self
        password = config.get('common info', 'password')  # assign to variable called url
        return password















