import cs50
import sys

def main():
  if len(sys.argv) != 2:
    print("Not valid key! Program shut down")
    exit(1)
  
  k = int(sys.argv[1])
  if k == 0:
    print("Not valid key! Program shut down")
    exit(1)
    
  print("Plaintext:  ", end = "")
  text = cs50.get_string()
  ciphertext = ''
  print("Ciphertext: ", end = "")
  l = len(text)
  for i in range(l):
    if text[i].isalpha() != True:
      ciphertext += text[i]
    else:
      if text[i].islower() != True:
        letter = iflarge(k, text[i])
        ciphertext += letter
      else:
        letter = ifsmall(k, text[i])
        ciphertext += letter
  
  print("{}".format(ciphertext))
  
def iflarge(k, letter):
  letter = ord(letter)
  letter -= 65
  letter = (letter + k) % 26
  letter += 65
  return chr(letter)
  
def ifsmall(k, letter):
  letter = ord(letter)
  letter -= 97
  letter = (letter + k) % 26
  letter += 97
  return chr(letter)
  
if __name__ == "__main__":
  main()