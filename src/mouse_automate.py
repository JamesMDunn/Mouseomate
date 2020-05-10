import numpy
import pyautogui
import time
class Mouseomate(object):
    pyautogui.PAUSE = 0.00 #useful
    pyautogui.FAILSAFE = True

    @staticmethod
    def image_to_clicks(image_array: numpy.array,offset:int) -> None:
        """
        Converts an image array to mouseclicks.
        :param image_array:
        A numpy array of bools, where False represents a click, and True represents no click.
        :param offset:
        An int which provides spacing between each pixel in image_array. Usefull to adjust for brush size used in whatever this will be outputting for.
        :return:
        """
        startpositionx,startpositiony = pyautogui.position()
        for row in image_array:
            xoffset = 0
            for value in row:
                if value == False:
                    pyautogui.moveTo(startpositionx, startpositiony, duration=0)
                    pyautogui.click(interval=0)
                    startpositionx += offset
                    xoffset += offset
                elif value == True:
                    startpositionx += offset
                    xoffset += offset
            startpositiony += offset
            startpositionx -= xoffset
            time.sleep(.07)



