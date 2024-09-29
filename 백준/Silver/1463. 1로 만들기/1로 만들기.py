import sys
from collections import deque
import math
ipt = sys.stdin.readline

nums = dict()
nums[1] = 0
for i in range(1, 1000001):
    if i + 1 not in nums.keys():
        nums[i + 1] = nums[i] + 1
    else:
        nums[i + 1] = min(nums[i + 1], nums[i] + 1)
    if 2 * i not in nums.keys():
        nums[2 * i] = nums[i] + 1
    else:
        nums[2 * i] = min(nums[2 * i], nums[i] + 1)
    if 3 * i not in nums.keys():
        nums[3 * i] = nums[i] + 1
    else:
        nums[3 * i] = min(nums[3 * i], nums[i] + 1)


n = int(ipt())

print(nums[n])
