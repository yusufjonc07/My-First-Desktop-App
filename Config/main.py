from asyncio.log import logger
from doctest import master
from email.mime import image
import os
import sys
import logging
import datetime

from tkinter import *
from tkinter import messagebox

import tkinter
from turtle import title
import customtkinter

from ctypes import windll
from PIL import Image, ImageTk

windll.shcore.SetProcessDpiAwareness(1)

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("System")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("dark-blue")

LOG = ""
ROOT = tkinter.Tk()
TKINTER_WIDGETS = {}
APP_WIDTH = 700
APP_HEIGHT = 320

CURRENT_SCRIPT_NAME = os.path.basename(__file__).split(".")[0]

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
CONFIG_DIRECTORY = os.path.join(CURRENT_DIRECTORY, "Config")
IMAGES_DIRECTORY = os.path.join(CURRENT_DIRECTORY, "Images")
LOGS_DIRECTORY = os.path.join(CURRENT_DIRECTORY, "Logs")


def logger():

    global LOG

    LOG = logging.getLogger(__name__)
    LOG.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s : %(levelname)s : %(funcName)s : %(lineno)d : %(message)s', datefmt="%d-%m-%Y %H:%m%S")

    current_year_month = datetime.datetime.now().strftime("%m-%Y")

    log_file_name = f"{current_year_month}_{CURRENT_SCRIPT_NAME}.log"

    os.makedirs(LOGS_DIRECTORY, exist_ok=True)

    log_file = os.path.join(LOGS_DIRECTORY, log_file_name)

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    LOG.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    LOG.addHandler(stream_handler)


def exit_bot():
    LOG.debug("Exit bot")

    quit_homepage()

    LOG.debug("Exit bot")
    sys.exit(0)


def quit_homepage():
    LOG.debug("Qit Homepage")

    global ROOT

    ROOT.destroy()


def homepage():

    LOG.debug("-- Homepage --")

    global ROOT
    global TKINTER_WIDGETS

    try:
        head_frame = customtkinter.CTkFrame(master=ROOT, corner_radius=10)
        head_frame.grid(row=1, column=0, padx=5, pady=5)

        img = Image.open(os.path.join(IMAGES_DIRECTORY, "yuvish.png"))
        img_resized = img.resize((370, 300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img_resized)

        TKINTER_WIDGETS['label_img'] = customtkinter.CTkLabel(
            master=head_frame, image=img, corner_radius=7)
        TKINTER_WIDGETS['label_img'].img = img
        TKINTER_WIDGETS['label_img'].grid(
            row=0, column=2, columnspan=2, padx=15, pady=10)

       

        frame_login = customtkinter.CTkFrame(master=head_frame, corner_radius=10)
        frame_login.grid(row=0, column=0, padx=15, pady=20)

        button_div = customtkinter.CTkFrame(master=frame_login, corner_radius=10)
        button_div.grid(row=2, column=0, padx=0, pady=10, columnspan=3)

        # Username input
        TKINTER_WIDGETS['label_username'] = customtkinter.CTkLabel(
            master=frame_login, text="Login:", width=30, height=25, corner_radius=7)
        TKINTER_WIDGETS['label_username'].grid(
            row=0, column=0,  padx=10, pady=20)

        TKINTER_WIDGETS['entry_username'] = customtkinter.CTkEntry(
            master=frame_login, placeholder_text="Loginni kiriting", width=200, height=30, corner_radius=10, border_width=2)
        TKINTER_WIDGETS['entry_username'].grid(
            row=0, column=1,  padx=10, columnspan=2)

        # Password input
        TKINTER_WIDGETS['label_password'] = customtkinter.CTkLabel(
            master=frame_login, text="Parol:", width=30, height=25, corner_radius=7)
        TKINTER_WIDGETS['label_password'].grid(
            row=1, column=0,  padx=10, pady=5, sticky='e')

        TKINTER_WIDGETS['entry_password'] = customtkinter.CTkEntry(
            master=frame_login, placeholder_text="Parolni kiriting", show="*", text_font=("Robot-Medium", 10), width=200, height=30, corner_radius=10, border_width=2)
        TKINTER_WIDGETS['entry_password'].grid(
            row=1, column=2, pady=20,  padx=10, columnspan=2)

        # Login button
        TKINTER_WIDGETS['button_login'] = customtkinter.CTkLabel(
            master=button_div, text="Kirish", width=70, fg_color=("#36719F", "red"), text_color="#fff", corner_radius=10)
        TKINTER_WIDGETS['button_login'].grid(
            row=0, column=0,  padx=10, pady=10, sticky='e')

        # bekor button
        TKINTER_WIDGETS['button_login'] = customtkinter.CTkLabel(
            master=button_div, text="Bekor qilish", width=70, fg_color=("gray", "red"), text_color="#fff", corner_radius=10)
        TKINTER_WIDGETS['button_login'].grid(
            row=0, column=0,  padx=90, pady=10, sticky='e')


    except Exception as e:
        LOG.error("Failed")
        LOG.error(e, exc_info=True)



  

def load_ui(myfunc):

    LOG.debug("- UI ni yuklash")

    global ROOT

    ROOT.title = "Yuvish Desktop - Kirish"
    ROOT.iconphoto = "icon.png"

    myfunc()

    screen_width = ROOT.winfo_screenwidth()
    screen_height = ROOT.winfo_screenheight()

    app_center_coordinate_x = (screen_width / 3) - (APP_WIDTH / 3)
    app_center_coordinate_y = (screen_height / 3) - (APP_HEIGHT / 3)

    ROOT.geometry(
        f"{APP_WIDTH}x{APP_HEIGHT}+{int(app_center_coordinate_x)}+{int(app_center_coordinate_y)}")
    # ROOT.resizable(width=False, height=False)
    ROOT.protocol("WM_DELETE_WINDOW", exit_bot)

    ROOT.mainloop()


if __name__ == "__main__":
    logger()
    load_ui(homepage)
