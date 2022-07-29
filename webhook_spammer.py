import sys
import requests
import ctypes

kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
SW_HIDE = 0
hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_HIDE)

if len(sys.argv) == 4:
    webhook = sys.argv[1]
    content = sys.argv[2]
    amount = int(sys.argv[3])
    
for i in range (amount):
    requests.post(webhook,json={'content': content})