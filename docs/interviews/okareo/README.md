# Okareo Interview - Dice Consistency Check

A six-sided dice is thrown repeatedly with results recorded as int[]. Each time we can only see three sides - top, front, right (bottom, left, back are hidden).

The visible sides are recorded in the order top, front, right. So for example [1,2,3] is top = 1, front = 2, and right = 3. Each side could be a number 1 to 50.

Multiple throws are recorded as [ [1,2,3], [1,3,6], [1,25,45]...]

We need to check that these historical throws data is consistent with respect to a single six-sided dice.

Write a method consistent(throws list[list[int]]) → int. The method returns 1 based index of the first entry in throws history that is inconsistent with respect to previous ones. If all the historical data is consistent the method should return 0.

## Solution

See [dice.py](dice.py) for the implementation and test cases.
