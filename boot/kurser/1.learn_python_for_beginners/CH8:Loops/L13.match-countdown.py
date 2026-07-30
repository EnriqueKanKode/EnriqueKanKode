"""status: løst"""

#importerte time for å ha tid mellom hvert tall i countdown
#brukte break når n = 1 for å ikke printe "1..." 2 ganger
import time
def countdown_to_start():
    for n in range(10,0,-1):
        time.sleep(1)
        if n == 1:
            print("1...Fight!")
            break
        print(f"{n}...")
        
        


# Don't edit below this line


def test():
    print("Counting down to match start:")
    countdown_to_start()
    print("=====================================")


def main():
    test()


main()
