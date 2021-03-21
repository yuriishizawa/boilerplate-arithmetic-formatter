def arithmetic_arranger(problems, b=False):
    arranged_problems = None
    
    if len(problems) > 5:
        arranged_problems = 'Error: Too many problems.'
        return arranged_problems
    
    for prob in problems:
      if prob.split()[1] != '+' and prob.split()[1] != '-':
         arranged_problems = 'Error: Operator must be \'+\' or \'-\'.'
         return arranged_problems
            
      for j in [0,-1]:
        if prob.split()[j].isdigit() and len(prob.split()[j]) <= 4:
            pass
        elif len(prob.split()[j]) > 4:
            arranged_problems = 'Error: Numbers cannot be more than four digits.'
            return arranged_problems
        else:
          arranged_problems = 'Error: Numbers must only contain digits.'
          return arranged_problems
    l1 = []      
    l2 = []
    l3 = []
    l4 = []
    a1 = []
    a2 = []

    for prob in problems:
        a1.append(int(prob.split()[0]))
        a2.append(int(prob.split()[1] + prob.split()[2]))
    results = [x + y for (x,y) in zip(a1,a2)] 

    for i,prob in enumerate(problems):
      if b != 1:
        pass
      else:
        l4.append(str(results[i]).rjust(2+max([len(prob.split()[0]),len(prob.split()[2])])))
        if prob != problems[-1]:
            l4.append("    ") 
      l1.append(prob.split()[0].rjust(2+max([len(prob.split()[0]),len(prob.split()[2])])))
      l2.append(prob.split()[1])
      l2.append(prob.split()[2].rjust(1+max([len(prob.split()[0]),len(prob.split()[2])])))
      l3.append('-'*(max([len(prob.split()[0]),len(prob.split()[2])])+2))
      if prob == problems[-1]:
          break 
      l1.append("    ")
      l2.append("    ")     
      l3.append("    ")

    l1.append("\n")
    l2.append("\n")
    if b == 1:
      l3.append("\n")
    arranged_problems = ''.join(l1 + l2 + l3 + l4)    

    return arranged_problems