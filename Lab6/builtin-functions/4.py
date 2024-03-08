import math
import time
# Write a Python program that invoke square root function after specific milliseconds

number = 25100
delay_ms = 2123

delay_s = delay_ms / 1000

time.sleep(delay_s)

sqrt_value = math.sqrt(number)

print(f"Square root of {number} after {delay_ms} milliseconds is {sqrt_value}")