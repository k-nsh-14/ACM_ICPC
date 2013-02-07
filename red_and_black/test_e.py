# -*- coding:utf-8 -*-


def travel(room_info, point):
	next_pattern = [[1,0],[0,1],[-1,0],[0,-1]]
	print point[0]," , ",point[1]
	travel_list.append(point)
	#print a[point[0]][point[1]]
	
	for next in next_pattern:
		next_point = (point[0]+next[0], point[1]+next[1])
		if 0 <= next_point[0] < 3 and 0 <= next_point[1] < 3 and next_point not in travel_list:
		#	next_point = (point[0]+next[0], point[1]+next[1])

			travel(room_info, next_point)
		else:
			pass
		#count += 1
		#if count == 100:
		#	break
	return 0
travel_list = []
count = 0
a = [[1,2,3],[4,5,6],[7,8,9]]
#try:
travel(a,(1,1))
#except Exception as e:
#    print e.message
    
print '処理終了'