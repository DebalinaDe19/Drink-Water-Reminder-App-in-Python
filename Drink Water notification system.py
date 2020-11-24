from win10toast import ToastNotifier
import requests
import time

if __name__ == '__main__':
    while True:
        toaster = ToastNotifier()
        toaster.show_toast("Please Drink Water Now",
                       " Drinking water will make you fitter, fresh and make your skin glow!",
                       icon_path="icon.ico.ico", duration=10)

        time.sleep(60*60)

