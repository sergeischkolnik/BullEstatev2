import threading
import time



def doit(arg):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        print ("working on" + str(arg))
        time.sleep(1)
    print("Stopping as you wish.")

t = threading.Thread(target=doit, args=(0,))

def main():

    for i in range(1,3):
        print("main:" + str(i))
        if(i==1):
            t = threading.Thread(target=doit, args=(i,))
            t.setDaemon(True)
            t.start()

        if(i==2):
            t.do_run = False

        time.sleep(5)

if __name__ == "__main__":
    main()