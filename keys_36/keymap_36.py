from draw_func import hl, cm, ch, ph

KEYMAP = [
    # BASE
    {
        "left": [
            [ph(""), "q", "w", "e", "r", "t"],
            ["shift", "a", "s", "d", "f", "g"],
            [ph(""), "z", "x", "c", "v", "b"],
        ],
        "right": [
            ["y", "u", "i", "o", "p", ph("")],
            ["j", "j", "k", "l", ";", "shift"],
            ["m", "n", ",", ".", "/", ph("")],
        ],
        "thumbs": {"left": ["space", "esc"], "right": ["enter", "bkspc",],},
    },
    # HOME-ROW MODS
    {
        "left": [
            [ph(""), "q", "w", "e", "r", "t"],
            [hl("ctrl"), hl("alt"), hl("cmd"), hl("shift"), "g"],
            [ph(""), "z", "x", "c", "v", "b"],
        ],
        "right": [
            ["y", "u", "i", "o", "p", ph("")],
            ["j", hl("shift"), hl("cmd"), hl("alt"), hl("ctrl")],
            ["m", "n", ",", ".", "/", ph("")],
        ],
        "thumbs": {"left": ["space", "esc"], "right": ["enter", "bkspc",],},
    },
    # COMBOS OUTER
    {
        "left": [
            [ph(""), "q", cm("{"), cm("{"), "r", "t"],
            ["shift", "a", cm("["), cm("["), "f", "g"],
            [ph(""), "z", cm("`"), cm("`"), "v", "b"],
        ],
        "right": [
            ["y", "u", cm("="), cm("="), "p", ph("")],
            ["j", "j", cm("'"), cm("'"), ";", "shift"],
            ["m", "n", cm("\\"), cm("\\"), "/", ph("")],
        ],
        "thumbs": {"left": ["space", "esc"], "right": ["enter", "bkspc",],},
        },
    # COMBOS INNER
    {
        "left": [
            [ph(""), "q", "w", cm("}"), cm("}"), "t"],
            ["shift", "a", "s", cm("]"), cm("]"), "g"],
            [ph(""), "z", "x", cm("~"), cm("~"), "b"],
        ],
        "right": [
            ["y", cm("-"), cm("-"), "o", "p", ph("")],
            ["j", "j", "k", "l", ";","shift"],
            ["m", "n", ",", ".", "/", ph("")],
        ],
        "thumbs": {"left": ["space", "esc"], "right": ["enter", "bkspc",],},
    },
    # NUMBER
    {
        "left": [
            [ph(""), "[", "7", "8", "9", "]"],
            ["shift, ""'", "4", "5", "6", "="],
            [ph(""), "`", "1", "2", "3", "\\"],
        ],
        "right": [
            ["", "", "", "", "",ph("")],
            ["", "shift", "cmd", "alt", "ctrl","shift"],
            ["", "", "", "", "",ph("")],
        ],
        "thumbs": {"left": ["space", "esc"], "right": ["enter", "bkspc",],},
    },
    # SYMBOL
    {
        "left": [
            [ph(""), "{", "&amp;", "*", "(", "}"],
            ["shift","\"","$", "%", "@", "+"],
            [ph(""), "~", "!", "@", "#", "|"],
        ],
        "right": [
            ["", "", "", "", "", ph("")],
            ["", "shift", "cmd", "alt", "ctrl", "shift"],
            ["", "", "", "", "",ph("")],
        ],
        "thumbs": {"left": ["space", "esc"], "right": ["enter", "bkspc",],},
    },
    # FUNCTION
    {
        "left": [
            [ph(""), "F12", "F7", "F8", "F9", "pscrn"],
            ["shift","F11", "F4", "F5", "F6", "slck"],
            [ph(""), "F10", "F1", "F2", "F3", "psbrk"],
        ],
        "right": [
            ["", "", "", "", "",ph("")],
            ["", "shift", "cmd", "alt", "ctrl","shift"],
            ["", "", "", "", "",ph("")],
        ],
        "thumbs": {"left": ["space", "esc"], "right": ["enter", "bkspc",],},
    },
    # NAVIGATION
    {
        "left": [
            [ph(""), "", "", "", "", ""],
            ["shift","ctrl", "alt", "cmd", "shift", ""],
            [ph(""), "", "", "", "", ""],
        ],
        "right": [
            ["", "", "", "", "",ph("")],
            ["caps lock", "left", "down", "up", "right","shift"],
            ["ins", "home", "page down", "page up", "end",ph("")],
        ],
        "thumbs": {"left": ["space", "esc"], "right": ["enter", "bkspc",],},
    },
    # MEDIA
    {
        "left": [
            [ph(""), "", "", "", "", ""],
            ["shift","ctrl", "alt", "cmd", "shift", ""],
            [ph(""), "", "", "", "", ""],
        ],
        "right": [
            ["", "", "", "", "",ph("")],
            ["", "prev", "vol down", "vol up", "next","shift"],
            ["bt4", "bt3", "bt2", "bt1", "bt0",ph("")],
        ],
        "thumbs": {"left": ["space", "esc"], "right": ["enter", "bkspc",],},
    },
]

