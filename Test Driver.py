# pseudocode

# from TV import TV
from TV import TV

# object tv1tv1 = TV()
tv1 = TV()
# object tv2
tv2 = TV()

# print current channel and volume
print("\033[0;33;40m tv1's current channel is", tv1.getChannel(), "\033[0;33;40m and volume level is", tv1.getVolume())
print("\033[0;36;40m tv2's current channel is", tv2.getChannel(), "\033[0;36;40m and volume level is", tv2.getVolume())

# turnOn method
tv1.turnOn()
tv2.turnOn()

# set channel and volume
tv1.setChannel(int(input("\033[0;33;40m Enter channel (tv1): ")))
tv1.setVolume(int(input("\033[0;33;40m Enter volume (tv1): ")))
tv2.setChannel(int(input("\033[0;36;40m Enter channel(tv2): ")))
tv2.setVolume(int(input("\033[0;36;40m Enter volume(tv2): ")))

# print with set channel and volume
print("\033[0;33;40m tv1's channel is", tv1.getChannel(), "\033[0;33;40m and volume level is", tv1.getVolume())
print("\033[0;36;40m tv2's channel is", tv2.getChannel(), "\033[0;36;40m and volume level is", tv2.getVolume())

# channelUp method
tv1.channelUp()
# volumeUp method
tv2.volumeUp()

# print with channel up and volume up
print("\033[0;33;40m tv1's channels up and its channel is", tv1.getChannel(), "\033[0;33;40m and volume level is still", tv1.getVolume())
print("\033[0;36;40m tv2's channel is still", tv2.getChannel(), "\033[0;36;40m and volumes up and is now", tv2.getVolume())

# turn off TV
tv1.turnOff()
tv2.turnOff()

print("\033[0;33;40m THE TV1 IS NOW TURNED OFF")
print("\033[0;36;40m THE TV2 IS NOW TURNED OFF")