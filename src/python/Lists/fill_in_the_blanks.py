import math
# Add any extra import statements you may need here

def fill_in_the_blanks(input_list):
  latest_char = None
  for i in range(0, len(input_list)):
    if input_list[i] is not None:
      latest_char = input_list[i]
    else:
      input_list[i] = latest_char
      
  return input_list


test_case_number = 1
def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', expected, sep='', end='')
    print(' Your output: ', output, end='')
    print()
  test_case_number += 1

if __name__ == "__main__":

  # Testcase 1
  input_lst_1 = [1,None,2,3,None,None,5,None]
  output_1 = fill_in_the_blanks(input_lst_1)
  expected_1 = [1, 1, 2, 3, 3, 3, 5, 5]
  check(expected_1, output_1)
  

  # Testcase 2
  input_lst_2 = [None, 8, None]
  output_2 = fill_in_the_blanks(input_lst_2)
  expected_2 = [None, 8, 8]
  check(expected_2, output_2)


  # Testcase 3
  input_lst_3 = [1,None,2]
  output_3 = fill_in_the_blanks(input_lst_3)
  expected_3 = [1, 1, 2]
  check(expected_3, output_3)
  

  # Testcase 4
  input_lst_4 = [5, None, None]
  output_4 = fill_in_the_blanks(input_lst_4)
  expected_4 = [5, 5, 5]
  check(expected_4, output_4)
  
  # Add your own test cases here
  