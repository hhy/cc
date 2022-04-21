#!/usr/bin/env python
from collections import Counter, defaultdict, deque
from curses import nonl
from functools import lru_cache, reduce, partial
from heapq import heapify
import heapq
import bisect
from itertools import combinations
from random import randint
from re import X
from statistics import median
from typing import Optional, List
import time



def f():
    '''
    given an array of integers nums, there is a sliding window of size k which is moving 
    from the very left of the array to the very right. 
    You can only see the k numbers in the window. Each time the sliding window moves right by one position.

    Return the max sliding window.
    '''
    def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
        q, r=deque(), []
        for i, v in enumerate(nums):
            j=i-k # the min index to stay
            while q and v>nums[q[-1]]: q.pop() # from right to left pop out any value < v
            while q and q[0]<=j: q.popleft() # from left to right, pop out index <= min index that could stay
            q.append(i) 
            if i>=k-1: r.append(nums[q[0]])
        return r

    ii=(([1,3,-1,-3,5,3,6,7], 3, [3,3,5,5,6,7]), ([1], 1, [1]), ([1,-1], 1, [1,-1]), 
    ([7,2,4], 2, [7,4]))
    for ar, k, an in ii[:]:
        r=maxSlidingWindow(ar, k)
        print(f'{r==an}, expect: {an}, get: {r}')


class Solution:
    '''
    Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        # dic  x+y = k,  array (a -> b) = sum(b)-sum(a), each b, find num of a that a+b=k
        r, s, dic=0, 0, {0:1}  
        for i in nums:
            s+=i
            ss=s-k
            if ss in dic: r+=dic[ss]
            if s in dic: dic[s]+=1
            else: dic[s]=1
        return r


class Solution:
    '''
    Given an integer array nums and an integer k, 
    return the length of the shortest non-empty subarray of nums with a sum of at least k.
    If there is no such subarray, return -1
    '''
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        nl=len(nums)
        ss=[0]
        for i in range(nl):
            ss.append(ss[-1]+nums[i])
        ml=nl+nl            
        q=deque()
        for i, v in enumerate(ss):
            while len(q)>0 and v<=q[-1][0]: q.pop()
            while len(q)>0:
                if v-q[0][0]>=k: 
                    ml=min(ml, i-q[0][1])
                    if ml==1: return 1
                    q.popleft()
                else:
                    break
            q.append((v, i))
        return ml if ml<=nl else -1


def f():
    '''
    Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array 
    such that for every two consecutive integers in the subsequence, nums[i] and nums[j],
    where i < j, the condition j - i <= k is satisfied
    '''
    def fa(nums: List[int], k: int) -> int:
        # nums[i] = max(0, nums[i - k], nums[i - k + 1], .., nums[i - 1]) + nums[i]
        # i.e. dp[i] = max(0, dp[i - k], dp[i - k + 1], .., dp[i -1]) + nums[i]
        q=deque()
        nl=len(nums)
        for i in range(nl):
            j=i-k
            if q: nums[i]+=nums[q[0]]
            while q and nums[i]>=nums[q[-1]]: q.pop()
            while q and q[0]<=j: q.popleft()
            if nums[i]>0: q.append(i)
        return max(nums)

    ii=(([10,2,-10,5,20], 2, 37), ( [-1,-2,-3], 1, -1), ([10,-2,-10,-5,20], 2, 23))
    for ar, k, an in ii:
        r=fa(ar, k)
        print(f'{an==r}, expect: {an}, get: {r}')

now=time.time()    
# for i in range(9900): f()
f()
print(f'\n{"="*100}+\ntotal time: {time.time()-now}')