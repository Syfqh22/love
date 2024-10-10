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
        ("Help me.", 0.1),
        ("Help me, help me, help me.", 0.1),
        ("Help me, help me, help, help, help, help, help, help, help, help, help, help, help, help, help, help me!", 0.1),
        ("It hurts, it hurts, it hurts, it hurts, it hurts, it hurts...", 0.1),
        ("It hurts, it hurts, it hurts, it hurts, it hurts, IT HURTS, IT HURTS, IT HURTS, IT HURTS, IT HURTS, IT HURTS, IT HURTS!", 0.08),
        ("Why can't I die?", 0.1),
        ("WHY CAN'T I DIE?!", 0.1)
    ]
    
    delays = [0.3, 2.0, 4.0, 6.0, 10.0, 15.0, 18.0]
    
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
