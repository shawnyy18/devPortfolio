import machine
import utime

sensor_pir = machine.Pin(28, machine.Pin.IN)
led = machine.Pin(15, machine.Pin.OUT)
buzzer = machine.Pin(14, machine.Pin.OUT)

def pir_handler(pin):
    print("Alarm! Motion Detected!")
    for i in range(50):
        led.toggle()
        buzzer.toggle()
        utime.sleep_ms(100)

def cleanup():
    led.off()  
    buzzer.off()  

sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

try:
    while True:
        led.toggle()
        utime.sleep(1)
except KeyboardInterrupt:
    cleanup()  
