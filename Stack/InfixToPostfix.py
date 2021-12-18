#############################################################
# Program to convert Infix expression To Postfix expression #
#############################################################

# class to convert the expression
class Conversion:

    # constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []     # this array is used as a stack to store operators
        self.output = []    # this array is for the postfix expression
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}   # precedence setting
    
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
    
    # function to check if the given character is operand
    def isOperand(self, ch):
        return ch.isalpha()
    
    # check if the precedence of operator is strictly
    # less than top of stack or not
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False
    
    # function that converts given infix expression to postfix expression
    def infixToPostfix(self, exp):

        # iterate over the expression for conversion
        for i in exp:

            # if character is an operand add it to output
            if self.isOperand(i):
                self.output.append(i)
            
            # if character is an '(', push it to stack
            elif i == '(':
                self.push(i)
            
            # if character is an ')', pop from the stack 
            # until '(' is found and add it to output
            elif i == ')':
                while((not self.isEmpty()) and self.peek() != '('):
                    self.output.append(self.pops())
                
                if(not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pops()
            
            # if character is an operator
            else:
                while((not self.isEmpty()) and self.notGreater(i)):
                    self.output.append(self.pops())
                self.push(i)
        
        # pop all the operator from the stack
        while not self.isEmpty():
            self.output.append(self.pops())
        
        return "".join(self.output)
            

# exp = "a+b*(c^d-e)^(f+g*h)-i"
# exp = "( A + B ) * C"
# exp = "A + B * C / D - E"
# exp = "( A + B * ( C - D ) ) / E"

exp = input("Enter Infix Expression: ")

# removing spaces from the expression using replace() or using split() and join() function
# exp = exp.replace(" ","")
exp = "".join(exp.split())

obj = Conversion(len(exp))
print("Postfix Expression:", obj.infixToPostfix(exp))