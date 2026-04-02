class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {} # key is number, value is # of occurences
        for number in nums:
            if numbers.get(number) == None:
                numbers[number] = 1
            else:
                numbers[number] += 1

        # create an array (index will be # of occurrences)
        # array of arrays
        bucket = [[] for _ in range(len(nums)+1)]

        for key in numbers:
            freq = numbers[key]
            bucket[freq].append(key)

        result = []
        counter = 1
        while len(result) < k:
            for num in bucket[-counter]:
                result.append(num)
                if len(result) == k:
                    break
            counter += 1
        return result


