#!/bin/python
#-*-coding:utf-8-*-

#ポイントから四方に突っ込んでみて，一つもいけなかったら１を返す，
'''
引数の話
room_infoはその部屋の情報(どこがいけるタイルか)，2次元リスト
room_sizeは部屋のサイズ(インデックス調べるように)，リスト(要素は2つx座標とy座標)
ポイントは自分のとこ，(x, y)のタプル
'''
def travel(room_info,room_size, point):
	next_pattern = [[1,0],[0,1],[-1,0],[0,-1]]
	#print room_size
	#print point
	#print room_info
	if room_info[point[0]][point[1]] != "#":
		black_tile_list.append(point)
		for next in next_pattern:
			#print next
			next_point = (point[0]+next[0], point[1]+next[1])
			if 0 <= next_point[0] < room_size[0] and 0 <= next_point[1] < room_size[1] and next_point not in black_tile_list:
				travel(room_info,room_size, next_point)
			else:
				pass
	else:
		pass
	return 0
	#if 自分のとこがOKタイルかどうか
		# 登録されているかどうか
			#登録する
		#else
			# pass
		#四方がindexからはみ出してないかどうか
			#再起する
	#else
		#pass

def find_start(room):
	for i,l in enumerate(room):
		if '@' in l:
			return (i,l.index('@'))


import sys
data = open(sys.argv[1]).readlines()


define_flag = 0
black_tile_list = []
room = []
for line in data:
	if line == '0 0':
		break
	if define_flag == 0:
		#travel(room,point)
		start = find_start(room)
		
		if start != None:
			#print "start = ",start
			travel(room, room_info,start)
			print len(black_tile_list)
		tmp_room_info = map(int, line[:-2].split())
		room_info = [tmp_room_info[1], tmp_room_info[0]]
		define_flag = int(room_info[0])
		room = []
		black_tile_list = []
	else:
		room.append(list(line[:-2]))
		define_flag -= 1
start = find_start(room)
travel(room, room_info,start)
print len(black_tile_list)		