#! /usr/bin/python3

class Solution:
	def maxArea(self,height:List[int]) -> int:
		temp=0
		area=0
		i=0
		j=len(height)-1
		while(i<j):
			if(height[i]>=height[j]):
				temp=height[j]*(j-i)
				j-=1
			else:
				temp=height[i]*(j-i)
                                i+=1
			if(temp>=area):
				area=temp
		return area
