"""
File: coin_flip_runs.py
Name: Andy Wu
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the runs!
"""

import random as r


def main():
	"""
	The same number is regarded as a run.
	Decide what you want the run is.
	"""
	print("Let's flip a coin!")
	num_run = int(input('Number of runs: '))
	run = 0
	is_in_a_row = False
	# To tell the number in a row.
	roll1 = r.randint(1, 2)
	if roll1 == 1:
		print('H', end='')
	else:
		print('T', end='')
	while True:
		if run != num_run:
			roll2 = r.randint(1, 2)
			if roll2 == 1:
				print('H', end='')
			else:
				print('T', end='')
			if roll1 == roll2:
				if not is_in_a_row:
					# The latter number is like the former number.
					run += 1
					is_in_a_row = True
					# Avoid the same pair of the run, to effect the run number.
			else:
				is_in_a_row = False
			roll1 = roll2
		else:
			break

###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
