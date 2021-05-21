"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	To find the largest digit by the helper function.
	"""
	if n > 0:
		n = n
	elif n < 0:
		n = -n
	return helper(n, 0)


def helper(num, maxima):
	if num == 0:
		return 'ans:' + str(maxima)
	else:
		a = num % 10
		# 取出餘數並比較maxima。
		if a > maxima:
			# 取代最大值maxima>。
			maxima = a
		# 降低位數
		num = (num - a) // 10
		return helper(num, maxima)


if __name__ == '__main__':
	main()
