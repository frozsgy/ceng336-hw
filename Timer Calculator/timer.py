
class Timer:

    __id = 0
    __bit_width = 0
    __f_clock = 40000000
    __prescaler = 1
    __postscaler = 1
    __timer_type = 0 # 0 for countdown, 1 for pr
    __timer_value = 0

    def __init__(self, id):
        self.__id = id

    def __str__(self):
        return "TIMER" + str(self.__id)

    def set_timer(self, f_clock, bit_width, prescaler, postscaler, timer_type, val):
        self.__f_clock = f_clock
        self.__bit_width = bit_width
        self.__prescaler = prescaler
        self.__postscaler = postscaler
        self.__timer_type = timer_type
        self.__timer_value = val


    def get_frequency(self):
        if self.__timer_type == 0:
            # Countdown type
            if self.__bit_width == 0:
                countdown = 256 - self.__timer_value
            else :
                countdown = 65536 - self.__timer_value
        else :
            # PR type
            countdown = self.__timer_value

        try:
            frequency = self.__f_clock / self.__prescaler / self.__postscaler / countdown
            period = 1 / frequency
            return (frequency, period)
        except:
            print("Period can't be computed")
            return (0, 0)
