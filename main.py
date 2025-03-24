import ttkbootstrap as ttk
import json

# LOAD and DEFINE variables, default values, universal methods
with open("config.json", "r") as f:
    defaults = json.load(f)

with open("lookup.json", "r") as f:
    lookup = json.load(f)

theme_ops = ["darkly", "superhero", "vapor", "cerculean", "yeti", "flatly"]

def adjust_color(color, factor):
    """Adjust color brightness by a factor.
    Positive factor makes the color lighter, negative factor makes it darker."""
    color = color.lstrip('#')
    r, g, b = int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)
    r = min(255, max(0, int(r * factor)))
    g = min(255, max(0, int(g * factor)))
    b = min(255, max(0, int(b * factor)))
    return f'#{r:02x}{g:02x}{b:02x}'

# DEFINE Root_Window
root = ttk.Window(title="VWireBox", themename=defaults["theme"], resizable=(True, True), size=(800, 600))

## DEFINE Root_Window.Top_Bar
top_bar = ttk.Canvas(root, width=800, height=50)
top_bar.pack(fill='x')
bar_color = lookup["themes"][defaults["theme"]]["top_bar"]
rect = top_bar.create_rectangle(0, 0, 800, 50, fill=bar_color)

### DEFINE Root_Window.Top_Bar.Theme_Selector
themeselector = ttk.Combobox(root, values=theme_ops, width=10, state="readonly", style="TCombobox", font=("Helvetica", 12))
themeselector.set(defaults["theme"])

theme_window = top_bar.create_window(735, 25, window=themeselector, anchor='center')

# DEFINE Bound Methods
def update_top_bar():
    new_color = lookup["themes"][defaults["theme"]]["top_bar"]
    top_bar.itemconfig(rect, fill=new_color)

def theme_selected(event):
    event.widget.selection_clear()
    selected_theme = event.widget.get()
    root.style.theme_use(selected_theme)
    with open("config.json", "w") as f:
        defaults["theme"] = selected_theme
        json.dump(defaults, f, indent=4)
    update_top_bar()
    themeselector.set(defaults["theme"])

def on_resize(event):
    new_width = event.width
    new_height = event.height
    top_bar.config(width=new_width)
    top_bar.coords(rect, 0, 0, new_width, 50)
    top_bar.coords(theme_window, new_width - 65, 25)

# SET Bindings
themeselector.bind("<<ComboboxSelected>>", theme_selected)
root.bind("<Configure>", on_resize)

# RUN Main Loop
root.mainloop()