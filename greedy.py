import cs50

def main():
  print("O hai! How much change is owned?")
  n = get_num()
  s = change(n)
  print("{}".format(s))
  exit(0)
  
def get_num():
  while True:
    n = cs50.get_float()
    if n >= 0:
      return n
      
def change(n):
  n *= 100
  s = 0
  while n != 0:
    if n >= 25:
      n -= 25
      s += 1
    elif n >= 10:
      n -= 10
      s += 1
    elif n >= 5:
      n -= 5
      s += 1
    elif n >= 1:
      n -= 1
      s += 1
  return s
  
if __name__ == "__main__":
  main()