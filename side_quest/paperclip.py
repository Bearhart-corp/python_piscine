#!/usr/bin/python3
from tkinter import *

def main():
    window = Tk(className="Paper Clip")

    # ---- STATE ----
    clips = 0
    autoclippers = 0

    clips_var = StringVar()
    auto_var = StringVar()

    clips_var.set(f"Paperclips: {clips}")
    auto_var.set(f"AutoClippers: {autoclippers}")

    # ---- FUNCTIONS ----
    def make_clip():
        nonlocal clips
        clips += 1
        clips_var.set(f"Paperclips: {clips}")

    def buy_autoclipper():
        nonlocal autoclippers
        autoclippers += 1
        auto_var.set(f"AutoClippers: {autoclippers}")

    def autoclipper_loop():
        nonlocal clips
        if autoclippers > 0:
            clips += autoclippers
            clips_var.set(f"Paperclips: {clips}")

        # rappel dans 1000 ms
        window.after(1000, autoclipper_loop)

    # ---- UI ----
    Label(window, textvariable=clips_var).pack()

    Button(window, text="Make Paperclip", command=make_clip).pack()

    Label(window, text="\nManufacturing").pack()
    Label(window, textvariable=auto_var).pack()

    Button(window, text="Buy AutoClipper", command=buy_autoclipper).pack()

    # ---- START LOOP ----
    autoclipper_loop()

    window.mainloop()

if __name__ == "__main__":
    main()
