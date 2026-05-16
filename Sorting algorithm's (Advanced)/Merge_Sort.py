# def merge(arr):
#     if len(arr) <=1:
#         return arr
#     mid = len(arr)//2
#     L = arr[:mid]
#     R = arr[mid:]
#     L = merge(L)
#     R = merge(R)
#     return merge_Sort(L,R)

# def merge_Sort(left,right):
#     new = []
#     i,j = 0,0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             new.append(left[i])
#             i += 1
#         else:
#             new.append(right[j])
#             j += 1
#     new.extend(left[i:])
#     new.extend(right[j:])
#     return new

# arr = [5,34,4,3,2,6,2,5,3]

# a = merge(arr)
# print(a)




class Solution(object):
    def twoSum(self, target):
        self.target = target
        self.nums = [9,4,3,1,5,7,8]

        i = 0

        while i < len(self.nums):
            j = i + 1

            while j < len(self.nums):
                if self.nums[i] + self.nums[j] == target:
                    print(self.nums[i],self.nums[j])
                    return
                else:
                    j += 1
            else:
                i += 1
        else:
            print("No matches")
                        
obj = Solution()
print(obj.twoSum(6))