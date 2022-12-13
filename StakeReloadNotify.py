import os
import ctypes
import time
import webbrowser
from plyer import notification
from tkinter import filedialog
from tkinter import *
from datetime import datetime


Tk().withdraw()

kernel32 = ctypes.windll.kernel32
handle = kernel32.GetStdHandle(-11)
kernel32.SetConsoleMode(handle, 0x0001 + 0x0002 + 0x0004)
os.system("title Auto Bonus❤ made by moku")

class C:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    RESET = '\033[0m'

class StakeReloadNotify():
    def __init__(self):
        self.AutoOpenBrowser = False
        self.Notify = False
        self.language = "en"

        self.Custome_Browser = None

        self.texts = {
            "Settings": {
                "Question_Auto_Open_Browser": {
                    "ja": "リロードが利用可能になったときに、自動でサイトを開きますか？(y/n)",
                    "en": "Do you want your browser to open automatically when you receive a bonus code?(y/n)"
                },
                "Question_Custome_Browser": {
                    "ja": "ブラウザの指定をしますか?(y/n)",
                    "en": "Would you like to specify a browser?(y/n)"
                },
                "Question_Custome_Browser_Path": {
                    "ja": "ブラウザのパスを選択してください",
                    "en": "Please select the browser path"
                },
                "Question_Notify": {
                    "ja": "リロードが利用可能になったときに、トースト通知を出しますか?(y/n)",
                    "en": "Do you want a toast notification when you receive a bonus code?(y/n)"
                },
                "SetupComplete": {
                    "ja": "セットアップが完了しました。",
                    "en": "Setup is complete."
                }
            },
            "Notify": {
                "Title": {
                    "ja": "リロードのクールダウンが終了しました。",
                    "en": "Reload cooldown has ended"
                },
                "Message": {
                    "ja": "リロードが利用可能になりました",
                    "en": "Reload is now available"
                }
            },
            "Errors": {
                "Question_Custome_Browser_Path": {
                    "NoPath": {
                        "ja": "ファイルを選択してください",
                        "en": "Please select a file"
                    },
                    "InvalidFileType":{
                        "ja": "ファイルタイプが無効です",
                        "en": "Invalid File Type"
                    },
                }
            },
        }

    def mainloop(self):
        try:
            while True:
                if self.language == "ja":
                    print(f"-{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}- リロードが利用可能になりました。")
                if self.Notify:
                    notification.notify(title=self.texts["Notify"]["Title"][self.language], message=self.texts["Notify"]["Message"][self.language], app_name="Stake Reload Notify", app_icon="money.ico", timeout=5)

                if self.AutoOpenBrowser:
                    if self.Custome_Browser:
                        browser = webbrowser.get(f'"{self.Custome_Browser}" %s')
                        browser.open("https://stake.com/?tab=reload&modal=vip")
                    else:
                        webbrowser.open_new("https://stake.com/?tab=reload&modal=vip")
                time.sleep(3900)
        except:
            self.mainloop()

    def setconfig(self):
        print("🌎Language(en/ja):")
        language = util.limited_input(["en", "ja"])
        self.language = language
        print(self.texts["Settings"]["Question_Auto_Open_Browser"][self.language])
        Question_Auto_Open_Browser = util.limited_input(["y", "n"])
        if Question_Auto_Open_Browser == "y":
            self.AutoOpenBrowser = True
        if self.AutoOpenBrowser:
            print(self.texts["Settings"]["Question_Custome_Browser"][self.language])
            Question_Custome_Browser = util.limited_input(["y", "n"])
            if Question_Custome_Browser == "y":
                print(self.texts["Settings"]["Question_Custome_Browser_Path"][self.language])
                while True:
                    path = filedialog.askopenfilename(filetypes=[("Browser",'*.exe')])
                    if path == "":
                        print(self.texts["Errors"]["Question_Custome_Browser_Path"]["NoPath"][self.language])
                        time.sleep(1)
                        print("\033[A                                                                             \033[A")
                    elif path.split(".")[-1] == ".exe":
                        print(self.texts["Errors"]["Question_Custome_Browser_Path"]["InvalidFileType"][self.language])
                        time.sleep(1)
                        print("\033[A                                                                             \033[A")
                    else:
                        self.Custome_Browser = path
                        break
        print(self.texts["Settings"]["Question_Notify"][self.language])
        Question_Notify = util.limited_input(["y", "n"])
        if Question_Notify == "y":
            self.Notify = True
        print(self.texts["Settings"]["SetupComplete"][self.language])
        time.sleep(2)
        os.system("cls")

class loading():
    def __init__(self, text:str):
        self.text = text

    def execute(self):
        i = 0
        while True:
            i += 1
            if len(self.text.split(">>^")) == 2:
                print("                                                                             ", end="\r")
                return print(self.text.split(">>^")[0])
            b = self.text + "." * i
            print(b, end="\r")
            time.sleep(0.5)

class util():
    @staticmethod
    def limited_input(limit):
        while True:
            user_input = input(">>")
            if type(limit) == list:
                if user_input in limit:
                    return user_input
                else:
                    print(f"{C.RED}Invalid input{C.RESET}")
                    time.sleep(1)
                    print("\033[A                                                                             \033[A")
                    print("\033[A                                                                             \033[A")
            elif type(limit) == int:
                if user_input.isdigit():
                    return user_input
                else:
                    print(f"{C.RED}Invalid input{C.RESET}")
                    time.sleep(1)
                    print("\033[A                                                                             \033[A")
                    print("\033[A                                                                             \033[A")
            else:
                if limit(user_input):
                    return user_input
                else:
                    print(f"{C.RED}Invalid input{C.RESET}")
                    time.sleep(1)
                    print("\033[A                                                                             \033[A")
                    print("\033[A                                                                             \033[A")


if __name__ == "__main__":
    client = StakeReloadNotify()
    client.setconfig()
    client.mainloop()