def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P2, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    while True:
        basic.pause(100)
        pins.digital_write_pin(DigitalPin.P2, 0)
        basic.pause(100)
        pins.digital_write_pin(DigitalPin.P2, 1)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    pins.digital_write_pin(DigitalPin.P2, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)
