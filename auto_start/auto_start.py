import pickle
import os
import pynput
import time

first_right_click_location = ()
second_left_click_location = ()
third_left_click_location = ()
# feel free to add more clicks or flicks

def setup():
        global first_right_click_location
        global second_left_click_location
        try:
                import pynput
        except ImportError:
                try:
                        import os
                        os.system("pip3 install pynput")
                except Exception as e:
                        print(e)
        x = pynput.mouse.Controller()
        print()
        while True:
                i = input("Please move you MOUSE to the\nFIRST RIGHT CLICK LOCATION\n and press 'ENTER' key:")
                if i == "":
                        first_right_click_location = x.position
                        print(f"Your current mouse position is {first_right_click_location}")
                        break
        while True:
                i = input("'ENTER': to RETAKE or 'y' to CONTINUE: ")
                v = x.position
                print(v)
                if i == "":
                        continue
                elif i.lower() == "y":
                        first_right_click_location = v
                        break
        while True:
                i = input("Please move you MOUSE to the\nSECOND LEFT CLICK LOCATION\n'ENTER': to RETAKE or 'y' to CONTINUE: ")
                v = x.position
                print(v)
                if i == "":
                        continue
                elif i.lower() == "y":
                        second_left_click_location = v
                        break
        while True:
                i = input("Please move you MOUSE to the\nTHIRD LEFT CLICK LOCATION\n'ENTER': to RETAKE or 'y' to CONTINUE: ")
                v = x.position
                print(v)
                if i == "":
                        continue
                elif i.lower() == "y":
                        third_left_click_location = v
                        break
        dict = {0:first_right_click_location, 1:second_left_click_location, 2:third_left_click_location}
        with open("data.pickle", "wb") as f:
                pickle.dump(dict, f, pickle.HIGHEST_PROTOCOL)
                

# if you want to make the pickle file with the locations as an input one at a time.
def manual_location_input():
        first_right_click_location = input("Please input FIRST CLICK LOCATION: ")
        second_left_click_location = input("Please input SECOND CLICK LOCATION: ")
        third_left_click_location = input("Please input THIRD CLICK LOCATION: ")
        dict = {0:first_right_click_location, 1:second_left_click_location, 2:third_left_click_location}
        with open("data.pickle", "wb") as f:
                pickle.dump(dict, f, pickle.HIGHEST_PROTOCOL)
                

# if you want to make the pickle file with the locatons as a parameter
def make_pickle(one, two, three):
        dict = {0:one, 1:two, 2:three}
        with open("data.pickle", "wb") as f:
                pickle.dump(dict, f, pickle.HIGHEST_PROTOCOL)

# persistent mouse location display to find out location
def mouse_posish():
        x = pynput.mouse.Controller()
        print("Press 'CTRL + C' to STOP")
        time.sleep(1)
        try:
                while True:
                        time.sleep(0.1)
                        print(x.position)
        except KeyboardInterrupt:
                print("Keyboard Interrupted.")


def run(sleep_time=10):
        # wait for n amount of time
        #check if pickle file exists
        # if not, run setup()
        # if yes, load pickle file
        # go to mouse position
        # right click
        # left click on run as admin
        # left click on accepting adminn permissions popup
        if os.path.exists("data.pickle") == False:
                setup()
        else:
                with open("data.pickle", "rb") as f:
                        data = pickle.load(f)
                print(f"sleeping for {sleep_time} seconds")
                time.sleep(sleep_time)
                print(f"going to {data[0]}")
                x = pynput.mouse.Controller()
                y = pynput.mouse.Button
                x.position = (data[0])
                x.press(y.right)
                x.release(y.right)
                time.sleep(1)
                print(f"going to {data[1]}")
                x.position = (data[1])
                x.press(y.left)
                x.release(y.left)
                time.sleep(2)
                x.position = (data[2])
                x.press(y.left)
                x.release(y.left)
                print("File should be running now. ")
                exit()

if __name__ == "__main__":
        run()





