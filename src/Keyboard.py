from msvcrt import getch
import msvcrt
import time


def main():
    print("Please press a key to see its value")
    while 1:
        if msvcrt.kbhit():
            key = ord(msvcrt.getch())
            # print(key)
            if key == 119:
                print("Forward")
            if key == 97:
                print("Left")
            if key == 115:
                print("Reverse")
            if key == 100:
                print("Right")
        time.sleep(0.001)


if __name__ == "__main__":
    main()
