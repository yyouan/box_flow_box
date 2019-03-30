import RPi.GPIO as GPIO
import time



##everytime call , return 1 mean it is push down,return 0 mean didnt touch

def buttom():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2,GPIO.IN)
    inputValue = GPIO.input(2)
    if(inputValue==False):
        print("OPEN!")
        return True
    else:
        return False
    '''
    if (inputValue == False): ##because it is put down
        print("dont touch me.")
        while(inputValue==False):
            time.sleep(0.1)
            inputValue = GPIO.input(2)
    '''
if __name__ == "__main__":
    ##testbench
    while(True):
        if(buttom()==1):
            print("dont touch me")
            while(buttom()==1):
                time.sleep(0.1)


        
