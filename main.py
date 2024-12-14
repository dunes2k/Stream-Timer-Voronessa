import tkinter as tk
import os
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning, showerror

APP_NAME = "Stream Timer Voronessa"
VERSION = "v1.1"
COPYRIGHT = "Copyright © 2024 Artemy Gilvanov"

def draw_window(minutes, color, speed, style, transparent):
    total_sec = minutes * 60
    total_hour = minutes // 60 if minutes % 60 == 0 else 0

    if speed == 1:
        speed = 1
    elif speed == 2:
        speed = 0.4
    elif speed == 3:
        speed = 0.1
    elif speed == 4:
        speed = 0.02

    if transparent == 80:
        transparent = 0.8
    elif transparent == 60:
        transparent = 0.6
    elif transparent == 40:
        transparent = 0.4
    elif transparent == 20:
        transparent = 0.2
    elif transparent == 100:
        transparent = 1

    def display_update(hours, minutes, seconds):
        if seconds <= 9:
            img_digit_seconds_b = tk.PhotoImage(file=f"clock_pack/{style}/{color}/{seconds}.png")
            seconds_b.configure(image=img_digit_seconds_b)
            seconds_b.image = img_digit_seconds_b

            img_digit_seconds_a = tk.PhotoImage(file=f"clock_pack/{style}/{color}/0.png")
            seconds_a.configure(image=img_digit_seconds_a)
            seconds_a.image = img_digit_seconds_a
        else:
            img_digit_seconds_a = tk.PhotoImage(file=f"clock_pack/{style}/{color}/{str(seconds)[0]}.png")
            seconds_a.configure(image=img_digit_seconds_a)
            seconds_a.image = img_digit_seconds_a

            img_digit_seconds_b = tk.PhotoImage(file=f"clock_pack/{style}/{color}/{str(seconds)[1]}.png")
            seconds_b.configure(image=img_digit_seconds_b)
            seconds_b.image = img_digit_seconds_b
        if minutes <= 9:
            img_digit_minutes_b = tk.PhotoImage(file=f"clock_pack/{style}/{color}/{minutes}.png")
            minutes_b.configure(image=img_digit_minutes_b)
            minutes_b.image = img_digit_minutes_b

            img_digit_minutes_a = tk.PhotoImage(file=f"clock_pack/{style}/{color}/0.png")
            minutes_a.configure(image=img_digit_minutes_a)
            minutes_a.image = img_digit_minutes_a
        else:
            img_digit_minutes_a = tk.PhotoImage(file=f"clock_pack/{style}/{color}/{str(minutes)[0]}.png")
            minutes_a.configure(image=img_digit_minutes_a)
            minutes_a.image = img_digit_minutes_a

            img_digit_minutes_b = tk.PhotoImage(file=f"clock_pack/{style}/{color}/{str(minutes)[1]}.png")
            minutes_b.configure(image=img_digit_minutes_b)
            minutes_b.image = img_digit_minutes_b


    def tksleep(time_second):
        milliseconds = int(time_second*1000)
        window = tk._get_default_root('sleep')
        var = tk.IntVar(window)
        window.after(milliseconds, var.set, 1)
        window.wait_variable(var)


    def display(hours=0, minutes=0, total_seconds=0):
        seconds = 0
        for value in range(0, total_seconds):
            tksleep(speed)
            if hours > 0 or minutes > 0 and seconds == 0:
                minutes -= 1
                seconds += 59
                display_update(hours, minutes, seconds)
            else:
                seconds -= 1
                display_update(hours, minutes, seconds)
        window.destroy()


    window = tk.Toplevel()
    window.title(f"{APP_NAME}")
    window.attributes("-fullscreen", True)
    window.attributes("-alpha", transparent)
    window.configure(bg="#000000")

    img_digit = tk.PhotoImage(file=f"clock_pack/{style}/{color}/0.png")
    img_point = tk.PhotoImage(file=f"clock_pack/{style}/{color}/_0.png")

    plug_a = tk.Label(window, width=192, height=360, bg="#000000")

    hours_a = tk.Label(window, width=192, height=360, image=img_digit, borderwidth=0)
    hours_b = tk.Label(window, width=192, height=360, image=img_digit, borderwidth=0)

    dot_a = tk.Label(window, width=192, height=360, image=img_point, borderwidth=0)

    minutes_a = tk.Label(window, width=192, height=360, image=img_digit, borderwidth=0)
    minutes_b = tk.Label(window, width=192, height=360, image=img_digit, borderwidth=0)

    dot_b = tk.Label(window, width=192, height=360, image=img_point, borderwidth=0)

    seconds_a = tk.Label(window, width=192, height=360, image=img_digit, borderwidth=0)
    seconds_b = tk.Label(window, width=192, height=360, image=img_digit, borderwidth=0)

    plug_b = tk.Label(window, width=192, height=360, bg="#000000")

    plug_a.grid(row=0, column=0)
    hours_a.grid(row=0, column=1)
    hours_b.grid(row=0, column=2)
    dot_a.grid(row=0, column=3)
    minutes_a.grid(row=0, column=4)
    minutes_b.grid(row=0, column=5)
    dot_b.grid(row=0, column=6)
    seconds_a.grid(row=0, column=7)
    seconds_b.grid(row=0, column=8)
    plug_b.grid(row=0, column=9)

    window.columnconfigure(index=0, weight=1, uniform="column"), window.rowconfigure(index=0, weight=1)
    window.columnconfigure(index=1, weight=1, uniform="column")
    window.columnconfigure(index=2, weight=1, uniform="column")
    window.columnconfigure(index=3, weight=1, uniform="column")
    window.columnconfigure(index=4, weight=1, uniform="column")
    window.columnconfigure(index=5, weight=1, uniform="column")
    window.columnconfigure(index=6, weight=1, uniform="column")
    window.columnconfigure(index=7, weight=1, uniform="column")
    window.columnconfigure(index=8, weight=1, uniform="column")
    window.columnconfigure(index=9, weight=1, uniform="column")

    window.bind("<Double-Button-1>", lambda event: display())

    display(total_hour, minutes, total_sec)

    window.mainloop()


