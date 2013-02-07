# -*- coding:utf-8 -*-


def travel(room_info, point):
	next_pattern = [[1,0],[0,1],[-1,0],[0,-1]]
	print point[0]," , ",point[1]
	if room_info[point[0]][point[1]] != "#":
		travel_list.append(point)
		for next in next_pattern:
			next_point = (point[0]+next[0], point[1]+next[1])
			if 0 <= next_point[0] < 9 and 0 <= next_point[1] < 6 and next_point not in travel_list:
				travel(room_info, next_point)
			else:
				pass
	else:
		pass
	return 0
travel_list = []
count = 0
a = [['.', '.', '.', '.', '#', '.'], ['.', '.', '.', '.', '.', '#'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['#', '@', '.', '.', '.', '#'], ['.', '#', '.', '.', '#', '.']]

#try:
travel(a,(7,1))
#except Exception as e:
#    print e.message
print len(travel_list)   
print '処理終了'