from sys import argv
import string

def process_input_file(filename):
	line = open(filename)
	line = line.read()
	for char in line:
		index = ord(string.lower(char)) - 97
		alpha_table[i] += 1

def setup_alphabet_table():
#	alphabet=[abcdefghijklmnopqrstuvwxyz]
	alpha_table = []
	for i in range(26):
		print i
		alpha_table[i] = 0

def count_letters_in_the_file(argv):

	script, filename = argv

	process_input_file(filename)

def main():
	setup_alphabet_table() 
	count_letters_in_the_file(argv)



if __name__ == "__main__":
	main()