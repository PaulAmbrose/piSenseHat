#TEST123 An object Oriented program using sense HAT that
#  >>Creates a text file for the day
#  >>Reads the temperature, pressure and humidity every 5mins across the day and then
#    saves the file

from sense_hat import SenseHat
from time import sleep, strftime, time
import os
import matplotlib.pyplot as plt

sense = SenseHat()
sense.clear()

plt.ion()
x = []
y = []

path = os.getcwd()

def SensorRun():
    temp = str(round(sense.get_temperature(),0))
    return temp

def write_temp(temp):
    log = open("log.csv", "a")
    temp = SensorRun()
    log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))
    sleep(1)
    
def graph(temp):
    y.append(temp)
    x.append(time())
    plt.clf()
    plt.scatter(x,y)
    plt.plot(x,y)
    plt.draw()
    
while True:
    temp = SensorRun()
    write_temp(temp)
    graph(temp)
    plt.pause(1)
