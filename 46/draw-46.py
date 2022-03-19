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

    .number {
        fill: #bfc2c7;
    }
"""


def hl(key):
    return {"key": key, "class": "held"}

def cm(key):
    return {"key": key, "class": "combo"}

def nm(key):
    return {"key": key, "class": "number"}

KEYMAP = [
    # BASE
    {
        "left": [
            [nm("1"), nm("2"), nm("3"), nm("4"), nm("5")],
            ["q", "w", "e", "r", "t"],
            ["a", "s", "d", "f", "g"],
            ["z", "x", "c", "v", "b"],
        ],
        "right": [
            [nm("6"), nm("7"), nm("8"), nm("9"), nm("0")],
            ["y", "u", "i", "o", "p"],
            ["j", "j", "k", "l", ";"],
            ["m", "n", ",", ".", "/"],
        ],
        "thumbs": {"left": ["del", "bkspc", "esc"], "right": ["enter", "space", "tab"],},
    },
    # COMBOS OUTER
    {
        "left": [
            [nm("1"), nm("2"), nm("3"), nm("4"), nm("5")],
            ["q", cm("{"), cm("{"), "r", "t"],
            ["a", cm("["), cm("["), "f", "g"],
            ["z", cm("`"), cm("`"), "v", "b"],
        ],
        "right": [
            [nm("6"), nm("7"), nm("8"), nm("9"), nm("0")],
            ["y", "u", cm("="), cm("="), "p"],
            ["j", "j", cm("'"), cm("'"), ";"],
            ["m", "n", cm("\\"), cm("\\"), "/"],
        ],
        "thumbs": {"left": ["del", "bkspc", "esc"], "right": ["enter", "space", "tab"],},
        },
    # COMBOS INNER
    {
        "left": [
            [nm("1"), nm("2"), nm("3"), nm("4"), nm("5")],
            ["q", "w", cm("}"), cm("}"), "t"],
            ["a", "s", cm("]"), cm("]"), "g"],
            ["z", "x", cm("~"), cm("~"), "b"],
        ],
        "right": [
            [nm("6"), nm("7"), nm("8"), nm("9"), nm("0")],
            ["y", cm("-"), cm("-"), "o", "p"],
            ["j", "j", "k", "l", ";"],
            ["m", "n", ",", ".", "/"],
        ],
        "thumbs": {"left": ["del", "bkspc", "esc"], "right": ["enter", "space", "tab"],},
    },
    # FUNCTION
    {
        "left": [
            [nm("f1"), nm("f2"), nm("f3"), nm("f4"), nm("f5")],
            ["", "", "", "", nm("f11")],
            ["ctrl", "alt", "cmd", "shift", ""],
            ["", "", "", "", ""],
        ],
        "right": [
            [nm("f6"), nm("f7"), nm("f8"), nm("f9"), nm("f10")],
            [nm("f12"), "", "", "", ""],
            ["", "shift", "cmd", "alt", "ctrl"],
            ["", "", ",", ".", "/"],
        ],
        "thumbs": {"left": [hl("func"), "bkspc", "esc"], "right": ["enter", "space", hl("func")],},
    },
    # NAVIGATION
    {
        "left": [
            [nm(""), nm(""), nm(""), nm(""), nm("")],
            ["", "", "", "", ""],
            ["ctrl", "alt", "cmd", "shift", ""],
            ["", "", "", "", ""],
        ],
        "right": [
            [nm(""), nm("menu bar"), nm(""), nm(""), nm("")],
            ["redo", "paste", "copy", "cut", "undo"],
            ["caps lock", "left", "down", "up", "right"],
            ["ins", "home", "page down", "page up", "end"],
        ],
        "thumbs": {"left": ["del", hl("nav"), "esc"], "right": ["enter", "space", "tab"],},
    },
    # MEDIA
    {
        "left": [
            [nm("bt clear"), nm(""), nm(""), nm(""), nm("")],
            ["", "", "", "", ""],
            ["prev", "vol down", "vol up", "next", ""],
            ["bt0", "bt1", "bt2", "bt3", "bt4"],
        ],
        "right": [
            [nm(""), nm(""), nm(""), nm(""), nm("")],
            ["", "", "", "", ""],
            ["ctrl", "alt", "cmd", "shift", ""],
            ["", "", "", "", ""],
        ],
        "thumbs": {"left": ["stop", "play pause", "mute"], "right": ["enter", hl("media"), "tab"],},
    },
]


layers = 0
for layer in KEYMAP:
    layers += 1

padding = layers + 1


KEYSPACE_W = KEY_W + 2 * INNER_PAD_W
KEYSPACE_H = KEY_H + 2 * INNER_PAD_H
HAND_W = 5 * KEYSPACE_W
HAND_H = 5 * KEYSPACE_H
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
        x + 2 * KEYSPACE_W, y + 4 * KEYSPACE_H, layer["thumbs"]["left"],
    )
    print_row(
        x + HAND_W + OUTER_PAD_W, y + 4 * KEYSPACE_H, layer["thumbs"]["right"],
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

