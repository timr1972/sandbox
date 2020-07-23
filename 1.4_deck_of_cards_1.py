#!/usr/bin/python3
#
# T M Russell
# Devnet Challange 1.4
# Using Loops print all cards in a deck
# Designed to run in Python3
#

def main():
	cards=['A','1','2','3','4','5','6','7','8','9','10','J','Q','K']
	suits=['C','S','H','D']
	long_suit=['Clubs','Spades','Hearts','Diamonds']
	print_stars(40)
	temp_str = ""
	for x in range(len(suits)):
		temp_str = temp_str + "\n" + long_suit[x] + "\n"
		for y in range(len(cards)):
			temp_str = temp_str + cards[y] + "-" + suits[x] + "\t"
			if cards[y] == "K":
				temp_str = temp_str + "\n"
	print(temp_str)
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
   
