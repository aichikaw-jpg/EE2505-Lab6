import sys
sys.path.append('~/Dexter/GrovePi/Software/Python')
import time
import grovepi
from grove_rgb_lcd import *

# Grove Ultrasonic Ranger connectd to digital port 4
ultrasonic_ranger = 4
# potentiometer connected to analog port A0 as input
potentiometer = 0
grovepi.pinMode(potentiometer,"INPUT")

# clear lcd screen  before starting main loop
setText("")

while True:
  try:
    # TODO:read distance value from Ultrasonic Ranger and print distance on LCD
    #distance in cm
      distanceVal = grovepi.ultrasonicRead(ultrasonic_ranger)

      #print the value
      print("Distance(CM):", distanceVal)

    # TODO: read threshold from potentiometer
    #reads the value from the potentiometer
      threshold = grovepi.analogRead(potentiometer)
    
    # TODO: format LCD text according to threshhold
    # add the threshold in string to the topline
      topLine = str(threshold) + " "

    # add spaces if the top line length is too small
      while(len(topLine) < 5):
        topLine += "  "


      #if the distance masured is less than the threshold obtained by the analog input
      if (distanceVal < threshold):
        #Add a line that says OBJ PRES
        topLine += "OBJ PRES"
      else:
        #Adds a bunch of spaces if the distance is greater
        topLine += "            "

      #make sure that it does not go past 16 characters
      topLine = topLine[:16]
      #add the distance to the bottom line
      bottomLine = str(distanceVal) + "cm"

      #set text fufnction for the LCD, and makes sure that it doesnt blink
      setText_norefresh(topLine + "\n" + bottomLine)

      #add a bit of delay just in case
      time.sleep(2)

    
  except IOError:
    print("Error")





    #pull from rpi: scp pi@10.134.239.211:grovepi_sensors.py ~/Desktop/
    #push to rpi: scp pi@10.134.239.211 /home/alan/Desktop/lab6/grovepi_sensors.py pi@10.134.239.211:~/


