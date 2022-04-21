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

def f():
    '''
    nums and an integer limit, return the size of the longest non-empty subarray
    such that the absolute difference between any two elements of this subarray is less than or equal to limit
    '''
    def longestSubarray(nums: List[int], limit: int) -> int:
        qa, qb=[], []
        r, m=0, -1
        for i, v in enumerate(nums):
            heapq.heappush(qa, (v, -i))
            heapq.heappush(qb, (-v, -i))
            if -qa[0][0]-qb[0][0]>limit:
                m=-max(qa[0][1], qb[0][1])
                while qa[0][1]>=-m: heapq.heappop(qa)
                while qb[0][1]>=-m: heapq.heappop(qb)
            r=max(r, i-m)

        return r

    
    
    def longestSubarray(A, limit):

        # This is a monotonically decreasing double-ended queue. 
        maxd = deque()

        # This is a monotonically increasing double-ended queue.

        
        mind = deque()

        i = 0
        for j in range(len(A)):
            # At each iteration, we maintain the biggest elements in maxd.
            # Remove any element smaller than A[j]
            while len(maxd) and A[j] > maxd[-1]: maxd.pop()

            # At each iteration, we maintain the smallest elements in mind.
            # Remove any element bigger than A[j]
            while len(mind) and A[j] < mind[-1]: mind.pop()

            # Why do we always add A[j] ?
            # As we will see below, we may have to remove an element(may be A[j-1] if i was j-1) 
            # from the beginning of the maxd/mind.
            # After that, we still need to know the max/min numbers from A[i/i+1]...A[j]
            maxd.append(A[j])
            mind.append(A[j])

            # maxd holds the biggest elements from A[i]...A[j] in decreasing order.
            # So maxd[0] is the biggest element in the window A[i]...A[j]
            # mind holds the smallest elements from A[i]...A[j] in increasing order.
            # So mind[0] is the smallest element in the window A[i]...A[j]
            # maxd[0]-mind[0] is the biggest difference in the window A[i]...A[j]
            if maxd[0] - mind[0] > limit:
                # The biggest difference is over the limit; so remove A[i] from the window.
                # Why do we check only maxd[0]/mind[0] to remove A[i]?
                # Take maxd as an example. In order for A[i] to be present in maxd, 
                # A[i] >= A[x], where x = i+1...j. In other words, it has to be the biggest element or 
                # it would have already been removed. The biggest element would be in maxd[0]. 
                # Similar explanation applies for mind.
                if maxd[0] == A[i]: maxd.popleft()
                if mind[0] == A[i]: mind.popleft()
                # The new window for consideration is A[i+1]...A[j].
                i += 1

            # At every iteration of j, the window size for consideration is from A[i..j]. Its size is j+1-i.
            # At every iteration, an element is added to the window and possibly removed only if the window contains
            # elements with max difference > limit.
            # So the window size only grows monotonically but never shrinks in size. The window grows only if all the elements in
            # the window satisfy the max difference <= limit.
            # Therefore, the last window size in the iteration(when j=len(A)-1) holds the maximum size of the window with max diff <= limit.
            # However, it must be noted that the window in consideration at the last iteration may not really be the window
            # which has the max diff <= limit.
            # This doesn't matter since all we are interested in is the window size and not really the elements in the window.
            return len(A) - i


            # The lazy update using if instead of while is brilliant.
            # Once you reach a new better interval, 
            # you just keep the current best interval between i and j and keep sliding, 
            # even when it slides to a window that failed the limit requirement. Later, 
            # when it slides to a better interval, 
            # no pop happens and i won't increase but j will increase and you get a new better interval. 
            # Finally, it slides to the end of the input vector, and j - i is exactly the answer we need.

    ii=(([8,2,4,7], 4, 2), ([10,1,2,4,7,2], 5, 4), ([4,2,2,2,4,4,2,2], 0, 3), ([1,1,1,2,3,4], 99, 6))
    for ar, k, an in ii[:]:
        r=longestSubarray(ar, k)
        print(f'{an==r}, expect: {an}, get: {r}')


class Solution:
    '''
    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
    There is only one repeated number in nums, return this repeated number.
    '''
    def findDuplicate(self, nums: List[int]) -> int:
 
        a, b, c=0, 0, 0
        while True:
            a, b=nums[a], nums[nums[b]]
            if a==b: break
        while True:
            a, c=nums[a], nums[c]
            if a==c: return a

class Solution:
    '''
    Given an unsorted integer array nums, return the smallest missing positive integer.
    '''
    def firstMissingPositive(self, nums: List[int]) -> int:
        nl=len(nums)
        m=nl*4+111
        for i in range(nl):
            v=nums[i]
            if v<1 or v>nl: nums[i]=m
        for i in range(nl):
            v=abs(nums[i])
            if v==m or v==-m: continue
            nums[v-1]=-abs(nums[v-1])
        for i, v in enumerate(nums):
            if v>0: return i+1
        return nl+1

now=time.time()    
# for i in range(9900): f()
f()
print(f'\n{"="*100}+\ntotal time: {time.time()-now}')


import math
class Solution:
    '''
    cost of min MST for given an array points representing integer coordinates of some points on a 2D-plane
    '''
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        lp=len(points)
        es=[]
        ps=set([i for i in range(lp)])
        s=0
        p=0
        while True:
            a, b=points[p]
            ps.remove(p)
            if len(ps)==0: return s
            for j in ps:
                c, d=points[j]
                heapq.heappush(es,  (abs(a-c)+abs(b-d), j) )
            while p not in ps: e, p=heapq.heappop(es)
            s+=e

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        h=[]
        lp=len(points)
        dist=[math.inf for x in range(lp)]
        ps=set([x for x in range(lp)])
        p=0
        s=0
        while True:
            a, b=points[p]
            ps.remove(p)
            if len(ps)==0: return s
            for x in ps:
                c,d=points[x]
                dd=abs(a-c)+abs(b-d)
                if dd<dist[x]: dist[x]=dd
            d=math.inf
            for i in ps:
                if d>dist[i]: p, d=i, dist[i]
            s+=d