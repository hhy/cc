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



now=time.time()    
# for i in range(9900): f()
f()
print(f'\n{"="*100}+\ntotal time: {time.time()-now}')