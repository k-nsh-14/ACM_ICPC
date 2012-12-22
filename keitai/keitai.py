#!/bin/python
#-*-coding:utf-8-*-


one   = ['.',',','!','?',' ']
two   = ['a','b','c']
three = ['d','e','f']
four  = ['g','h','i']
five  = ['j','k','l']
six   = ['m','n','o']
seven = ['p','q','r','s']
eight = ['t','u','v']
nine  = ['w','x','y','z']
dict = [one,two,three,four,five,six,seven,eight,nine]


def decode(code):
	return_str = ''
	tmp_letter = ''
	count = 0
	for letter in code: 
		if letter is '0':
			return_str += tmp_letter
			tmp_letter = ''
			count = 0
		else:
			button_list = dict[int(letter)-1]
			tmp_letter = button_list[count%len(button_list)]
			count += 1
	return return_str

inputs = open('input.txt').readlines()

text_num = int(inputs.pop(0))
for i in range(text_num):
	print decode(inputs.pop(0)[:-2])