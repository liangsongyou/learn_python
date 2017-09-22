def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1

	return d

def print_hist(h):
	for c in h:
		print (c, h[c])

def reverse_lookup(d, v):
	"""如果我们到达了循环的终点，就意味着v在字典中没有作为值出现过，所以抛出异常

	这个函数接收一个值，并且返回映射到该值的第一个键。

	反向查找

	"""
	for k in d:
		if d[k] == v:
			return k
	raise LookupError()

	

