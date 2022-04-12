let A1 = [0, 1]
let B1 = [1, 0]
let C1 = [0, 1]
let A2 = []
let B2 = []
let C2 = []
led.plot(A1[0], A1[1])
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if ((A1[0] == 0 || A1[0] == 1) && (A1[1] == 0 || A1[1] == 1)) {
        A2 = [A1[0], 4 - A1[1]]
        led.unplot(A1[0], A1[1])
        A1 = A2
        led.plot(A2[0], A2[1])
    } else if ((A1[0] == 0 || A1[0] == 1) && (A1[1] == 3 || A1[1] == 4)) {
        A2 = [4 - A1[0], 0 - A1[1]]
        led.unplot(A1[0], A1[1])
        A1 = A2
        led.plot(A2[0], A2[1])
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    A2 = [4 - A1[0], 0 - A1[1]]
    led.unplot(A1[0], A1[1])
    A1 = A2
    led.plot(A2[0], A2[1])
})
basic.forever(function stred() {
    led.plotBrightness(2, 2, 127)
})
