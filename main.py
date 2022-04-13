bod = [[0, 1], [1, 0]]
for i in bod:
    led.plot(i[0],i[1])

def on_button_pressed_a():
    for y in range(3):
        basic.pause(3000)
        basic.clear_screen()
        for u in bod:
            u[0] += 1
            u[1] += 1
            led.plot(u[0], u[1])
input.on_button_pressed(Button.A, on_button_pressed_a)