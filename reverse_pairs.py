# -*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(100000)

class Solution:
    def InversePairs(self, data):
        # write code here
        if (len(data) < 0) or (data==None):
            return 0
        copy = data
        count = self.InversePairsCount(data, copy, 0, len(data)-1)
        return count
    
    def InversePairsCount(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        length = (start + end) >> 1
        
        left = self.InversePairsCount(copy, data, start, start+length)
        right = self.InversePairsCount(copy, data, start+length+1, end)
        
        i = start + length
        j = end
        index_copy = end
        count = 0
        
        while(i>=start and j>=start+length+1):
            if data[i] > data[j]:
                i -= 1
                index_copy -= 1
                copy[index_copy] = data[i]
                count += j-start-length
            else:
                index_copy -= 1
                j -= 1
                copy[index_copy] = data[j]
        
        while i >= start:
            index_copy -= 1
            i -= 1
            copy[index_copy] = data[i]
        while j >= start+length+1:
            index_copy -= 1
            j -= 1
            copy[index_copy] = data[j]
        return left+right+count
