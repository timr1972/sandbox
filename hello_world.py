#!/usr/bin/python3
#
# T M Russell
# 

from datetime import date
from datetime import datetime

def main():
    now = datetime.now()
    d1_string = now.strftime("%B %d, %Y")
    t1_string = now.strftime("%H:%M:%S")
    
    temp_counter = 1
    while temp_counter < 45:
        print_stars(temp_counter)
        temp_counter = temp_counter + 5
    print("\tHello World on", d1_string)
    print("\tThe time is", t1_string)
    temp_counter = 41
    while temp_counter > 0:
        print_stars(temp_counter)
        temp_counter = temp_counter - 5
    


def print_stars(number_of_stars):
	temp_str = ""
	temp_val = 0
	while temp_val < number_of_stars:
		temp_str = temp_str + "*"
		temp_val = temp_val + 1
	print(temp_str)

if __name__ == "__main__":
   main()
