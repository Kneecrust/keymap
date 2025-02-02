from draw_func import hl, cm, ch, ph, hm

KEYMAP = [
    # BASE
    {
        "left": [
            [ph(""), "q", "w", "f", "p", "b", ph("")],
            ["shift", "a", "r", "s", hm("t"), "g", ph("")],
            [ph(""), "z", "x", "c", "d", "v", ph("")],
        ],
        "right": [
            [ph(""), "j", "l", "u", "y", ";", ph("")],
            [ph(""), "m", hm("n"), "e", "i", "o", "shift"],
            [ph(""), "k", "h", ",", ".", "/", ph("")],
        ],
        # "thumbs": {"left": ["space", "enter"], "right": ["esc", "bkspc"],},
        "thumbs": {
            "left": [
                ["space"],
                [ph(""), "enter"],
            ],
            "right": [
                [ph(""), "bkspc"],
                ["esc"],
            ],
        },
    },

    # BASE SHIFTED
    {
        "left": [
            [ph(""), "Q", "W", "F", "P", "B", ph("")],
            ["shift", "A", "R", "S", hm("T"), "G", ph("")],
            [ph(""), "Z", "X", "C", "D", "V", ph("")],
        ],
        "right": [
            [ph(""), "J", "L", "U", "Y", ":", ph("")],
            [ph(""), "M", hm("N"), "E", "I", "O", "shift"],
            [ph(""), "K", "H", "&lt;", "&gt;", "?", ph("")],
        ],
        # "thumbs": {"left": ["space", "enter"], "right": ["esc", "bkspc"],},
        "thumbs": {
            "left": [
                ["space"],
                [ph(""), "enter"],
            ],
            "right": [
                [ph(""), "bkspc"],
                ["esc"],
            ],
        },
    },

    # ALL LAYERS & MODS

    {
        "left": [
            [ph(""), "", "", "", "", "", ph("")],
            [hl("nav"), "", hl("ctrl"), hl("alt"), hl("win"), "", ph("")],
            [ph(""), "", "", "", "", "", ph("")],
        ],
        "right": [
            [ph(""), "", "", "", "", "", ph("")],
            [ph(""), "", hl("win"), hl("alt"), hl("ctrl"), "", hl("func")],
            [ph(""), "", "", "", "", "", ph("")],
        ],
        # "thumbs": {"left": [hl("num"), hl("sym")], "right": ["esc", "bkspc"],},
        "thumbs": {
            "left": [
                [hl("num")],
                [ph(""), hl("sym")],
            ],
            "right": [
                [ph(""), "bkspc"],
                ["esc"],
            ],
        },
    },

    # COMBOS OUTER
    {
        "left": [
            [ph(""), "q", cm("{"), cm("{"), "p", "b", ph("")],
            ["shift", "a", cm("["), cm("["), hm("t"), "g", ph("")],
            [ph(""), "z", cm("("), cm("("), "d", "v", ph("")],
        ],
        "right": [
            [ph(""), "j", "l", cm("="), cm("="), ";", ph("")],
            [ph(""), "m", hm("n"), cm("'"), cm("'"), "o", "shift"],
            [ph(""), "k", "h", cm("&quot;"), cm("&quot;"), "/", ph("")],
        ],
        # "thumbs": {"left": ["space", "enter"], "right": ["esc", "bkspc"],},
        "thumbs": {
            "left": [
                ["space"],
                [ph(""), "enter"],
            ],
            "right": [
                [ph(""), "bkspc"],
                ["esc"],
            ],
        },
    },

    # COMBOS INNER
    {
        "left": [
            [ph(""), "q", "w", cm("}"), cm("}"), "b", ph("")],
            ["shift", "a", "r", cm("]"), cm("]"), "g", ph("")],
            [ph(""), "z", "x", cm(")"), cm(")"), "v", ph("")],
        ],
        "right": [
            [ph(""), "j", cm("-"), cm("-"), "y", ";", ph("")],
            [ph(""), "m", cm("_"), cm("_"), "i", "o", "shift"],
            [ph(""), "k", cm("\\"), cm("\\"), ".", "/", ph("")],
        ],
        # "thumbs": {"left": ["space", "enter"], "right": ["esc", "bkspc"],},
        "thumbs": {
            "left": [
                ["space"],
                [ph(""), "enter"],
            ],
            "right": [
                [ph(""), "bkspc"],
                ["esc"],
            ],
        },
    },

    # NUMBER
    {
        "left": [
            [ph(""), "", "", "", "", "", ph("")],
            ["shift", "", "ctrl", "alt", hm("win"), "", ph("")],
            [ph(""), "", "", "", "", "", ph("")],
        ],
        "right": [
            [ph(""), "*", "7", "8", "9", "+", ph("")],
            [ph(""), "-", hm("0"), "1", "2", "3", "="],
            [ph(""), "/", "4", "5", "6", ".", ph("")],
        ],
        # "thumbs": {"left": [hl("num"), "enter"], "right": ["esc", "bkspc"],},
        "thumbs": {
            "left": [
                [hl("space")],
                [ph(""), "enter"],
            ],
            "right": [
                [ph(""), "bkspc"],
                ["esc"],
            ],
        },
    },

    # SYMBOL
    {
        "left": [
            [ph(""), "", "", "", "", "", ph("")],
            ["shift", "", "ctrl", "alt", hm("win"), "", ph("")],
            [ph(""), "", "", "", "", "", ph("")],
        ],
        "right": [
            [ph(""), "|", "&amp;", "*", "(", "~", ph("")],
            [ph(""), "_", hm(")"), "!", "@", "#", "="],
            [ph(""), "/", "$", "%", "^", "`", ph("")],
        ],
        # "thumbs": {"left": ["space", hl("sym")], "right": ["esc", "bkspc"],},
        "thumbs": {
            "left": [
                ["space"],
                [ph(""), hl("sym")],
            ],
            "right": [
                [ph(""), "bkspc"],
                ["esc"],
            ],
        },
    },

    # FUNCTION
    {
        "left": [
            [ph(""), "F8", "F7", "F6", "F5", "", ph("")],
            ["prtscr", "F3", "F2", "F1", hm("F4"), "", ph("")],
            [ph(""), "F12", "F11", "F10", "F9", "", ph("")],
        ],
        "right": [
            [ph(""), "", "", "", "", "", ph("")],
            [ph(""), "", hm("win"), "alt", "ctrl", "", hl("func")],
            [ph(""), "", "", "", "", "", ph("")],
        ],
        # "thumbs": {"left": ["space", "enter"], "right": ["esc", "bkspc"],},
        "thumbs": {
            "left": [
                ["space"],
                [ph(""), "enter"],
            ],
            "right": [
                [ph(""), "bkspc"],
                ["esc"],
            ],
        },
    },

    # NAVIGATION
    {
        "left": [
            [ph(""), "", "", "", "", "", ph("")],
            [hl("nav"), "", "ctrl", "alt", hm("win"), "", ph("")],
            [ph(""), "", "", "", "", "", ph("")],
        ],
        "right": [
            [ph(""), "", "page down", "up", "page up", "", ph("")],
            [ph(""), "caps", hm("left"), "down", "right", "", "shift"],
            [ph(""), "tab", "home", "end", "ins", "", ph("")],
        ],
        # "thumbs": {"left": ["space", "enter"], "right": ["esc", "bkspc"],},
        "thumbs": {
            "left": [
                ["space"],
                [ph(""), "enter"],
            ],
            "right": [
                [ph(""), "bkspc"],
                ["esc"],
            ],
        },
    },
]

# python3 draw.py keys_36.keymap_36 > keys_36/keymap-36.svg
