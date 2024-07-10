#2 Viết function mô phỏng theo 3 activation function.
import math
def is_number(n):
  try:
    float (n)
  except ValueError:
    return False
  else:
    return True

def exercise2():
  x = input("Input x =")
  if not is_number(x):
    print("x must be a number")
    return
  func_name = input("Input activation Function ( sigmoid | relu | elu ) :")
  if func_name not in "sigmoid|relu|elu".split("|"):
    print(f"{func_name} is not supportted")
    return

  x = float(x)

  if func_name == "sigmoid":
    print(f"sigmoid: f({x}) = {1/(1+math.exp(-x))}")
  elif func_name == "relu":
    print(f"relu: f({x}) = {max(0,x)}")
  else:
    alpha = 0.01
    print(f"elu: f({x}) = {x if x>0 else alpha*(math.exp(x)-1)}")

exercise2()