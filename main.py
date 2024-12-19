import tkinter as tk
import os
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning, showerror

APP_NAME = "Stream Timer Voronessa"
VERSION = "v1.3"
COPYRIGHT = "Copyright © 2024 Artemy Gilvanov"

class TimeKeeper:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def set_time_point(self, time_point):
        self.time_point = time_point
        self.hours = time_point // 60
        self.minutes = time_point - time_point // 60 * 60

    def get_total_seconds(self):
        return self.time_point * 60

    def get_time_digit(self):
        return (self.hours, self.minutes, self.seconds)

    def count_down(self):
        if self.minutes == 0 and self.seconds == 0:
            if self.hours != 0:
                self.hours -= 1
                self.minutes = 60
        if self.minutes != 0 and self.seconds == 0:
            self.minutes -= 1
            self.seconds = 59
        else:
            self.seconds -= 1


class ControlState:
    def __init__(self, styles):
        self.styles = styles
        self.load_style, self.load_color = None, None
        self.load_time, self.load_speed = None, None
        self.load_transparent = None

    def load_state(self):
        if os.path.isfile(path="state"):
            with open("state", "r", encoding="utf-8") as state_read:
                cache_state = list()
                for element in state_read:
                    cache_state.append(element.replace("\n", ""))
                for obj_style in self.styles:
                    if obj_style.get_style()[0] in cache_state:
                        for color_style in obj_style.get_style()[2]:
                            if color_style in cache_state:
                                self.load_style = obj_style.get_style()[0]
                                self.load_color = color_style
                                for value in cache_state:
                                    if value[0] == "@":
                                        self.load_time = int(value[1:])
                                    elif value[0] == "&":
                                        self.load_speed = int(value[1:])
                                    elif value[0] == "*":
                                        self.load_transparent = int(value[1:])

                                return True
        else:
            return False

    def get_state(self):
        return self.load_style, self.load_color, self.load_time, self.load_speed, self.load_transparent

    def save_state(self, style, color, time, speed, transparent):
        if os.path.isfile(path="state"):
            with open("state", "r", encoding="utf-8") as state_read:
                cache_state = list()
                record_state = True
                time = "@" + str(time)
                speed = "&" + str(speed)
                transparent = "*" + str(transparent)
                for element in state_read:
                    cache_state.append(element.replace("\n", ""))
                if len(cache_state) == 5:
                    if style in cache_state and color in cache_state:
                        if time in cache_state and speed in cache_state:
                            if transparent in cache_state:
                                record_state = False

                    if record_state:
                        with open("state", "w", encoding="utf-8") as state_write:
                            state_write.writelines(f"@{time}\n{style}\n{color}\n&{speed}\n*{transparent}")
                else:
                    with open("state", "w", encoding="utf-8") as state_write:
                        state_write.writelines(f"@{time}\n{style}\n{color}\n&{speed}\n*{transparent}")
        else:
            with open("state", "w", encoding="utf-8") as state_write:
                state_write.writelines(f"@{time}\n{style}\n{color}\n&{speed}\n*{transparent}")


