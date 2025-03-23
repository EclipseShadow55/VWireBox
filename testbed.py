import ttkbootstrap as ttk
import json

theme = "darkly"
test = True
with open("lookup.json", "r") as f:
    lookup = json.load(f)

if not test:
    root = ttk.Window(title="Tester", resizable=(False, False), size=(800, 600))

    canvas = ttk.Canvas(root, width=800, height=600)
    canvas.pack(fill='both')
    primary = canvas.create_rectangle(0, 0, 100, 600, fill=lookup["themes"][theme]["primary"])
    secondary = canvas.create_rectangle(100, 0, 200, 600, fill=lookup["themes"][theme]["secondary"])
    success = canvas.create_rectangle(200, 0, 300, 600, fill=lookup["themes"][theme]["success"])
    info = canvas.create_rectangle(300, 0, 400, 600, fill=lookup["themes"][theme]["info"])
    warning = canvas.create_rectangle(400, 0, 500, 600, fill=lookup["themes"][theme]["warning"])
    danger = canvas.create_rectangle(500, 0, 600, 600, fill=lookup["themes"][theme]["danger"])
    light = canvas.create_rectangle(600, 0, 700, 600, fill=lookup["themes"][theme]["light"])
    dark = canvas.create_rectangle(700, 0, 800, 600, fill=lookup["themes"][theme]["dark"])
else:
    root = ttk.Window(title="Tester", themename=theme, resizable=(False, False), size=(900, 600))
    canvas = ttk.Canvas(root, width=900, height=600)
    canvas.pack(fill='both')
    bar = canvas.create_rectangle(0, 0, 900, 50, fill=lookup["themes"][theme]["top_bar"])
    primary = canvas.create_rectangle(0, 50, 100, 600, fill=lookup["themes"][theme]["primary"])
    secondary = canvas.create_rectangle(100, 50, 200, 600, fill=lookup["themes"][theme]["secondary"])
    success = canvas.create_rectangle(200, 50, 300, 600, fill=lookup["themes"][theme]["success"])
    info = canvas.create_rectangle(300, 50, 400, 600, fill=lookup["themes"][theme]["info"])
    warning = canvas.create_rectangle(400, 50, 500, 600, fill=lookup["themes"][theme]["warning"])
    danger = canvas.create_rectangle(500, 50, 600, 600, fill=lookup["themes"][theme]["danger"])
    light = canvas.create_rectangle(600, 50, 700, 600, fill=lookup["themes"][theme]["light"])
    dark = canvas.create_rectangle(700, 50, 800, 600, fill=lookup["themes"][theme]["dark"])

root.mainloop()