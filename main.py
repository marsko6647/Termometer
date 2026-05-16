from machine import Pin, SPI
from ssd1309 import Display

spi = SPI(
    0,
    baudrate=100_000,
    polarity=0,
    phase=0,
    sck=Pin(18),
    mosi=Pin(19)
)

oled = Display(
    spi=spi,
    cs=Pin(17),
    dc=Pin(16),
    rst=Pin(20),
    width=128,
    height=64,
    flip=False
)

oled.clear()
oled.draw_text8x8(0, 0, "Hejsan allihopa")
oled.present()