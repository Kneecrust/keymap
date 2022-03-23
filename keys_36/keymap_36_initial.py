from draw_func import hl, cm, ch, ph

KEYMAP = [
    # BASE
    {
        "left": [
            [ph(""), "q", "w", "e", "r", "t", ph("")],
            ["shift", "a", "s", "d", "f", "g", ph("")],
            [ph(""), "z", "x", "c", "v", "b", ph("")],
        ],
        "right": [
            [ph(""),"y", "u", "i", "o", "p", ph("")],
            [ph(""),"j", "j", "k", "l", ";", "shift"],
            [ph(""),"m", "n", ",", ".", "/", ph("")],
        ],
        "thumbs": {"left": ["space", "esc"], "right": ["enter", "bkspc"],},
    },
    # HOME-ROW MODS
    {
        "left": [
            [ph(""), "q", "w", "e", "r", "t", ph("")],
            ["shift", hl("ctrl"), hl("alt"), hl("cmd"), hl("shift"), "g", ph("")],
            [ph(""), "z", "x", "c", "v", "b", ph("")],
        ],
        "right": [
            [ph(""),"y", "u", "i", "o", "p", ph("")],
            [ph(""),"j", hl("shift"), hl("cmd"), hl("alt"), hl("ctrl"),"shift"],
            [ph(""),"m", "n", ",", ".", "/", ph("")],
        ],
        "thumbs": {"left": ["space", "esc"], "right": ["enter", "bkspc",],},
    },
    # COMBOS OUTER
    {
        "left": [
            [ph(""), "q", cm("{"), cm("{"), "r", "t", ph("")],
            ["shift", "a", cm("["), cm("["), "f", "g", ph("")],
            [ph(""), "z", cm("`"), cm("`"), "v", "b", ph("")],
        ],
        "right": [
            [ph(""),"y", "u", cm("="), cm("="), "p", ph("")],
            [ph(""),"j", "j", cm("'"), cm("'"), ";", "shift"],
            [ph(""),"m", "n", cm("\\"), cm("\\"), "/", ph("")],
        ],
        "thumbs": {"left": ["space", "esc"], "right": ["enter", "bkspc",],},
        },
    # COMBOS INNER
    {
        "left": [
            [ph(""), "q", "w", cm("}"), cm("}"), "t", ph("")],
            ["shift", "a", "s", cm("]"), cm("]"), "g", ph("")],
            [ph(""), "z", "x", cm("~"), cm("~"), "b", ph("")],
        ],
        "right": [
            [ph(""),"y", cm("-"), cm("-"), "o", "p", ph("")],
            [ph(""),"j", "j", "k", "l", ";","shift"],
            [ph(""),"m", "n", ",", ".", "/", ph("")],
        ],
        "thumbs": {"left": ["space", "esc"], "right": ["enter", "bkspc",],},
    },
    # NUMBER
    {
        "left": [
            [ph(""), "[", "7", "8", "9", "]", ph("")],
            ["shift", "'", "4", "5", "6", "=", ph("")],
            [ph(""), "`", "1", "2", "3", "\\", ph("")],
        ],
        "right": [
            [ph(""),"", "", "", "", "",ph("")],
            [ph(""),"", "shift", "cmd", "alt", "ctrl","shift"],
            [ph(""),"", "", "", "", "",ph("")],
        ],
        "thumbs": {"left": ["space", "esc"], "right": ["enter", "bkspc",],},
    },
    # SYMBOL
    {
        "left": [
            [ph(""), "{", "&amp;", "*", "(", "}", ph("")],
            ["shift","\"","$", "%", "@", "+", ph("")],
            [ph(""), "~", "!", "@", "#", "|", ph("")],
        ],
        "right": [
            [ph(""),"", "", "", "", "", ph("")],
            [ph(""),"", "shift", "cmd", "alt", "ctrl", "shift"],
            [ph(""),"", "", "", "", "",ph("")],
        ],
        "thumbs": {"left": ["space", "esc"], "right": ["enter", "bkspc",],},
    },
    # FUNCTION
    {
        "left": [
            [ph(""), "F12", "F7", "F8", "F9", "pscrn", ph("")],
            ["shift","F11", "F4", "F5", "F6", "slck", ph("")],
            [ph(""), "F10", "F1", "F2", "F3", "psbrk", ph("")],
        ],
        "right": [
            [ph(""),"", "", "", "", "",ph("")],
            [ph(""),"", "shift", "cmd", "alt", "ctrl","shift"],
            [ph(""),"", "", "", "", "",ph("")],
        ],
        "thumbs": {"left": ["space", "esc"], "right": ["enter", "bkspc",],},
    },
    # NAVIGATION
    {
        "left": [
            [ph(""), "", "", "", "", "", ph("")],
            ["shift","ctrl", "alt", "cmd", "shift", "", ph("")],
            [ph(""), "", "", "", "", "", ph("")],
        ],
        "right": [
            [ph(""),"", "", "", "", "",ph("")],
            [ph(""),"caps lock", "left", "down", "up", "right","shift"],
            [ph(""),"ins", "home", "page down", "page up", "end",ph("")],
        ],
        "thumbs": {"left": ["space", "esc"], "right": ["enter", "bkspc",],},
    },
    # MEDIA
    {
        "left": [
            [ph(""), "", "", "", "", "", ph("")],
            ["shift","ctrl", "alt", "cmd", "shift", "", ph("")],
            [ph(""), "", "", "", "", "", ph("")],
        ],
        "right": [
            [ph(""),"", "", "", "", "",ph("")],
            [ph(""),"", "prev", "vol down", "vol up", "next","shift"],
            [ph(""),"bt4", "bt3", "bt2", "bt1", "bt0",ph("")],
        ],
        "thumbs": {"left": ["space", "esc"], "right": ["enter", "bkspc",],},
    },
]

