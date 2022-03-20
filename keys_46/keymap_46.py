from draw_func import hl, cm, nm

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
    # HOME-ROW MODS
    {
        "left": [
            [nm("1"), nm("2"), nm("3"), nm("4"), nm("5")],
            ["q", "w", "e", "r", "t"],
            [hl("ctrl"), hl("alt"), hl("cmd"), hl("shift"), "g"],
            ["z", "x", "c", "v", "b"],
        ],
        "right": [
            [nm("6"), nm("7"), nm("8"), nm("9"), nm("0")],
            ["y", "u", "i", "o", "p"],
            ["j", hl("shift"), hl("cmd"), hl("alt"), hl("ctrl")],
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
            ["", "", "", "", ""],
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

