import multiprocessing as mp
import os
import time

def main(rank, a):
	if rank != 0:
		__print = lambda *args, **kwargs: ...
		__builtins__['print'] = __print
	else:
		ori_print = __builtins__['print']
		__print = lambda *args, **kwargs: ori_print(*args, **kwargs, flush=True)
		__builtins__['print'] = __print
	
	for i in range(5):
		time.sleep(2)
		print(rank, a, time.ctime())

def spawn(target, nprocs, args=(), kwargs={}):
	procs = []
	for i in range(nprocs):
		p = mp.Process(
			target=target, 
			args=(i, ) + args, 
			kwargs=kwargs, 
			daemon=True
		)
		p.start()
		procs.append(p)
	for p in procs:
		p.join()

if __name__ == '__main__':
	spawn(
		target=main,
		nprocs=4,
		args=('hello world!', )
	)
	print('done!')