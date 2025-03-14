# Leetcode 370.  Range Addition
# This problem introduces you to the concept of a "difference array"
# This allows you to take the sum of subarrays in O(1) time


def prefix_sum(l: list[int]):
    for i in range(len(l) - 1):
        l[i + 1] += l[i]


def calculate_difference_array(length: int, updates: list[list[int]]) -> list[int]:
    diff = [0] * length

    for start, end, inc in updates:
        diff[start] += inc
        if end + 1 < length:
            diff[end + 1] -= inc

    return diff

def getModifiedArray(length: int, updates: list[list[int]]) -> list[int]:
    diff = calculate_difference_array(length, updates)
    prefix_sum(diff)
    
    return diff


def getModifiedArray_02(l: list[int], updates: list[list[int]]) -> list[int]:
    diff = [0] * len(l)

    for start, end, inc in updates:
        diff[start] += inc
        if end + 1 < len(l):
            diff[end + 1] -= inc

    prefix_sum(diff)
    for i, val in enumerate(l):
        l[i] = val + diff[i]

    return l


def main() -> None:
    print(getModifiedArray(length=5, updates=[[1,  3,  2], [2,  4,  3], [0,  2, -2]])) # [-2, 0, 3, 5, 3]
    print(getModifiedArray(5, [[1,3,2],[2,4,3]])) # [0, 2, 5, 5, 3]
    print(getModifiedArray_02([15, 10, 5, 20, 40], [[1, 3, 10], [1, 4, 5]])) # [15, 25, 20, 35, 45]



if __name__ == '__main__':
    main()
