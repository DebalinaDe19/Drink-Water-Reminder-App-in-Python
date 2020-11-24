# Drink-Water-Reminder-App-in-Python

I often used to forget to drink sufficient amount of water required for healthy body. So being a programmer I sorted this issue by building a simple Drink Water Notification System.
The program can also be built using Plyer package. However, due to some dependency anomaly on Windows 10, Plyer wasn't effective in my OS. Hence, an alternate Package called win10toast for Toast Notification is very helpful.

The program is supposed to run as a background utility. So to run it as a deamon, type the following in the python terminal.

pythonw .\main.py

Make sure to kill the program once you are done working, else it will keep on scrapping memory.
