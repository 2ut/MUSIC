import os

def s():
    os.system("cls")
    print("\u001b[31;1mYoutube \u001b[37;1mMusic Search (BYPASS)")
    search = input("/p ")
    os.system("start \"\" https://music.youtube.com/search?q=" + search)
    s()
s()
