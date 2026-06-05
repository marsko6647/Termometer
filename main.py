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

oled = Display(
    spi=spi,
    cs=Pin(17),
    dc=Pin(16),
    rst=rst,
    width=128,
    height=64,
    flip=False
)

ow = onewire.OneWire(Pin(22))
ds = ds18x20.DS18X20(ow)

ute_rom = b'(\xfe\xc1V\x00\x00\x00A'   # Har en utbytt stiftlist
inne_rom = b'(\xeb\xa0V\x00\x00\x00-'    

while True:
    ds.convert_temp()
    time.sleep(2)
    oled.clear()

    oled.draw_text8x8(0, 0, f"Inne {ds.read_temp(inne_rom):.0f} C")
    oled.draw_text8x8(0, 16, f"Ute {ds.read_temp(ute_rom):.0f} C")

    oled.present()

    time.sleep(2)