def draw_window(minutes, color, speed, style, transparent):
    if speed == 1:
        speed = 1000
    elif speed == 2:
        speed = 400
    elif speed == 3:
        speed = 100
    elif speed == 4:
        speed = 70

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

        if hours <= 9:
            img_digit_hours_b = tk.PhotoImage(file=f"clock_pack/{style}/{color}/{hours}.png")
            hours_b.configure(image=img_digit_hours_b)
            hours_b.image = img_digit_hours_b

            img_digit_hours_a = tk.PhotoImage(file=f"clock_pack/{style}/{color}/0.png")
            hours_a.configure(image=img_digit_hours_a)
            hours_a.image = img_digit_hours_a
        else:
            img_digit_hours_a = tk.PhotoImage(file=f"clock_pack/{style}/{color}/{str(hours)[0]}.png")
            hours_a.configure(image=img_digit_hours_a)
            hours_a.image = img_digit_hours_a

            img_digit_hours_b = tk.PhotoImage(file=f"clock_pack/{style}/{color}/{str(hours)[1]}.png")
            hours_b.configure(image=img_digit_hours_b)
            hours_b.image = img_digit_hours_b


    def display(minutes=0, stop_flag=False):
        timer = TimeKeeper()
        timer.set_time_point(minutes)
        def time_cycle():
            timer.count_down()
            h, m, s = timer.get_time_digit()
            total = h + m + s
            if total != 0:
                display_update(*timer.get_time_digit())
                window.after(speed, time_cycle)
            else:
                display_update(0, 0, 0)
                window.destroy()

        if not stop_flag:
            time_cycle()
        else:
            window.destroy()


    window = tk.Toplevel()
    window.focus_force()
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

    window.bind("<Double-Button-1>", lambda event: display(stop_flag=True))

    display(minutes)

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

    state = ControlState(styles_storage)

    def start_timer(preset=False):
        def warning():
            WARNING_MESSAGE = "Incorrectly entered time!"
            showwarning(title=f"{APP_NAME}", message=f"{WARNING_MESSAGE}")
        try:
            time_point = int(set_time.get()) if not preset else preset
            if time_point == 0 or time_point > 5940:
                warning()
            else:
                speed_point = int(set_speed.get())
                color_point = set_color.get()
                style_point = set_style.get()
                transparent_point = int(set_transparent.get())
                state.save_state(style_point, color_point, time_point, speed_point, transparent_point)
                draw_window(time_point, color_point, speed_point, style_point, transparent_point)
        except ValueError:
            warning()


    def about_message():
        ABOUT_MESSAGE = ("about styles:"
        "\n- icon by Artemy Gilvanov"
        "\n- in default style used font Avocado by LyonsType"
        "\n- ASCII style by Artemy Gilvanov"
        "\n- in ceramic style used font Replicant by João G. Gonçalves"
        "\n- in tech style used font Werkzeug by Dima Grenev"
        "\n- in cutouts style used font Halo Grotesk by Roman Bobkov"
        "\n- in pressure style used font Avocado by LyonsType"
        "\n- sector style by Artemy Gilvanov"
        "\n\ntechnical:"
        "\n- Tcl/Tk 8.6.13"
        "\n- Python 3.12.2"
        "\n- nuitka compiler if it is a binary file")
        showinfo(title=f"{APP_NAME}", message=f"{APP_NAME} {VERSION}\n{COPYRIGHT}\n\n{ABOUT_MESSAGE}")


    color_lst = [x for x in styles_storage[0].get_style()[2]] if directory_verified else ["not found"]
    speed_lst = [1, 2, 3, 4]
    styles_lst = [x.get_style()[0] for x in styles_storage] if directory_verified else ["not found"]
    transparent_lst = [100, 80, 60, 40, 20]


    main_window = tk.Tk()
    main_window.title(f"{APP_NAME}")
    main_window.geometry("890x47")
    main_window.resizable(False, False)
    main_window.iconphoto(True, tk.PhotoImage(file="icon.png"))

    directory_exists = error_directory() if not directory_verified else True

    time_label = ttk.Label(main_window, text="set time minutes", width=25)
    color_label = ttk.Label(main_window, text="set color", width=25)
    style_label = ttk.Label(main_window, text="set style", width=25)
    speed_label = ttk.Label(main_window, text="speed modify", width=25)
    transparent_label = ttk.Label(main_window, text="darkening %", width=25)
    launch_label = ttk.Label(main_window, text="launch", width=25)


    set_time = ttk.Entry(main_window, width=25)
    set_color = ttk.Combobox(main_window, values=color_lst, state="readonly", width=25)
    set_speed = ttk.Combobox(main_window, values=speed_lst, state="readonly", width=25)
    set_style = ttk.Combobox(main_window, values=styles_lst, state="readonly", width=25)
    set_style.bind("<<ComboboxSelected>>", lambda event: choose_colors(set_style.get()))
    set_transparent = ttk.Combobox(main_window, values=transparent_lst, state="readonly", width=25)
    start_button = ttk.Button(main_window, text="start", width=25)

    state_done = state.load_state()

    if not state_done:
        set_time.insert(0, "3")
        set_color.current(0)
        set_speed.current(0)
        set_style.current(0)
        set_transparent.current(1)
    else:
        set_time.insert(0, state.get_state()[2])
        set_color.current(color_lst.index(state.get_state()[1]))
        set_speed.current(speed_lst.index(state.get_state()[3]))
        set_style.current(styles_lst.index(state.get_state()[0]))
        set_transparent.current(transparent_lst.index(state.get_state()[4]))


    class MenuPresets:
        def ten_minutes():
            start_timer(10)

        def half_an_hour():
            start_timer(30)

        def one_hour():
            start_timer(60)

        def an_hour_and_a_half():
            start_timer(90)

        def two_hour():
            start_timer(120)


    main_menu = tk.Menu()
    main_menu.add_cascade(label="10 minutes", command=MenuPresets.ten_minutes)
    main_menu.add_cascade(label="30 minutes", command=MenuPresets.half_an_hour)
    main_menu.add_cascade(label="1 hour", command=MenuPresets.one_hour)
    main_menu.add_cascade(label="1.5 hours", command=MenuPresets.an_hour_and_a_half)
    main_menu.add_cascade(label="2 hours", command=MenuPresets.two_hour)
    main_menu.add_cascade(label="About", command=about_message)
    main_window.config(menu=main_menu)

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

    main_window.columnconfigure(index=0, weight=1, uniform="column")
    main_window.columnconfigure(index=1, weight=1, uniform="column")
    main_window.columnconfigure(index=2, weight=1, uniform="column")
    main_window.columnconfigure(index=3, weight=1, uniform="column")
    main_window.columnconfigure(index=4, weight=1, uniform="column")
    main_window.columnconfigure(index=5, weight=1, uniform="column")

    main_window.mainloop()


if __name__ == "__main__":
    main()