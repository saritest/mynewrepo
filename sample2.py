#! /usr/bin/python


def getLength(str):
  return len(str)
  
def testGetLength():
  str = 'Hello'
  if getLength(str) == 5:
    return True
  else:
    return False
    
def main():
  print testGetLength()
  
if __name__ == "__main__":
  main()
