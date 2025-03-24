import eel
import json
import os

# LOAD and DEFINE variables, default values, universal methods
with open("config.json", "r") as f:
    defaults = json.load(f)

with open("lookup.json", "r") as f:
    lookup = json.load(f)

theme_ops = ["darkly", "superhero", "vapor", "cerculean", "yeti", "flatly"]

def adjust_color(color, factor):
    """Adjust color brightness by a factor.
    If the factor is greater than 1.0 the color will lighten, if less than 1.0 it will darken."""
    color = color.lstrip('#')
    r, g, b = int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)
    r = min(255, max(0, int(r * factor)))
    g = min(255, max(0, int(g * factor)))
    b = min(255, max(0, int(b * factor)))
    return f'#{r:02x}{g:02x}{b:02x}'

@eel.expose
def theme_selected(selected_theme):
    defaults["theme"] = selected_theme
    with open("config.json", "w") as f:
        json.dump(defaults, f, indent=4)
    update_top_bar()

def update_top_bar():
    new_color = lookup["themes"][defaults["theme"]]["top_bar"]
    eel.updateTopBar(new_color)

# Initialize Eel
eel.init('web')

# Start the Eel application
eel.start('index.html', size=(800, 600))