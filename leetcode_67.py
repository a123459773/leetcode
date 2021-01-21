#! /usr/bin/python3
class Solution:
	def addBinary(self,a:str,b:str) -> str:
		temp=""
		carry="0"
		if(len(a)>=len(b)):
			while(len(a)>len(b)):
				b="0"+b
		else:
			while(len(b)>len(a)):
				a="0"+a
		for i in range(len(a)-1,-1,-1):
			if(a[i]=="1"and b[i]=="1"):
				if(carry=="1"):
					carry="1"
					c="1"
				else:
					carry="1"
					c="0"
			elif((a[i]=="0"and b[i]=="0")and carry=="0"):
				carry="0"
				c="0"
			elif((a[i]=="1"and carry=="1")or (b[i]=="1"and carry=="1")):
				carry="1"
				c="0"
			else:
				carry="0"
				c="1"
			temp+=c
		if(carry=="1"):
			temp+=carry
		return temp[::-1]
