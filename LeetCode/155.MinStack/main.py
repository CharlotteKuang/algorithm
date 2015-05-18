from Solution import MinStack 

def main():
	minStack = MinStack()
	minStack.push(1)
	print minStack.top()
	print minStack.getMin() 
	minStack.push(2)
	print minStack.top()
	print minStack.getMin() 
	minStack.push(0)
	print minStack.top()
	print minStack.getMin() 
	minStack.pop()
	print minStack.top()
	print minStack.getMin() 

main()
