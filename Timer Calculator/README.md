# PIC18F8722 TIMER Values Calculator

This repository aims to help you with your timer values calculations while using [PIC18F8722](https://www.microchip.com/wwwproducts/en/PIC18F8722) (Microchip Technology Inc.). You can get the frequency and period values of a timer by entering the timer settings easily.

## Background

While working on the homework assignments for [METU](https://www.metu.edu.tr) [CENG336 Introduction to Embedded Systems Development](https://github.com/frozsgy/ceng336-hw) course, I got bored of doing the same mundane calculations by hand whenever I needed to use a timer, or change the timer frequency. That lead to the idea of writing this Python script to handle these calculations quickly. 

Theoretically, any PIC Microcontroller using the same timers should work with this script nicely as well, but I don't have any and I don't have any intention to get any either. So, use at your own risk! 

## Quick Notes

* While doing the computations, it is your own responsibility to check if the entered pre and post-scaler values supported on the given timer. The script does not check it, and it might differ on the version of the microcontroller. The [Datasheet](http://ww1.microchip.com/downloads/en/devicedoc/39646c.pdf) is your Holy Bible on this.
* Reverse calculation is not implemented. Since each timer has different pre and post-scaler settings, hardcoding these values seemed pointless, and I decided trial and error is better than coding that. If you want to implement it, I'd be happy to accept the pull request.
* I know that this is over-engineered. I needed something to fiddle around, and kept on writing more of this.

## Usage

1. Simply run `main.py` with Python 3.
2. To exit, hit CTRL+D.
3. Hitting CTRL+C will restart the application from scratch, so you can enter new values if you mistyped anything.

## Dependencies

* Python 3

## Bugs, Comments, Ideas?

Don't hesitate contacting me, or sending a pull request. They are always welcome.