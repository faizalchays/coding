import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\nsudah terbiasa terjadi tante", 0.10),
        ("teman datang ketika lagi butuh saja", 0.09),
        ("coba kalo lagi susah", 0.08),
        ("mereka semua menghilang...", 0.09),
        ("tante\n", 0.07),
    ]
    
    delays = [0.3, 3.9, 8.1, 11.0, 16.8]  
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()