# 1306. Jump Game III

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        stack, visited, n = [start], set(), len(arr)
        while stack:
            i = stack.pop()
            if arr[i] == 0:
                return True
            visited.add(i)
            i1, i2 = i + arr[i], i - arr[i]
            if i1 < n and i1 not in visited:
                stack.append(i1)
            if i2 >=0 and i2 not in visited:
                stack.append(i2)
        return False
        
        