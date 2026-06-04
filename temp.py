from machine import Pin, SPI
from ssd1309 import Display
import onewire, ds18x20, time

spi = SPI(
    0,
    baudrate=100_000,
    polarity=0,
    phase=0,
    sck=Pin(18),
    mosi=Pin(19)
)

rst = Pin(20, Pin.OUT, value=1)
rst.value(1)

oled = Display(
    spi=spi,
    cs=Pin(17),
    dc=Pin(16),
    rst=rst,
    width=128,
    height=64,
    flip=False
)

datapin = Pin(22)

ow = onewire.OneWire(datapin)
ds = ds18x20.DS18X20(ow)

roms = ds.scan()

print("Hittade sensorer:", roms)

last_temp_1 = None
last_temp_2 = None

while True:
    ds.convert_temp()
    time.sleep(1)

    oled.clear()

    temps = []

    for rom in roms:
        temps.append(ds.read_temp(rom))
        
    oled.draw_text8x8(0, 0, str(temps[0]))
    oled.draw_text8x8(0, 16, str(temps[1]))

    time.sleep(2)




