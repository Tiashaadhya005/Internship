import threading
import time


class createdata(threading.Thread):
    def run(self):
        try:
            for i in range(10):
                print("hi")
                time.sleep(1)
        except Exception as err:
            print(err)

class createdatatwo(threading.Thread):
    def run(self):
        try:
            for i in range(10):
                print("hello")
                time.sleep(1)
        except Exception as err:
            print(err)


    