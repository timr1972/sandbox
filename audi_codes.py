#!/usr/bin/python3
#
# T M Russell
# Looking up audi codes using a python interpreter
#

import csv
import sys
import subprocess as sp
tmp = sp.call('cls', shell=True)

def main():
	print_stars(40)
	print("\n\nType 3 characters, these will be added to a feature list.  Enter with no characters to finish and the list will be printed to screen.")
	#
	code_count = 0
	finished =0
	vag_array = []
	
	while finished == 0:
		vag_code = input(str(code_count) + " :")
		# Convert to Upper String
		vag_code = vag_code.upper()
		# Change O to 0
		vag_code = vag_code.replace("O", "0")

		# Check for no entry...
		if vag_code == "":
			finished = 1
		else:
			finished = 0
			csv_file = csv.reader(open('vag-option-codes.csv', "r"))
			for row in csv_file:
				if vag_code == row[3]:
					vag_array.append([vag_code.upper(),row[5]])
					found=1
			if found != 1:
				vag_array.append([vag_code.upper(),'Not Found'])
			found = 0
			csv_file = ""
		code_count = code_count + 1
	for x in vag_array:
		print(x)
	print_stars(40)

	#
	# CSV file with codes is vag-option-codes.csv
	#
	
def print_stars(number_of_stars):
	temp_str = ""
	temp_val = 0
	while temp_val < number_of_stars:
		temp_str = temp_str + "*"
		temp_val = temp_val + 1
	print(temp_str)

  
if __name__ == "__main__":
   main()
   
