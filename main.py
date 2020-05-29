def zeroPad(numberString, zeros, left = True):
    for i in range(zeros):
        if left:
            numberString = '0' + numberString
        else:
            numberString = numberString + '0'
    return numberString

def karatsuba(x,y):
  x = str(x)
  y = str(y)

  if(len(x)==1 and len(y)==1):
    return int(x)*int(y)
  if(len(x)>len(y)):
    y = zeroPad(y, len(x) - len(y))
  if(len(y)>len(x)):
    x = zeroPad(x, len(y) - len(x))

  n = len(x)
  m = n // 2
  #handle odds
  if (n % 2) != 0:
    m+=1    
  
  BZeroPadding = n - m
  AZeroPadding = BZeroPadding * 2

  a = int(x[:m])
  b = int(x[m:])
  c = int(y[:m])
  d = int(y[m:])

  ac = a*c
  bd = b*d
  k = recursiveKaratsuba(a + b, c + d)

  A = int(zeroPad(str(ac), AZeroPadding, False))
  B = int(zeroPad(str(k - ac - bd), BZeroPadding, False))

  return A + B + bd

def recursiveKaratsuba(x,y):
  x = str(x)
  y = str(y)

  if(len(x)==1 and len(y)==1):
    return int(x)*int(y)
  if(len(x)>len(y)):
    y = zeroPad(y, len(x) - len(y))
  if(len(y)>len(x)):
    x = zeroPad(x, len(y) - len(x))

  n = len(x)
  m = n // 2
  #handle odds
  if (n % 2) != 0:
    m+=1    
  
  BZeroPadding = n - m
  AZeroPadding = BZeroPadding * 2

  a = int(x[:m])
  b = int(x[m:])
  c = int(y[:m])
  d = int(y[m:])

  ac = recursiveKaratsuba(a,c)
  bd = recursiveKaratsuba(b,d)
  k = recursiveKaratsuba(a + b, c + d)

  A = int(zeroPad(str(ac), AZeroPadding, False))
  B = int(zeroPad(str(k - ac - bd), BZeroPadding, False))

  return A + B + bd

print(karatsuba(1234,4567))
print(recursiveKaratsuba(1234,4567))
print(1234*4567)