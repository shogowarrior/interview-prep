# Return Missing Balanced Numbers

A balanced array would be an array in which each element appears the same number of times.

Given an array with n elements, return a dictionary with the key as the element and the value as the count of elements needed to balance the given array.

## Signature

```java
HashMap<Object, Integer> returnMissingBalancedNumbers(Object[] elements)
```

## Input

Array of mixed elements (integers, strings, etc.)

## Output

Object with a mixed key, and an integer value

## xamples

```python
elements: ["a", "b", "abc", "c", "a"]
output: {"b":1, "abc":1, "c":1}

elements: [1,3,4,2,1,4,1]
output: {2:2, 3:2, 4:1}

elements: [4,5,11,5,6,11]
output: {4:1,6:1}

```
