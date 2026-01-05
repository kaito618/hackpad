import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, SSD1306

keyboard = KMKKeyboard()

keyboard.pins = (
    board.A0,
    board.A1,
    board.A2,
    board.A3,
    board.TX,
    board.RX,
    board.SCK,
    board.MISO,
    board.MOSI,
)

keyboard.keymap = [
    [
        KC.N1, KC.N2, KC.N3,
        KC.N4, KC.N5, KC.N6,
        KC.N7, KC.N8, KC.N9,
    ]
]

display = Display(
    display_type=SSD1306,
    width=128,
    height=32,
    i2c=board.I2C(),
    device_address=0x3C,
)
keyboard.extensions.append(display)

if __name__ == '__main__':
    keyboard.go()

