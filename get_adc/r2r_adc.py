import RPi.GPIO as GPIO
import time
 
class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.compare_time = compare_time
        self.verbose = verbose
 
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21
 
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
 
    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()
 
    def number_to_dac(self, number):
        bits = [int(bit) for bit in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio, bits)
 
    def sequential_counting_adc(self):
        for i in range(256):
            self.number_to_dac(i)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) or i == 255:
                voltage = i * (self.dynamic_range / 255.0)
                if self.verbose:
                    print(f"напряжение: {voltage:.4f} В")
                return voltage
 
    def get_sc_voltage(self):
        return self.sequential_counting_adc()
 
if __name__ == "__main__":
    DYNAMIC_RANGE = 3.183  
 
    try:
        adc = R2R_ADC(dynamic_range=DYNAMIC_RANGE, verbose=True)
        while True:
            voltage = adc.get_sc_voltage()
            time.sleep(0.05)
 
    except KeyboardInterrupt:
        print("\nПрограмма остановлена пользователем.")
 
    finally:
        adc.deinit()
        print("GPIO очищены.")