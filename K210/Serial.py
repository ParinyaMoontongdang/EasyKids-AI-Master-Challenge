from fpioa_manager import fm
from machine import UART
import time

fm.register(6, fm.fpioa.UART2_RX)
fm.register(8, fm.fpioa.UART2_TX)

yb_uart = UART(UART.UART2, 115200, 8, 0, 0, timeout=1000, read_buf_len=4096)

try:
    while True:
        data = b'on\n'
        yb_uart.write(data)
        print("Sent:", data)
        time.sleep(2)

        data = b'off\n'
        print("Sent:", data)
        yb_uart.write(data)
        time.sleep(1)
except:
    pass
