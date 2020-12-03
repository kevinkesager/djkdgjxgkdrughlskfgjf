input.onButtonPressed(Button.A, function on_button_pressed_a() {
    pins.digitalWritePin(DigitalPin.P2, 0)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    while (true) {
        basic.pause(100)
        pins.digitalWritePin(DigitalPin.P2, 0)
        basic.pause(100)
        pins.digitalWritePin(DigitalPin.P2, 1)
    }
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    pins.digitalWritePin(DigitalPin.P2, 1)
})
