import tkinter as ui
import time

import math

window = ui.Tk()
window.geometry("420x420")



def update_clock():
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    second = int(time.strftime("%S"))

# Updating second hand per second
    second_x = second_hand_len *  math.sin(math.radians(second * 6)) + center_x
    second_y = -1 * second_hand_len * math.cos(math.radians(second *6)) + center_y
    canvas.coords(second_hand, center_x, center_y, second_x, second_y)

# Updating minutes hand per second
    minutes_x = minutes_hand_len * math.sin(math.radians(minutes * 6)) + center_x
    minutes_y = -1 * minutes_hand_len * math.cos(math.radians(minutes * 6)) + center_y
    canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)


# Updating hours hand per second
    hours_x = hours_hand_len * math.sin(math.radians(hours * 30)) + center_x
    hours_y = -1 * hours_hand_len * math.cos(math.radians(hours * 30)) + center_y
    canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)


    window.after(1000, update_clock)


canvas = ui.Canvas(window, width=700, height=800, bg="white")
canvas.pack(expand=True, fill='both')

# create background
bg = ui.PhotoImage(file="E:\\analog\\toexe\\Group 1.png")
canvas.create_image(200, 200, image=bg)


# create clock hands
center_x = 200
center_y = 200
second_hand_len = 170
minutes_hand_len = 130
hours_hand_len = 120

# drawing clock hands
# second hand
second_hand = canvas.create_line(200, 200,
                                 200 + second_hand_len, 200 + second_hand_len,
                                 width=1, fill='#0AAC8F')
# minutes hand
minutes_hand = canvas.create_line(200, 200,
                                  200 + minutes_hand_len, 200 + minutes_hand_len,
                                  width=2, fill='#0AAC8F')
# hours hand
hours_hand = canvas.create_line(200, 200,
                                200 + hours_hand_len, 200 + hours_hand_len,
                                width=4, fill='#0AAC8F')



update_clock()

window.mainloop()
