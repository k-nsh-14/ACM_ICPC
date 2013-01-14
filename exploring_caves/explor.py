#!/bin/pyton
#-*-coding:utf-8-*-
import math
def go_next(now, distance):
	tmp = [0, 0]
	#print "     now = ", now
	#print "distance = ",distance
	tmp[0] = now[0] + distance[0]
	tmp[1] = now[1] + distance[1]
	#print "     tmp = ",tmp
	return tmp

	
lines = open("input1.txt").readlines()#データ読み込み
data_num = lines.pop(0)
##print "data_num = ",data_num

treasure_room = [0,0]
treasure_distance = 0
present_room = [0,0]
for line in lines:#データの数だけ回す
	room = map(int, line[:-1].split())#1行のデータをxy座標にする
	##print room
	if room == [0, 0]:#[0, 0]のデータ終了文字だったら結果を出力してリセットする
		print "%d %d"%(treasure_room[0],treasure_room[1])
		treasure_room = [0,0]
		treasure_distance = 0
		present_room = [0,0]
	else:#もし継続だったら
		present_room = go_next(present_room, room)#部屋を進める
		tmp_distance = math.sqrt(present_room[0] ** 2 + present_room[1] ** 2)#その部屋のスタートからのユークリッド距離を出す
		#print "tmp_distance = ",tmp_distance
		if treasure_distance < tmp_distance:#もし今の距離が最大なら宝部屋も更新
			#print "treasure_distance < tmp_distance"
			treasure_room = [present_room[0], present_room[1]]
			treasure_distance = tmp_distance
		elif tmp_distance == treasure_distance:#同じなら部屋のx値が大きいほうが宝部屋
			#print "tmp_distance == treasure_distance"
			if treasure_room[0] < present_room[0]:
				treasure_room = [present_room[0], present_room[1]]
			else:
				pass
		else:
			pass
