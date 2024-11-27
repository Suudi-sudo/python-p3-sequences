#!/usr/bin/env python3

def print_fibonacci(length):

	fib_seq = []
	if length > 0:
		fib_seq.append(0)
	if length >= 2:
		fib_seq.append(1)
		for i in range(2, length):
			fib_seq.append(fib_seq[-1] + fib_seq[-2])

	print(fib_seq)