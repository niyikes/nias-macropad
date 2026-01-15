import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.modules.encoder import EncoderHandler

from kmk.extensions.display import Display, DisplayText
from kmk.extensions.display.ssd1306 import SSD1306

keyboard = KMKKeyboard()

# Macros
macros = Macros()
keyboard.modules.append(macros)

# Encoder
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

PINS = [
    board.D26,
    board.D27,
    board.D28,
    board.D29,
    board.D0,
    board.D1,
    board.D2
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.LCTL(KC.Z),
        KC.LCTL(KC.Y),
        KC.LCTL(KC.C),
        KC.LCTL(KC.V),
        KC.LALT(KC.TAB),
        KC.LCTL(KC.TAB),
        KC.PAUS
    ]
]

encoder_handler.pins = (
    (board.D3, board.D4),
)

encoder_handler.map = [
    (KC.VOLD, KC.VOLU)
]

display_text = DisplayText()
display_text.lines = [
    "NIA'S MACRO",
    "COOL ASS OLED",
]

display = Display(
    display=SSD1306(
        sda=board.SDA,
        scl=board.SCL,
    ),
    extensions=[display_text],
)

keyboard.extensions.append(display)

if __name__ == '__main__':
    keyboard.go()
