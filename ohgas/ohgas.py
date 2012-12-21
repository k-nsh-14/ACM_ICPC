#!/bin/python
#-*-coding:utf-8-*-

class ohga:
	def __init__(self):
		self.first_ope_fund = 0
		self.ope_year = 0
		self.ope_values = 0
		#ope_procedures = []
	def set_first_ope_fund(self, money):
		self.first_ope_fund = money
	def set_ope_year(self, year):
		self.ope_year = year
	def set_ope_values(self, num):
		self.ope_values = num
		self.ope_procedures = []
	def print_info(self):
		print 'first_ope_fund =', self.first_ope_fund
		print 'ope_year =', self.ope_year
		print 'ope_values =', self.ope_values
		

f = open('input.txt')
line = f.readlines()

data_set_num = int(line[0])
data_set_info = line[1:]

index_num = 0
print data_set_info
for i in range(data_set_num):
	ohga_fund = ohga()
	ohga_fund.set_first_ope_fund(int(data_set_info.pop(0)[:-2]))#pop(0)は頭を取り出す
	ohga_fund.set_ope_year(int(data_set_info.pop(0)[:-2]))
	ohga_fund.set_ope_values(int(data_set_info.pop(0)[:-2]))
	ohga_fund.print_info()
	for j in range(ohga_fund.ope_values):
		print data_set_info.pop(0)[:-2]
	