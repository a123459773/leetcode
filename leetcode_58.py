#! /usr/bin/python3

class Solution:
	def lengthOfLastWord(self,s:str) -> int:
		count=0
		for i in range(len(s)-1,-1,-1):
			if(s[i]==" " and count>0):
				return count
			elif(s[i]==" " and count==0):
				count=0
			else:
				count+=1
		return count
