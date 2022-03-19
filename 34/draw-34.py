KEY_W = 55
KEY_H = 45
KEY_RX = 6
KEY_RY = 6
INNER_PAD_W = 2
INNER_PAD_H = 2
OUTER_PAD_W = KEY_W / 2
OUTER_PAD_H = KEY_H / 2
LINE_SPACING = 18

STYLE = """
    svg {
        font-family: SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;
        font-size: 14px;
        font-kerning: normal;
        text-rendering: optimizeLegibility;
        fill: #24292e;
    }

    rect {
        fill: #f6f8fa;
    }

    .held {
        fill: #fdd;
    }

    .combo {
        fill: #B6F2F2;
    }
"""


def hl(key):
    return {"key": key, "class": "held"}

def cm(key):
    return {"key": key, "class": "combo"}

KEYMAP = [
    # BASE
    {
        "left": [
            ["q", "w", "e", "r", "t"],
            ["a", "s", "d", "f", "g"],
            ["z", "x", "c", "v", "b"],
        ],
        "right": [
            ["y", "u", "i", "o", "p"],
            ["j", "j", "k", "l", ";"],
            ["m", "n", ",", ".", "/"],
        ],
        "thumbs": {"left": ["bkspc", "esc"], "right": ["enter", "space"],},
    },
    # COMBOS OUTER
    {
        "left": [
            ["q", cm("{"), cm("{"), "r", "t"],
            ["a", cm("["), cm("["), "f", "g"],
            ["z", cm("`"), cm("`"), "v", "b"],
        ],
        "right": [
            ["y", "u", cm("="), cm("="), "p"],
            ["j", "j", cm("'"), cm("'"), ";"],
            ["m", "n", cm("\\"), cm("\\"), "/"],
        ],
        "thumbs": {"left": [cm("del"), cm("del")], "right": [cm("tab"), cm("tab")],},
        },
    # COMBOS INNER
    {
        "left": [
            ["q", "w", cm("}"), cm("}"), "t"],
            ["a", "s", cm("]"), cm("]"), "g"],
            ["z", "x", cm("~"), cm("~"), "b"],
        ],
        "right": [
            ["y", cm("-"), cm("-"), "o", "p"],
            ["j", "j", "k", "l", ";"],
            ["m", "n", ",", ".", "/"],
        ],
        "thumbs": {"left": ["bkspc", "esc"], "right": ["enter", "space"],},
    },
    # NUMBER
    {
        "left": [
            ["[", "7", "8", "9", "]"],
            ["'", "4", "5", "6", "="],
            ["`", "1", "2", "3", "\\"],
        ],
        "right": [
            ["", "", "", "", ""],
            ["", "shift", "cmd", "alt", "ctrl"],
            ["", "", "", "", ""],
        ],
        "thumbs": {"left": ["bkspc", "esc"], "right": ["enter", hl("num")],},
    },
    # SYMBOL
    {
        "left": [
            ["{", "&amp;", "*", "(", "}"],
            ["\"","$", "%", "@", "+"],
            ["~", "!", "@", "#", "|"],
        ],
        "right": [
            ["", "", "", "", ""],
            ["", "shift", "cmd", "alt", "ctrl"],
            ["", "", "", "", ""],
        ],
        "thumbs": {"left": ["bkspc", "esc"], "right": [hl("sym"), "space"],},
    },
    # FUNCTION
    {
        "left": [
            ["F12", "F7", "F8", "F9", "pscrn"],
            ["F11", "F4", "F5", "F6", "slck"],
            ["F10", "F1", "F2", "F3", "psbrk"],
        ],
        "right": [
            ["", "", "", "", ""],
            ["", "shift", "cmd", "alt", "ctrl"],
            ["", "", "", "", ""],
        ],
        "thumbs": {"left": ["bkspc", "esc"], "right": [hl("func"), hl("func")],},
    },
    # NAVIGATION
    {
        "left": [
            ["", "", "", "", ""],
            ["ctrl", "alt", "cmd", "shift", ""],
            ["", "", "", "", ""],
        ],
        "right": [
            ["", "", "", "", ""],
            ["caps lock", "left", "down", "up", "right"],
            ["ins", "home", "page down", "page up", "end"],
        ],
        "thumbs": {"left": [hl("nav"), "esc"], "right": ["enter", "space"],},
    },
    # MEDIA
    {
        "left": [
            ["", "", "", "", ""],
            ["ctrl", "alt", "cmd", "shift", ""],
            ["", "", "", "", ""],
        ],
        "right": [
            ["", "", "", "", ""],
            ["", "prev", "vol down", "vol up", "next"],
            ["bt4", "bt3", "bt2", "bt1", "bt0"],
        ],
        "thumbs": {"left": ["bkspc", hl("media")], "right": ["mute", "play pause"],},
    },
]


layers = 0
for layer in KEYMAP:
    layers += 1

padding = layers + 1


KEYSPACE_W = KEY_W + 2 * INNER_PAD_W
KEYSPACE_H = KEY_H + 2 * INNER_PAD_H
HAND_W = 5 * KEYSPACE_W
HAND_H = 4 * KEYSPACE_H
LAYER_W = 2 * HAND_W + OUTER_PAD_W
LAYER_H = HAND_H
BOARD_W = LAYER_W + 2 * OUTER_PAD_W
BOARD_H = layers * LAYER_H + padding * OUTER_PAD_H


def print_key(x, y, key):
    key_class = ""
    if type(key) is dict:
        key_class = key["class"]
        key = key["key"]
    print(
        f'<rect rx="{KEY_RX}" ry="{KEY_RY}" x="{x + INNER_PAD_W}" y="{y + INNER_PAD_H}" width="{KEY_W}" height="{KEY_H}" class="{key_class}" />'
    )
    words = key.split()
    y += (KEYSPACE_H - (len(words) - 1) * LINE_SPACING) / 2
    for word in key.split():
        print(
            f'<text text-anchor="middle" dominant-baseline="middle" x="{x + KEYSPACE_W / 2}" y="{y}">{word}</text>'
        )
        y += LINE_SPACING


def print_row(x, y, row):
    for key in row:
        print_key(x, y, key)
        x += KEYSPACE_W


def print_block(x, y, block):
    for row in block:
        print_row(x, y, row)
        y += KEYSPACE_H


def print_layer(x, y, layer):
    print_block(x, y, layer["left"])
    print_block(
        x + HAND_W + OUTER_PAD_W, y, layer["right"],
    )
    print_row(
        x + 3 * KEYSPACE_W, y + 3 * KEYSPACE_H, layer["thumbs"]["left"],
    )
    print_row(
        x + HAND_W + OUTER_PAD_W, y + 3 * KEYSPACE_H, layer["thumbs"]["right"],
    )


def print_board(x, y, keymap):
    x += OUTER_PAD_W
    for layer in keymap:
        y += OUTER_PAD_H
        print_layer(x, y, layer)
        y += LAYER_H


print(
    f'<svg width="{BOARD_W}" height="{BOARD_H}" viewBox="0 0 {BOARD_W} {BOARD_H}" xmlns="http://www.w3.org/2000/svg">'
)
print(f"<style>{STYLE}</style>")
print_board(0, 0, KEYMAP)
print("</svg>")

