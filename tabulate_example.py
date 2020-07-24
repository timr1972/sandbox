#!/usr/bin/python3
#
# T M Russell
# 

from tabulate import tabulate

def main():
    print_stars(40)
    print(tabulate([["value1", "value2"], ["value3", "value4"]], ["column 1", "column 2"], tablefmt="grid"))
    print_stars(40)

def print_stars(number_of_stars):
	temp_str = ""
	temp_val = 0
	while temp_val < number_of_stars:
		temp_str = temp_str + "*"
		temp_val = temp_val + 1
	print(temp_str)

if __name__ == "__main__":
   main()
