import time
from timer import *

timers = []

def init_timers():
    for i in range(5):
        timers.append(Timer(i))

def get_fosc():
    while True:
        f_osc = input("Enter oscillator frequency in Hz: ")
        try:
            f_osc = int(f_osc)
            if f_osc > 0:
                return f_osc
            else:
                print("Oscillator frequency must be greater than 0\n")    
        except:
            print("Oscillator frequency is not an integer\n")
            
def select_timer():
    while True:
        print("\nSelect the TIMER by indicating the number")

        c = 0
        for i in timers:
            print("%d - %s" % (c, i))
            c += 1

        t_select = input("Timer: ")

        try:
            t_select = int(t_select)
            if t_select < c and t_select > -1:
                return t_select
            else :
                print("Selected TIMER is not valid")
        except:
            print("Selected TIMER is not valid")


def get_prescaler(min_val = 1, max_val = 256):
    while True:
        prescaler = input("Prescaler value (between %d and %d): " % (min_val, max_val))
        try:
            prescaler = int(prescaler)
            if prescaler in range(min_val, max_val + 1):
                return prescaler
            else :
                print("Prescaler value is not in range\n")
        except:
            print("Prescaler value is not in range\n")

def get_postscaler(min_val = 1, max_val = 16):
    while True:
        postscaler = input("Postscaler value (between %d and %d): " % (min_val, max_val))
        try:
            postscaler = int(postscaler)
            if postscaler in range(min_val, max_val + 1):
                return postscaler
            else :
                print("Postscaler value is not in range\n")
        except:
            print("Postscaler value is not in range\n")

def get_init(bit_width):
    while True:
        tmr = input("TIMER initial value: ")
        try:
            tmr = int(tmr)
            if (bit_width == 0 and tmr < 256) or (bit_width == 1 and tmr < 65536):
                return tmr
            else :
                print("TIMER initial value is not valid\n")    
        except:
            print("TIMER initial value is not valid\n")

def get_bit_width():
    while True:
        tmr = input("Enter the bit-width, 0 for 8-bit, 1 for 16-bit: ")
        try:
            tmr = int(tmr)
            if tmr in [0, 1]:
                return tmr
            else :
                print("Bit-width is not valid\n")
        except:
            print("Bit-width is not valid\n")

def get_pr():
    while True:
        pr = input("TIMER PR value: ")
        try:
            pr = int(pr)
            if pr < 256:
                return pr
            else :
                print("TIMER PR value is not valid\n")    
        except:
            print("TIMER PR value is not valid\n")

def calculate_timer(f_clock, timer):
    print("")
    if timer in [0, 1, 3]:
        bit_width = get_bit_width()
    else :
        bit_width = 0
    
    if timer in [0, 1, 3]:
        timer_init = get_init(bit_width)
        timer_type = 0
    else :
        timer_init = get_pr()
        timer_type = 1
    
    prescaler = get_prescaler(1, 256)

    if timer in [2,4]:
        postscaler = get_postscaler()
    else :
        postscaler = 1
    
    timers[timer].set_timer(f_clock, bit_width, prescaler, postscaler, timer_type, timer_init)

    timer_frequency, timer_period = timers[timer].get_frequency()
    if timer_frequency != 0:
        print("\n%s Frequency: %d" % (timers[timer], timer_frequency))
        print("%s Period: %.6f s (%.3f ms, %.2f us)\n" % (timers[timer], timer_period, timer_period * 1000, timer_period * 1000 * 1000))
        print("-" * 40 + "\n")
    
def main():
    print("-" * 40 + "\n")
    print("Welcome to PIC18F8722 TIMER Values Calculator!\n")
    print("This application aims to help you with your timer values calculations. While doing the computations, it is your own responsibility to check if the entered pre and post-scaler values supported on the given timer. Please always refer to the Datasheet in any case of discrepancies.")
    print("\nYou can use the GitHub page to report bugs, leave comments, or anything else: https://github.com/frozsgy/PIC18F8722-TIMER-Values-Calculator")
    print("\nThanks for using this app! \n")
    print("-" * 40 + "\n")
    print("Use CTRL+C to restart.")
    print("Use CTRL+D to exit.\n")
    print("-" * 40 + "\n")
    init_timers()
    while True:
        try:
            f_osc = get_fosc()

            f_clock = f_osc / 4

            timer = select_timer()

            calculate_timer(f_clock, timer)

        except KeyboardInterrupt:
            print("\n\nRestarting the app", end ="", flush=True)
            time.sleep(0.07)
            print(".", end ="", flush=True)
            time.sleep(0.07)
            print(".", end ="", flush=True)
            time.sleep(0.07)
            print(".\n", flush=True)
            continue

        except EOFError:
            print("\nGoodbye!")
            exit()

if __name__ == "__main__":
    main()