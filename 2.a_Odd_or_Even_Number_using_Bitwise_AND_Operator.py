#Program to check whether a given number a odd or a even number

def isEven(num):
  return not num&1

if __name__ == "__main__":
  num = 14
  if isEven(num):
    print('Even')
  else:
    print('Odd')