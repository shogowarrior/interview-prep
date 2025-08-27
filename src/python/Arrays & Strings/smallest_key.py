def return_smallest_key(inputDict, n):
  if n<=0 or n>len(inputDict):
    return None

  outputDict = {}
  outputList = sorted({v: outputDict.get(v, []) + [k] for k, v in inputDict.items()}.items())

  # Sort values in smallest key
  smallestKey = sorted(outputList[n-1][1])

  # Return 1st sorted
  return smallestKey[0]
  

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printValue(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printValue(expected)
    print(' Your output: ', end='')
    printValue(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  
  # Testcase 1 
  inputDict1 = {"laptop": 999,"smartphone": 999,"smart tv": 500,"smart watch": 300,"smart home": 9999999}
  n1 = 2
  expected_1 = "smart tv"
  output_1 = return_smallest_key(inputDict1, n1)
  check(expected_1, output_1)
  
  # Testcase 2 
  inputDict2 = {"a": 10,"b": 20}
  n2 = 0
  expected_2 = None
  output_2 = return_smallest_key(inputDict2, n2)
  check(expected_2, output_2)
  
  # Testcase 3 
  inputDict3 = {"a": 1,"b": 2,"c": 3,"d": 4,"e": 5}
  n3 = 6 
  expected_3 = None 
  output_3 = return_smallest_key(inputDict3, n3)
  check(expected_3, output_3)

  # Testcase 4
  inputDict4 =  {"a": 10,"b": 20,"c": 3,"d": 2,"e": 9}
  n4 = 1 
  expected_4 = "d" 
  output_4 = return_smallest_key(inputDict4, n4)
  check(expected_4, output_4)

  # Testcase 5
  inputDict5 =  {"a": 10,"b": 20,"c": 3,"d": 2,"e": 9}
  n5 = 20
  expected_5 = None 
  output_5 = return_smallest_key(inputDict5, n5)
  check(expected_5, output_5)

  # Testcase 6
  inputDict5 =  {"a": 10,"b": 10,"d": 20,"c": 20,"e": 40}
  n5 = 2
  expected_5 = "c"
  output_5 = return_smallest_key(inputDict5, n5)
  check(expected_5, output_5)  
  