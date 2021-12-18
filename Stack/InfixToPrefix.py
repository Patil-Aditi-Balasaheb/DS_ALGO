#############################################################
# Program to convert Infix expression To Prefix expression #
#############################################################

# class for stack
class Stack:
    
    # constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []    # this array is used as a stack
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}    # precedence setting
    
    # check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False
    
    # return the value of the top of stack
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


# class to convert the expression
class Conversion():
    
    # constructor to initialize the class variables
    def __init__(self, capacity):
        self.operand = Stack(capacity)    # creating object of Stack class to store operands
        self.operator = Stack(capacity)   # creating object of Stack class to store operators
    
    # function that converts given infix expression to prefix expression
    def infixToPrefix(self, exp):
        
        # iterate over the expresson for conversion
        for i in exp:
            
            # if the character is an operand then push it into the operands stack
            if self.operand.isOperand(i):
                self.operand.push(i + "")
            
            # if character is an opening bracket, then
            # push into the operators stack
            elif i == '(':
                self.operator.push(i)
            
            # if character is a closing bracket, then
            # pop from both stacks and push result 
            # into the operands stack until matching opening bracket is not found
            elif i == ')':
                while(not self.operator.isEmpty() and self.operator.peek() != '('):
                    # operand 1
                    op1 = self.operand.pops()
                    
                    # operand 2
                    op2 = self.operand.pops()
                    
                    # operator
                    op = self.operator.pops()
                    
                    # Add operands and operator in form:
                    # operator + operand1 + operand2
                    tmp = op + op2 + op1
                    self.operand.push(tmp)
                
                # pop opening bracket from opertors stack
                self.operator.pops()
            
            # if character is an operator, then
            # push it into operators stack after
            # popping high priority operators from operators stack
            # and pushing result in operands stack
            else:
                while(not self.operator.isEmpty() and self.operator.notGreater(i)):
                    # operand 1
                    op1 = self.operand.pops()
                    
                    # operand 2
                    op2 = self.operand.pops()
                    
                    # operator
                    op = self.operator.pops()
                    
                    # Add operands and operator in form:
                    # operator + operand1 + operand2
                    tmp = op + op2 + op1
                    self.operand.push(tmp)
                
                # push the operator in operators stack
                self.operator.push(i)
        
        # pop operators from operators stack until it is empty
        # and operation in add result of each pop operands stack
        while (not self.operator.isEmpty()):
            # operand 1
            op1 = self.operand.pops()

            # operand 2
            op2 = self.operand.pops()

            # operator
            op = self.operator.pops()

            # Add operands and operator in form:
            # operator + operand1 + operand2
            tmp = op + op2 + op1
            self.operand.push(tmp)

        # final prefix expression is present in operands stack
        return self.operand.peek()


# exp = "(A-B/C)*(A/K-L)"
# exp = "A * B + C / D"
# exp = "(A - B/C) * (A/K-L)"
# exp = "G+A+(U-R)^I"

exp = input("Enter Infix Expression: ")

# removing spaces from the expression using replace() or using split() and join() function
# exp = exp.replace(" ","")
exp = "".join(exp.split())

obj = Conversion(len(exp))
print("Prefix Expression:", obj.infixToPrefix(exp))     