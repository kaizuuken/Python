import random
import time

class Controller():
    def __init__(self,tv_status="off",tv_sound=0,channel_list=["Trt"],channel="Trt"):
        self.tv_status=tv_status
        self.tv_sound=tv_sound
        self.channel_list=channel_list
        self.channel=channel
    def tv_on(self):
        if self.tv_status=="on":
            print("TV is already on...")
        else:
            print("TV is Opening...")
            self.tv_status = "on"
    def tv_off(self):
        if self.tv_status == "off":
            print("Tv Is Already off...")
        else:
            print("TV is turning off")
            self.tv_status="off"
    def volume_adjustment(self):
        while True:
            answer=input("Lower the sound '<'\n Increase the sound '>'\nExit 'Exit'\n:")
            if answer =="<":
                if self.tv_sound!=0:
                    self.tv_sound-=1
                    print("Vol:",self.tv_sound)
            elif answer ==">":
                if self.tv_sound !=32:
                    self.tv_sound+=1
                    print("Vol:",self.tv_sound)
            else:
                print("Vol Updated..",self.tv_sound)
                break
    def add_channel(self,channel_name):

        print("Adding Channel..")
        time.sleep(1)
        self.channel_list.append(channel_name)
        print("Channel added..")
    def random_channel(self):

        random1=random.randint(0,len(self.channel_list)-1)
        self.channel=self.channel_list[random1]
        print("Current Channel:",self.channel)

    def __len__(self):
        return (len(self.channel_list))
    def __str__(self):
        return "TV Status: {}\nChannel List: {}\nCurrent Channel {}:".format(self.tv_status,self.channel_list,self.channel)


controller=Controller()

print("""

1. TV On

2.TV Off

3. TV Sound Adjustment

4.Add Channel

5.Learn The Number Off chnannels

6.Random Channel

7.Tv Information

8.Press 'q' to exit

""")

while True:
    operation=input("Choose The operation:")
    if operation =="q":
        print("The Program is terming..")
        break
    elif operation=="1":
        controller.tv_on()
    elif operation=="2":
        controller.tv_off()
    elif operation=="3":
        controller.volume_adjustment()
    elif operation=="4":

        channel_Names=input("enter channel names separated by ','")

        channel_list=channel_Names.split(",")

        for will_be_added in channel_list:
            controller.add_channel(will_be_added)
    elif operation=="5":
        print("Number Of Channel",len(controller))
    elif operation=="6":
        controller.random_channel()
    elif operation=="7":
        print(controller)
    else:
        print("Invalid Transaction...")