def arithmetic_arranger(problems, val=False):

  arranged_problems = ''
  if len(problems) > 5:
    arranged_problems = "Error: Too many problems."
    return arranged_problems

  numbers = []
  for i in problems :
    p = i.split()
    num1 = p[0]
    operator = list(map(lambda x: x.split()[1], problems))
    num2 = p[2]
    numbers.extend([p[0], p[2]])
    
    if set(operator) != {'+', '-'} and len(set(operator)) != 1:
        arranged_problems = "Error: Operator must be '+' or '-'."
        return arranged_problems
    
    if len(num1) > 4 or len(num2) > 4 :
        arranged_problems = "Error: Numbers cannot be more than four digits."
        return arranged_problems
        
    if not all(map(lambda x: x.isdigit(), numbers)):
        arranged_problems = "Error: Numbers must only contain digits."
        return arranged_problems

  top = ''
  dash = ''
  values = list(map(lambda x: eval(x), problems))
  answer = ''
  for i in range(0, len(numbers), 2):
        space = max(len(numbers[i]), len(numbers[i+1])) + 2
        top = top + numbers[i].rjust(space)
        dash = dash + '-' * space
        answer += str(values[i // 2]).rjust(space)
        if i != len(numbers) - 2:
            top = top + ' ' * 4
            dash = dash + ' ' * 4
            answer = answer + ' ' * 4

  bottom = ''
  for i in range(1, len(numbers), 2):
        space = max(len(numbers[i - 1]), len(numbers[i])) + 1
        bottom = bottom + operator[i // 2]
        bottom = bottom + numbers[i].rjust(space)
        if i != len(numbers) - 1:
            bottom += ' ' * 4

  if val:
        arranged_problems = '\n'.join((top, bottom, dash, answer))
  else:
        arranged_problems = '\n'.join((top, bottom, dash))
  return arranged_problems        
