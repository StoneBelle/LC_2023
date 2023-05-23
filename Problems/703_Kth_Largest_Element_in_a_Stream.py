class KthLargest(object):
    def __init__(self, k, nums):
        # Create attributes for passed in arguments
        # i.e. kth largest element, & stream
        self.largest_num = k
        self.stream = nums

    def add(self, val):
        # Append all new values to stream
        self.stream.append(val)
        
        # Sort updated stream
        self.stream.sort()

        # Traverse k times from back of list         
        return self.stream[-self.largest_num]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
