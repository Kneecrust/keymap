# Here you declare all the classes for keys:

# This makes the key red for hold 
def hl(key):
    return {"key": key, "class": "hold"}
# This makes the key blue for combo
def cm(key):
    return {"key": key, "class": "combo"}
# This makes the key red for a combo hold
def ch(key):
    return {"key": key, "class": "combo_hold"}
# This makes the key grey (for static number rows)
def nm(key):
    return {"key": key, "class": "number"}
# This makes it so you can add 'extra' keys to better mimick your layout.
# It has the opacity set to 0% so you won't even see the key is there.
def ph(key):
    return {"key": key, "class": "invisible"}
# This makes the key grey for home key. 
# (I just used the two index finger home keys)
def hm(key):
    return {"key": key, "class": "home"}