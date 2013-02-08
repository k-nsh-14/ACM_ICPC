#-*-coding:utf-8-*-
import sys

input = open(sys.argv[1]).readlines()

for l in input:
	print l[:-1]