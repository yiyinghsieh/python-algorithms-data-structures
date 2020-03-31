"""Array.diff
6 kyu

URL:https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
"""


def array_diff(a, b):



def main():
	# Output: [2]
	a, b = [1,2], [1]
	print(array_diff(a, b))


 assert array_diff([1,2], [1]) == [2], "a was [1,2], b was [1], expected [2]"
 assert array_diff([1,2,2], [1]) == [2,2], "a was [1,2,2], b was [1], expected [2,2]"
 assert array_diff([1,2,2], [2]) == [1], "a was [1,2,2], b was [2], expected [1]"
 assert array_diff([1,2,2], []) == [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]"
 assert array_diff([], [1,2]) == [], "a was [], b was [1,2], expected []"



if __main__ == '__name__':
	main()