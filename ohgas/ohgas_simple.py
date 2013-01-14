#!/bin/python
#-*-coding:utf-8-*-

def print_info(first_fund, interest_rate, year, commission):
	print 'first_fund = ',first_fund
	print 'interest_rate = ',interest_rate
	print 'year = ',year
	print 'commission =',commission

def calcurate_compound(first_fund, interest_rate, year, commission):
	#print_info(first_fund, interest_rate, year, commission)
	fund = first_fund
	for i in range(year):
		interest = int(interest_rate * fund)
		fund = fund + interest - commission
	return fund
	
def calcurate_simple(first_fund, interest_rate, year, commission):
	#print_info(first_fund, interest_rate, year, commission)
	total_interest = 0
	fund = first_fund
	for i in range(year):
		tmp_interest = int(fund * interest_rate)
		fund = fund - commission
		total_interest += tmp_interest
	return fund + total_interest

class ohga:
	def __init__(self):
		self.first_ope_fund = 0
		self.ope_year = 0
		self.ope_values = 0
		self.ope_procedures = []
		self.balance = []
		
	def set_first_ope_fund(self, money):
		self.first_ope_fund = money
		
	def set_ope_year(self, year):
		self.ope_year = year
		
	def set_ope_values(self, num):
		self.ope_values = num
		
	def print_info(self):
		print 'first_ope_fund =', self.first_ope_fund
		print 'ope_year =', self.ope_year
		print 'ope_values =', self.ope_values
		print 'ope_procedures ='
		print self.ope_procedures
		
	def append_procedur(self, pattern):
		pattern_info = pattern.split(' ')
		self.ope_procedures.append(pattern_info)
	
	def operation(self):
		money = 0
		for i in range(self.ope_values):
			if self.ope_procedures[i][0] == '0':
				money = calcurate_simple(self.first_ope_fund, float(self.ope_procedures[i][1]), self.ope_year, int(self.ope_procedures[i][2]))
			elif self.ope_procedures[i][0] == '1':
				money = calcurate_compound(self.first_ope_fund, float(self.ope_procedures[i][1]), self.ope_year, int(self.ope_procedures[i][2]))
			self.balance.append(money)
		#print 'balance =',self.balance
	def answear(self):
		print max(self.balance)

			
f = open('input.txt')
line = f.readlines()

data_set_num = int(line[0])
data_set_info = line[1:]

index_num = 0
#print data_set_info
for i in range(data_set_num):
	ohga_fund = ohga()
	ohga_fund.set_first_ope_fund(int(data_set_info.pop(0)[:-2]))#pop(0)は頭を取り出す
	ohga_fund.set_ope_year(int(data_set_info.pop(0)[:-2]))
	ohga_fund.set_ope_values(int(data_set_info.pop(0)[:-2]))
	
	for j in range(ohga_fund.ope_values):
		ohga_fund.append_procedur(data_set_info.pop(0)[:-2])
	ohga_fund.operation()
	ohga_fund.answear()
	#ohga_fund.print_info()
	