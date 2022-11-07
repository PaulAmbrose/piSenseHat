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
  pressure = str(round(sense.get_pressure(),0))
  humidity = str(round(sense.get_humidity(),0))    

while True:
    
  sleep(300)
  SensorRun()
  myfile = open('log.txt', 'a')
  myfile.write(temp + " " + pressure + " " + humidity)
  myfile.write('\n')
  myfile.close
  
  for event in sense.stick.get_events():

    if event.action == "pressed":
        SensorRun()
        
        if event.direction == "middle":
            sense.show_message("T " + temp + " P " + pressure + " H " + humidity)     
        else:
            pass

        sleep
        (5.0)
        sense.clear()
