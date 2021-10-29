def __print(*args, **kwargs):
	# old_print(args) # ('hello world', 'xxx', 22)
	# old_print(kwargs) # {'sep': '.', 'end': '\n\n'}
	pass

old_print = print
__builtins__.print = __print

print('hello world', 'xxx', 22, sep='.', end='\n\n')