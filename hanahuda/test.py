#!/bin/python
#-*-coding:utf-8-*-

def shuffle(p, c):
	p_stack = []
	c_stack = []
	
	for i in range(p-1):#まずはp-1個の数字をキューに退避させる
		p_num = n.pop()
		p_stack.insert(0, p_num)
	
	for i in range(c):#次にc個の数字をキューに退避させる
		c_num = n.pop()
		c_stack.insert(0, c_num)
	
	#順番を入れ替えてnに戻してあげる
	n.extend(p_stack)
	n.extend(c_stack)
	print n #デバック用出力コード

def answear(ans_list):
	if len(ans_list) > 0:
		print ans_list.pop()
	else:
		pass

f = open("hanahuda.txt")
line = f.readline()

count = 0
r = 0
n = []
while line != '0 0':
	data_set =	 line[:-2].split(' ')
	if count == r:
		answear(n)
		r = int(data_set[1])
		count = 0
		n = range(int(data_set[0])+1)[1:]
		print n
	else:
		shuffle(int(data_set[0]),int(data_set[1]))
		count += 1
		
	line = f.readline()
else:
	answear(n)