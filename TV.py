# pseudocode

# class for TV
class TV:

    def __init__(self):
    # channel int
        self.channel = 1
    # volumeLevel int
        self.volumeLevel = 1
    # on bool
        self.on = False

    # def turn on
    def turnOn(self):
        self.on = True

    # def turn off
    def turnOff(self):
        self.on = False

    # def getChannel
    def getChannel(self):
        return self.channel
    
    # def setChannel
    def setChannel(self, channel):
        if self.on and 1 <= channel <= 120:
            self.channel = channel

    # def getVolume
    def getVolume(self):
        return self.volumeLevel
    
    # def setVolume
    def setVolume(self, volumeLevel):
        if self.on and 1 <= volumeLevel <= 7:
            self.volumeLevel = volumeLevel
    
    # def channelUp
    # def channelDown
    # def volumeUp
    # def volumeDown