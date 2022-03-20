from sys import argv
from importlib import import_module

if len(argv) > 1:
    KEYMAP = import_module(argv[1]).KEYMAP
else:
    from keymap_34 import KEYMAP

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

    .combo_hold {
        fill: #fdd;
    }

    .combo {
        fill: #B6F2F2;
    }
    
    .number{
        fill: #bfc2c7
    }
"""


layers = 0

for layer in KEYMAP:
    layers += 1

padding = layers + 1


rows = 1

for layer in KEYMAP:
    for row in layer["left"]:
        rows += 1
    break

KEYSPACE_W = KEY_W + 2 * INNER_PAD_W
KEYSPACE_H = KEY_H + 2 * INNER_PAD_H
HAND_W = 5 * KEYSPACE_W
HAND_H = rows * KEYSPACE_H
LAYER_W = 2 * HAND_W + OUTER_PAD_W
LAYER_H = HAND_H
BOARD_W = LAYER_W + 2 * OUTER_PAD_W
BOARD_H = layers * LAYER_H + padding * OUTER_PAD_H


def print_key(x, y, key, combo_flag):
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

    if key_class == "combo" or key_class == "combo_hold":
        if combo_flag:
            print(
                f'<path fill="none" stroke="#eda65e" stroke-width="4" stroke-linecap="round" d="M{x+OUTER_PAD_W},{y-KEY_H+INNER_PAD_H*6} A{KEY_W},{KEY_W*1} 0,0,0 {x-OUTER_PAD_W},{y-KEY_H+INNER_PAD_H*6}" />'
            )


def print_row(x, y, row):
    for index,key in enumerate(row):
        combo_flag = False
        key_class = ""
        if type(key) is dict:
            key_class = key["class"]
        if key_class == "combo" or key_class == "combo_hold":
            if index > 0:
                prev = row[index-1]
                prev_class = ""
                if type(prev) is dict:
                    prev_class = prev["class"]
                if prev_class == "combo" or prev_class == "combo_hold":
                    combo_flag = True

        print_key(x, y, key, combo_flag)
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

    rows = 0
    for row in layer["left"]:
        rows += 1

    print_row(
        x + (5-len(layer["thumbs"]["left"])) * KEYSPACE_W, y + rows * KEYSPACE_H, layer["thumbs"]["left"],
    )
    print_row(
        x + HAND_W + OUTER_PAD_W, y + rows * KEYSPACE_H, layer["thumbs"]["right"],
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

