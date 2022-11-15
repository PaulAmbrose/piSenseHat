#An object Oriented program using sense HAT that
#  >>Creates a text file for the day
#  >>Reads the temperature, pressure and humidity every 5mins across the day and then saves the file
#  >>Allows the user to select the joy stick button to get a temperature readout in colour banding

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

def SensorRun():
    temp = str(round(sense.get_temperature(),0))  
    return temp

while True:

  temp = SensorRun()
  myfile = open('log.txt', 'a')
  myfile.write(temp)
  myfile.write('\n')
  myfile.close
  sleep(10)
  
  for event in sense.stick.get_events():

    if event.action == "pressed":
        temp = SensorRun()
        
        if event.direction == "middle":
            sense.show_message("T " + temp)     
        else:
            pass
        
        sense.clear()
        