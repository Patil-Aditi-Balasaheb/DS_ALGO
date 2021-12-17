####################################
# Evaluation of Postfix Expression #
####################################

# class to evaluate value of a postfix expression
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
    
    # function that evaluates the given postfix expression
    def evaluatePostfix(self, exp):
        
        # iterate over the expression for conversion
        for i in exp:
            
            # if character is an operand(number) push it to the stack
            if i.isdigit():
                self.push(i)
            
            # if character is an operator,
            # pop two elements from stack and apply it
            else:
                val1 = self.pops()
                val2 = self.pops()
                self.push(str(eval(val2 + i + val1)))
        
        return int(float(self.pops()))


# exp = "100 200 + 2 / 5 * 7 +"
# exp = "231*+9-"

exp = input("Enter a Postfix expression: ")

# splitting the given string to obtain
# integers and operators into a list
# this if is used to identify whether there are single digit numbers 
# or two or more than two digit numbers in a expression
if len(exp.split(' ')) < 2:
    strconv = exp
else:
    strconv = exp.split(' ')

obj = Evaluate(len(strconv))
print("Postfix evaluation: %d" %(obj.evaluatePostfix(strconv)))