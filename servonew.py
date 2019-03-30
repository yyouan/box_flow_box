import sys
import time
import RPi.GPIO as GPIO



def turnangle(angle=4120,speed=2):
    GPIO.setmode(GPIO.BCM)

    # Define GPIO signals to use
    # Physical pins 11,12,13,15
    # GPIO17,GPIO18,GPIO21,GPIO22
    StepPins = [17,18,21,22]

    # Set all pins as output
    for pin in StepPins:
        print ("Setup pins")
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin, False)
    GPIO.setup(25,GPIO.OUT)
    GPIO.output(25,True)

    # Define advanced sequence
    # as shown in manufacturers datasheet
    Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]

    StepCount = len(Seq)
    StepDir = 1


    # Read wait time from command line
    if len(sys.argv)>1:
        WaitTime = float(speed)/float(1000)
    else:
        WaitTime = 10/float(1000)

    # Initialise variables
    StepCounter = 0
    will = 0

    haha = angle
    # Start main loop
    while (will<int(haha)):
        will += 1
        print (StepCounter)
        print (Seq[StepCounter])

        for pin in range(0, 4):
            xpin = StepPins[pin]
            if Seq[StepCounter][pin]!=0:
                print (" Enable GPIO " ,(xpin))
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)

        StepCounter += StepDir

        # If we reach the end of the sequence
        # start again
        if (StepCounter>=StepCount):
            StepCounter = 0
        if (StepCounter<0):
            StepCounter = StepCount+StepDir

        # Wait before moving on
        time.sleep(WaitTime)

    GPIO.output(25,False)

def turnonecircle():
    turnangle(4120,2)

def turnquartercircle():
    #input('1/4')
    turnangle(1030,2)

if __name__ == "__main__":
    turnonecircle()
    turnangle(2000,2)
    time.sleep(1)
    turnangle(2120,2)
