#4. Viết 4 functions để ước lượng các hàm số sau.
def factorial(n):
  assert n>=0, "n must be greater than or equal zero"
  if n==0 or n==1:
    return 1
  for i in range(n-1,0,-1):
    n*=i
  return n

def approx_sin(x,n):
  sin=0
  for i in range(n+1):
    sin+=(-1)**i*x**(2*i+1)/factorial(2*i+1)
  print(sin)

def approx_cos(x,n):
  cos=0
  for i in range(n+1):
    cos+=(-1)**i*x**(2*i)/factorial(2*i)
  print(cos)

def approx_sinh(x,n):
  sinh=0
  for i in range(n+1):
    sinh+=x**(2*i+1)/factorial(2*i+1)
  print(sinh)

def approx_cosh(x,n):
  cosh=0
  for i in range(n+1):
    cosh+=x**(2*i)/factorial(2*i)
  print(cosh)

approx_sin(x =3.14, n =10)
approx_cos(x =3.14, n =10)
approx_sinh(x =3.14, n =10)
approx_cosh(x =3.14, n =10)
