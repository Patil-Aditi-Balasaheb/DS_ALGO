####################################
# Evaluation of Prefix Expression #
####################################

# class to evaluate value of a prefix expression
class Evaluate:
    
    # constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []    # this array is used as a stack
    
    # check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False
    
    # return the value of the top of the stack
    def peek(self):
        return self.array[self.top]
    
    # pop the element from the stack
    def pops(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        
        else:
            return "$"
    
    # push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)
    
    # function that evaluates the given prefix expression
    def evaluatePrefix(self, exp):
        
        # iterate over the expression in reverse order
        for i in exp[::-1]:
            
            # if character is an operand(number) push it to the stack
            if i.isdigit():
                self.push(i)
            
            # if character is an operator,
            # pop two elements from stack and apply it
            else:
                val1 = self.pops()
                val2 = self.pops()
                self.push(str(eval(val1 + i + val2)))
        
        return int(float(self.pops()))


# exp = "+9*26"
# exp = "+ 9 * 12 6"
# exp = "-+8/632"
# exp = "-+7*45+20"

exp = input("Enter a Prefix expression: ")

# splitting the given string to obtain
# integers and operators into a list
# this if is used to identify whether there are single digit numbers 
# or two or more than two digit numbers in a expression
if len(exp.split(' ')) < 2:
    strconv = exp
else:
    strconv = exp.split(' ')

obj = Evaluate(len(strconv))
print("Prefix evaluation: %d" %(obj.evaluatePrefix(strconv)))