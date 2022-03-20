from draw_func import hl, cm, ch

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
        "thumbs": {"left": ["del", "bkspc", "esc"], "right": ["enter", "space", "tab"],},
    },
    # HOME-ROW MODS
    {
        "left": [
            ["q", "w", "e", "r", "t"],
            [hl("ctrl"), hl("alt"), hl("cmd"), hl("shift"), "g"],
            ["z", "x", "c", "v", "b"],
        ],
        "right": [
            ["y", "u", "i", "o", "p"],
            ["j", hl("shift"), hl("cmd"), hl("alt"), hl("ctrl")],
            ["m", "n", ",", ".", "/"],
        ],
        "thumbs": {"left": ["del", "bkspc", "esc"], "right": ["enter", "space", "tab"],},
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
        "thumbs": {"left": ["del", "bkspc", "esc"], "right": ["enter", "space", "tab"],},
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
        "thumbs": {"left": ["del", "bkspc", "esc"], "right": ["enter", "space", "tab"],},
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
        "thumbs": {"left": [".", "0", "-"], "right": ["enter", hl("num"), "tab"],},
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
        "thumbs": {"left": [".", ")", "_"], "right": [hl("sym"), "space", "tab"],},
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
        "thumbs": {"left": ["", "", ""], "right": ["enter", "space", hl("func")],},
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
        "thumbs": {"left": ["del", hl("nav"), "esc"], "right": ["enter", "space", "tab"],},
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
        "thumbs": {"left": ["del", "bkspc", hl("media")], "right": ["mute", "play pause", "stop"],},
    },
]

