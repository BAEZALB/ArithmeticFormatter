def arithmetic_arranger(*arg):
    if not( len(arg) == 1 or len(arg) == 2):
      return "Error invalid number of arguments"

    problems = arg[0] 

    expressions = splitProblems(problems)
    
    if type(expressions) == str:
      return expressions

    if(len(arg) == 2 and arg[1] == True):
      arrangedProblems = buildExpressionString(expressions, True)

    else:
      arrangedProblems = buildExpressionString(expressions, False)

    return arrangedProblems


# Pass function list of strings containing arithmetic problems ie ["123 + 345", "321 - 1234"]
# Function checks if string meets specifications outlined:
# No more than 5 problems, each problem must consist of "<positive int> <+ or -> <positive int>"
# Each positive int must be no longer than 4 digits
# Returns string containing error or list of ArithmeticExpression objects if no error

def splitProblems(problems):

  if(len(problems) > 5):
    return "Error: Too many problems."

  expressions = []

  for problem in problems:
    words = problem.split()
    numWords = len(words)
    if numWords != 3:
      return "Error: Improperly formatted expression. Each expression must consist of \"Operand1 Operator Operand 2\""
    
    if not (words[0].isnumeric() and words[2].isnumeric()):
      return "Error: Numbers must only contain digits."

    if not(words[1] == "-" or words[1] == "+"):
      return "Error: Operator must be '+' or '-'."

    if len(words[0]) > 4 or len(words[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    expression = ArithmeticExpression(words[0], words[2], words[1])

    expressions.append(expression)

  return expressions


# function that runs through list of constructed ArithmeticExpression objects and puts
# their data together to produce the horizontal expressions
def buildExpressionString(expressions, printResult):

  arrangedProblems = ""
  i = 0
  numExpressions = len(expressions)

  while i < numExpressions:
    arrangedProblems += expressions[i].getTop()
    if(i + 1 != numExpressions):
      arrangedProblems += "    "
    i += 1

  arrangedProblems += "\n"
  i = 0

  while i < numExpressions:
    arrangedProblems += expressions[i].getBot()
    if(i + 1 != numExpressions):
      arrangedProblems += "    "
    i += 1

  arrangedProblems += "\n"
  i = 0

  while i < numExpressions:
    arrangedProblems += expressions[i].getDashes()
    if(i + 1 != numExpressions):
      arrangedProblems += "    "
    i += 1

  if printResult:
    arrangedProblems += "\n"
    i = 0

    while i < numExpressions:
      arrangedProblems += expressions[i].getResult()
      if(i + 1 != numExpressions):
        arrangedProblems += "    "
      i += 1

  return arrangedProblems

# class container for expressions to contain an operator and the top + bottom operand
# also used to create the horizontal expression line by line
class ArithmeticExpression:
  def __init__ (self, x, y, op):
    self.topOperand = x
    self.botOperand = y
    self.operator = op
    self.result = 0
    self.length = 0

    if(len(x) + 2 > self.length):
      self.length = len(x) + 2
    if(len(y) + 2 > self.length):
      self.length = len(y) + 2

    if self.operator == "+":
      self.result = str(int(self.topOperand) + int(self.botOperand))
    elif self.operator == "-":
      self.result = str(int(self.topOperand) - int(self.botOperand))

  def getTop(self):
    top = ""
    topNumDigits = len(self.topOperand)
    topNumSpaces = self.length - topNumDigits
    i = 0
    while i < topNumSpaces:
      top += " "
      i = i + 1
    top += self.topOperand
    return top
  
  def getBot(self):
    bot = self.operator
    botNumDigits = len(self.botOperand)
    botNumSpaces = self.length - botNumDigits
    i = 1
    while i < botNumSpaces:
      bot += " "
      i = i + 1
    bot += self.botOperand
    return bot

  def getDashes(self):
    dashes = ""
    i = 0
    while i < self.length:
      dashes += "-"
      i += 1
    return dashes

  def getResult(self):
    resultStr = ""

    i = 0
    resultNumDigits = len(self.result)
    resultNumSpaces = self.length - resultNumDigits
    while i < resultNumSpaces:
      resultStr += " "
      i += 1
    resultStr += self.result

    return resultStr