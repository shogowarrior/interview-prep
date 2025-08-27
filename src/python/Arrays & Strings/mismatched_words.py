from collections import Counter

def update_list_1(list1, list2):
  output = []
  for word in list1:
    if word not in list2:
      output.append(word)
  for word in list2:
    if word not in list1:
      output.append(word)
  return output


def update_list_2(list1, list2):
  output = list1 + list2
  word_count = Counter(output)
  output = [word for word in output if word_count[word] == 1]
  print(output)
  return output


def return_mismatched_words(str1, str2): 
  # Split string into tokens
  str1_list = str1.split(" ")
  str2_list = str2.split(" ")

  output_1 = update_list_1(str1_list, str2_list)
  output_2 = update_list_2(str1_list, str2_list)
  if output_1 == output_2:
    print("Both methods are equal")
    return output_1
  return output_2


def printStringList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printStringList(expected)
    print(' Your output: ', end='')
    printStringList(output)
    print()
  test_case_number += 1
    
if __name__ == "__main__":
  # Testcase 1
  str1 = "Firstly this is the first string"
  str2 = "Next is the second string" 
  output_1 = return_mismatched_words(str1, str2)
  expected_1 = ["Firstly", "this", "first", "Next", "second"]
  check(expected_1, output_1)

  # Testcase 2
  str1 = "This is the first string"
  str2 = "This is the second string" 
  output_2 = return_mismatched_words(str1, str2)
  expected_2 = ["first", "second"]
  check(expected_2, output_2)
  
  # Testcase 3
  str1 = "This is the first string extra"
  str2 = "This is the second string" 
  output_3 = return_mismatched_words(str1, str2)
  expected_3 = ["first", "extra", "second"]
  check(expected_3, output_3)
  
  # Testcase 4
  str1 = "This is the first text"
  str2 = "This is the second string" 
  output_4 = return_mismatched_words(str1, str2)
  expected_4 = ["first", "text", "second", "string"]
  check(expected_4, output_4)
  
  
  # Add your own test cases here