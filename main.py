from machine import Pin, SPI
from ssd1306 import SSD1306_SPI

print("START")

spi = SPI(
    0,
    baudrate=1_000_000,
    polarity=0,
    phase=0,
    sck=Pin(18),
    mosi=Pin(19)
)

print("SPI OK")

oled = SSD1306_SPI(
    128,
    64,
    spi,
    dc=Pin(16),
    res=Pin(20),
    cs=Pin(17)
)

print("OLED OK")

oled.fill(1)
oled.show()

print("DONE")