class Style:
    def __init__(self, style_name, style_path):
        self.style_name = style_name
        self.style_path = style_path
        self.style_color = list()
        self.delete_trigger = False

    def set_color(self, style_color):
        self.style_color.append(style_color)

    def get_style(self):
        return self.style_name, self.style_path, self.style_color

    def set_delete_trigger(self, delete_trigger):
        self.delete_trigger = delete_trigger

    def get_delete_trigger(self):
        return self.delete_trigger


def main():
    def error_directory():
        ERROR_MESSAGE = ("clock_pack directory error!"
        "\nThe clock_pack folder seems to be missing or it doesn't contain any styles.")
        showerror(title=f"{APP_NAME}", message=f"{ERROR_MESSAGE}")
        return False


    styles_storage = []

    try:
        with os.scandir(path="clock_pack/") as check_pack:
            for pack in check_pack:
                styles_storage.append(Style(pack.name, pack.path))

        for style_object in styles_storage:
            if os.path.isfile(path=f"{style_object.get_style()[1]}/!empty"):
                with os.scandir(path=f"{style_object.get_style()[1]}/") as style_color:
                    for colors in style_color:
                        if os.path.isfile(path=f"{style_object.get_style()[1]}/{colors.name}/include"):
                            style_object.set_color(colors.name)
            else:
                style_object.set_delete_trigger(True)

        cache_styles = []

        for candidate in styles_storage:
            if not candidate.get_delete_trigger():
                cache_styles.append(candidate)

        styles_storage = cache_styles[:]

        directory_verified = True
        directory_verified = True if len(styles_storage) > 0 else False

    except FileNotFoundError:
        directory_verified = False

    def choose_colors(style_choose):
        for style_object in styles_storage:
            if style_object.style_name == style_choose:
                set_color.configure(values=style_object.get_style()[2])
                set_color.current(0)


    def start_timer():
        def warning():
            WARNING_MESSAGE = "Incorrectly entered time!"
            showwarning(title=f"{APP_NAME}", message=f"{WARNING_MESSAGE}")
        try:
            time_point = int(set_time.get())
            if time_point == 0:
                warning()
            else:
                speed_point = int(set_speed.get())
                color_point = set_color.get()
                style_point = set_style.get()
                transparent_point = int(set_transparent.get())
                draw_window(time_point, color_point, speed_point, style_point, transparent_point)
        except ValueError:
            warning()


    def about_message():
        ABOUT_MESSAGE = ("about styles:\n- icon by Artemy Gilvanov\n- in default style used font Avocado by LyonsType"
        "\n- ASCII style by Artemy Gilvanov\n- in ceramic style used font Replicant by João G. Gonçalves\n"
        "- in tech style used font Werkzeug by Dima Grenev\n\ntechnical:\n- Tcl/Tk 8.6.13\n- Python 3.12.2"
        "\n- nuitka compiler if it is a binary file")
        showinfo(title=f"{APP_NAME}", message=f"{APP_NAME} {VERSION}\n{COPYRIGHT}\n\n{ABOUT_MESSAGE}")


    color_lst = [x for x in styles_storage[0].get_style()[2]] if directory_verified else ["not found"]
    speed_lst = [1, 2, 3, 4]
    styles_lst = [x.get_style()[0] for x in styles_storage] if directory_verified else ["not found"]
    transparent_lst = [100, 80, 60, 40, 20]

    main_window = tk.Tk()
    main_window.title(f"{APP_NAME}")
    main_window.geometry("917x50")
    main_window.resizable(False, False)
    main_window.iconphoto(True, tk.PhotoImage(file="icon.png"))
    main_menu = tk.Menu()
    main_menu.add_cascade(label="About", command=about_message)
    main_window.config(menu=main_menu)

    directory_exists = error_directory() if not directory_verified else True

    time_label = ttk.Label(main_window, text="set time minutes")
    color_label = ttk.Label(main_window, text="set color")
    style_label = ttk.Label(main_window, text="set style")
    speed_label = ttk.Label(main_window, text="speed modify")
    transparent_label = ttk.Label(main_window, text="darkening %")
    launch_label = ttk.Label(main_window, text="launch")

    set_time = ttk.Entry(main_window)
    set_time.insert(-1, "1")

    set_color = ttk.Combobox(main_window, values=color_lst, state="readonly")
    set_color.current(0)

    set_speed = ttk.Combobox(main_window, values=speed_lst, state="readonly")
    set_speed.current(0)

    set_style = ttk.Combobox(main_window, values=styles_lst, state="readonly")
    set_style.bind("<<ComboboxSelected>>", lambda event: choose_colors(set_style.get()))
    set_style.current(0)

    set_transparent = ttk.Combobox(main_window, values=transparent_lst, state="readonly")
    set_transparent.current(1)

    start_button = ttk.Button(main_window, text="start", width=25)

    if not directory_exists:
        start_button.configure(command=error_directory)
    else:
        start_button.configure(command=start_timer)

    time_label.grid(row=0, column=0, padx=5)
    color_label.grid(row=0, column=1, padx=5)
    speed_label.grid(row=0, column=2, padx=5)
    style_label.grid(row=0, column=3, padx=5)
    transparent_label.grid(row=0, column=4, padx=5)
    launch_label.grid(row=0, column=5, padx=5)

    set_time.grid(row=1, column=0, padx=5)
    set_color.grid(row=1, column=1, padx=5)
    set_speed.grid(row=1, column=2, padx=5)
    set_style.grid(row=1, column=3, padx=5)
    set_transparent.grid(row=1, column=4, padx=5)
    start_button.grid(row=1, column=5, padx=5)

    main_window.mainloop()


if __name__ == "__main__":
    main()