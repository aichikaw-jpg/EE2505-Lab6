# EE2505-Lab6
Team members
 - Jamie Ho (ID: 6556717550) 
 - Alan Ichikawa - Chang (ID: 1212825599)


## Lab 6 Question Answers

4.1. Suppose you just cloned a repository that included one python file, my_first_file.py, and you now want to add a second file to your repository named my_second_file.py which contains the following code and push it to Github.com.

Code - print(“Hello World”)
Complete the sequence of linux shell commands:
git clone git@github.com:my-name/my-imaginary-repo.git
##complete the sequence
cd my-imaginary-repo
touch my_second_file.py
nano my_second_file.py

Inside the python file, add the line:
print("Hello Wolrd)

Ctrl X; Y to save and exit 

Run in bash:
git add my_second_file.py
git commit -m "Added my_second_file.py with Hello World"
git push origin main 
(Note: create the file using the `touch` command)

4.2 Describe the workflow you adopted for this lab (i.e. did you develop on your VM and push/pull to get code to your RPi, did you edit files directly on your RPi, etc.). Are there ways you might be more efficient in the next lab (i.e. learning a text-based editor so you can edit natively on the RPi, understanding Git commands better, etc.)?

I developed the code directly on my RPi using nano. The program needed to use the physical inferface with the sensors connected to the RPi, and testing required running the script on the RPi hardware itself. After successfully running, I pulled the final code back to the VM using scp. 

To be more efficient in the next lab, using vim or micro to edit my code in the RPi would be better. Commiting and push/pull to Git would also be safer practice in case the Rpi or VM crashes. 

4.3 In the starter code, we added a 200 ms sleep. Suppose you needed to poll the ultrasonic ranger as fast as possible, so you removed the sleep function. Now, your code has just the function ultrasonicRead() inside a while loop. However, even though there are no other functions in the while loop, you notice there is a
constant delay between each reading. Dig through the python library to find out why there is a constant delay. What is the delay amount? In addition, what communication protocol does the Raspberry Pi use to communicate with the Atmega328P on the GrovePi when it tries to read the ultrasonic ranger output using the `grovepi` python library? 

The delay amount should be 10 microseconds. There is a constant delay because of the differences in sample rates based on whether the object is closer to the sensor or not. Because of this variation in timing, a constant delay is added. The communication protocol that the Raspberry Pi uses to communicate with the Atmega328P is the I2C(inter-integrated circuit) protocol. It is a type of communication protocol that is common in short-distance communication. 

4.4 When you rotate the Grove Rotary Angle Sensor, its analog output voltage changes between 0 V and 5 V and the GrovePi library reports integer values between 0 and 1023. Explain how this conversion works and why the Raspberry Pi cannot do it directly.

The conversion is obtained through the equation: Vin/5V * 1023. 1023 is obtained because of 2^10. The reason why the Raspberry PI cannot do this directly is because it does not have an analog to digital converter like the atmega. 

4.5 Your LCD RGB Backlight screen is not displaying any text even though your code executes without errors. Describe how you would debug the issue. Include at least two terminal commands.

First, I would check that I2C is enabled. The command for this is ls /dev/i2c*. Second, I would check if the LCD is properly connected by doing i2cdetect -y 1 to scan the devices. If it is connected it should show up. 
