#!/usr/bin/env python3
from os.path import isfile, exists


def check_file_exist():
	'''
	check file if it is exist
	'''
	if exists('VERSION'):
		return
	with open('VERSION', 'w'): pass
	return


def write_file():
	'''
	write or modify version patch information
	'''
	check_file_exist()
	if isfile('VERSION'):
		with open('VERSION', 'r+') as w_file:
			line = w_file.read()
			print(line)
			# modify the patch of version if file not None
			if line != '':
				last_digit_pos = line.rfind('.') + 1
				w_file.seek(0)
				modify = str(int(line[last_digit_pos:]) + 1)
				line = line[:last_digit_pos] + modify
				w_file.write(line)
			# write initial version if file is None
			else:
				w_file.write('1.0.1')


if __name__ == '__main__':
	try:
		write_file()
	except OSError:
		pass
	except TypeError:
		print('Not A Valid Version')