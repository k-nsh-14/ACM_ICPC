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
	#print n #デバック用出力コード


def answear(ans_list):
	if len(ans_list) > 0:
		print ans_list.pop()
	else:
		pass

f = open('hanahuda.txt')
line = f.readline() # 1行を文字列として読み込む(改行文字も含まれる)

count = 1

n = []
r = 1
p ,c = 0, 0

while line != '0 0':
	data_set = line[:-2].split(' ')
	#shuffle()
	if count == r:#シリーズの初めってことだから[num, num] = [n, r]で配列と回数決める
		answear(n)
		num = int(data_set[0])+1#５で作っちゃうと0~4になるからこまる
		n = range(num)[1:]
		r = int(data_set[1])
		count = 0
		
		#確認用の出力たち
		#print n
		#print r
		#print count
	else:
		shuffle(int(data_set[0]), int(data_set[1]))
		count += 1
	line = f.readline()
else:
	answear(n)