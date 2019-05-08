#Eliezer Martinez
Math4330Project - Part 1

def ScaVecMulti(scalar, vector01):
  """
    This function takes a vector an a scalar as it’s arguments, and then it multiplies each element of the vector by the scalar, updating each element of the vector. 
  """  
  vector = [] #brackets for the answer 
  for i in range(len(vector01)):
    total = 0
    total += vector01[i] * scalar #multiplies each element of the vector by the scalar
    vector.append(total) #put the total inside the new vector
  return vector

def VecSub(vector01, vector02):
  """
    This function takes two vectors as its arguments, then it updates each of the elements inside the vector by subtracting them, returning a new updated vector.
  """
  VecSub = [] #brackets for the answer 
  for i in range(len(vector01)):
    total = 0 
    total += vector01[i] - vector02[i] #substract each element individually from each vector
    VecSub.append(total) #adds the total in the brackets
  return VecSub

def dot(vector01, vector02):
  """
    This function takes two vectors as its arguments. It multiplies each element of each vector before adding them, and returning the dot product of two 
    vectors as a scalar.
  """
  total = 0 #perform an addition 
  for i in range(len(vector01)):
    total += vector01[i] * vector02[i] #multiplies each element of the vector by each other before adding them to return a scalar
  return total


def norm(vector):
  """
  The two norms takes a vector as it's arguments, to compute the sum of the squares of each element of the vector, returning the square root of the sum.
  """
  total = 0
  for i in range(len(vector)):
    total += vector[i] ** 2 #squares each element of the vector
  total = total**(1/2) #takes the sqaure root of the sum
  return total

def normalize(vector):
  """
  This function takes the infinity norm and uses it to normalize a vector, Returning a normalize vector with respect to the infinity norm.
  """
  normalizer = []
  for i in range(len(vector)):
    total = 0
    total += vector[i] * (1 / norm(vector)) #the vector its divided by the two norm
    normalizer.append(total)
  return normalizer  


A = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00], [0.3025, 0.36, 0.4225, 0.49, 0.5625, 0.64, 0.7225, 0.81, 0.9025, 1], [0.166375, 0.216, 0.274625, 0.343, 0.421875, 0.512, 0.614125, 0.729, 0.857375, 1]]

y = [1.102, 1.099, 1.017, 1.111, 1.117, 1.152, 1.265, 1.380, 1.575, 1.857]

def GramSchmidt(A):
  """
  The modified Gram-Schmidt algorithm takes a comlimn vector inside a matrix and computes orthonormal vectors. Q and R are returned after being substracted from the original matrix
  """

  n = len(A)
  m = len(A[0])
  Q = [[0] * m for i in range(n)]
  R = [[0] * n for i in range(n)]
  v = [[0] * m for i in range(n)]
  # Dimention of R and Q must match for the multiplication

  for i in range(n):
    v[i] = A[i]
  for i in range(n):
    R[i][i] = norm(v[i])
    # Taking two norm
    Q[i] = normalize(v[i])
    # normalizing 
    for j in range(i + 1, n):
      R[i][j] = dot(Q[i],v[j])
      # dot product 
      temp = ScaVecMulti(R[i][j], Q[i])
      # vector scalar multiplication
      v[j] = VecSub(v[j],temp)
      # vector substraction
  return [Q, R]
QR = GramSchmidt(A)

Q = QR[0] 
R = QR[1] 

'''
def trans(Q):
  m = len(Q)
  n = len(Q[0])
  new = [[0] * m for i in range(n)]
  for i in range(len(Q)):
    for j in range(len(Q[0])):
      new[j][i] = Q[i][j]
  return new
QT = trans(Q)
'''

def transmatvecMulti(Q, y):
  '''
This functions uses Matrix Q and Vector y as the arguments, to multiply them together. Q should have been transformed. Matrix multiplication was used because of the orientation of my matrix. It is made of rows, not columns, so Q can be used because it is made of a column vector.
  '''  
  if len(Q) != len(y):
    print('invalid input')
  if len(Q[0]) != len(y):
    print('invalid input')

  new = [] 
  for i in range(len(Q)):
    product = 0 # before the for statement to avoid addition
    for j in range(len(y)):
      product += Q[i][j] * y[j]
    new.append(product) #appends product inside the bracket
  return new
b = transmatvecMulti(Q, y)

def backsub(R, b):
  '''
This function takes vector R and b, and returns unknown c. backwards substitution finds the unknown starting from the last unknown, in order to find the next unknown.
  '''
  if len(R) != len(b):
    print('invalid input')

  a = len(b) - 1
  c = [0] * len(b)
  c[a] = b[a] / R[a][a]
  for i in range(a, 0, -1):
    c[i] = b[i]
    for j in range(i +1, a):
      c[i] = c[i] - c[j]*R[j][i]
      c[i] = c[i] / R[i][i]
  return c
print(backsub(R, b))
