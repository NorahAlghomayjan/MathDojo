# Create a MathDojo class

# Write the add method and test it by calling it 3 times, with different numbers of arguments each time

# Write the subtract method and test it by calling it 3 times, with different numbers of arguments each time

# Make sure you are able to chain methods as demonstrated above


from os import pread


class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        for i in nums:
            self.result += i
        self.result += num
        return self
        # your code here
    def subtract(self, num, *nums):
        for i in nums:
            self.result -= i
        self.result -= num
        return self
        # your code here
# create an instance:
md = MathDojo()
md2 = MathDojo()
md3 = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
x = md2.add(2,3,4,5,6,7).result
print(x)
x = md3.subtract(3).result
print(x)
# run each of the methods a few more times and check the result!

