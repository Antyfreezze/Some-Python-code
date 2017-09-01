import cs50

def main():
  i = get_pos()
  build(i)

def build(i):
  h = 2
  s = i - 1
  for n in range(i):
    left = ' ' * s + '#' * h
    right = '#' * h + ' ' * s
    line = left + '  ' + right
    if n == 0:
      s -= 1
      h += 1
    else:
      s -= 1
      h += 1
    print("{}".format(line))

def get_pos():
  while True:
    i = cs50.get_int()
    if i > 0 and i < 24:
      return i

if __name__ == "__main__":
  main()