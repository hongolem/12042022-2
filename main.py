A1 = [0, 1]
B1 = [1, 0]
C1 = [0, 1]
A2 = []
B2 = []
C2 = []

led.plot(A1[0], A1[1])


def on_button_pressed_a():
    global A1, A2
    if (A1[0] == 0 or A1[0] == 1) and (A1[1] == 0 or A1[1] == 1):
        posun_v1()
    elif (A1[0] == 0 or A1[0] == 1) and (A1[1] == 3 or A1[1] == 4):
        posun_v2()
    elif (A1[0] == 3 or A1[0] == 4) and (A1[1] == 3 or A1[1] == 4):
        posun_v1()
    elif (A1[0] == 3 or A1[0] == 4) and (A1[1] == 0 or A1[1] == 1):
        posun_v2()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global A1, A2
    if (A1[0] == 0 or A1[0] == 1) and (A1[1] == 0 or A1[1] == 1):
        posun_v2()
    elif (A1[0] == 0 or A1[0] == 1) and (A1[1] == 3 or A1[1] == 4):
        posun_v1()
    elif (A1[0] == 3 or A1[0] == 4) and (A1[1] == 3 or A1[1] == 4):
        posun_v2()
    elif (A1[0] == 3 or A1[0] == 4) and (A1[1] == 0 or A1[1] == 1):
        posun_v1()
input.on_button_pressed(Button.B, on_button_pressed_b)

def stred():
    led.plot_brightness(2, 2, 127)
basic.forever(stred)

def posun_v1():
    global A1, A2
    A2 = [A1[0], 4 - A1[1]]
    led.unplot(A1[0], A1[1])
    A1 = A2
    led.plot(A2[0], A2[1])

def posun_v2():
    global A1, A2
    A2 = [4 - A1[0], A1[1]]
    led.unplot(A1[0], A1[1])
    A1 = A2
    led.plot(A2[0], A2[1])