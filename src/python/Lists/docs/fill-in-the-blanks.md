# Fill in the Blanks
Given an array containing null values fill in the null values with most recent non-null value in the array.
**Signature**
```java
integer[] returnFilledArray(integer[] input_lst)
```

**Input**
Array of integers and/or null values

**Output**
Array of integers and/or null values

**Examples**
```python
input:  [1,null,2,3,null,null,5,null]
output: [1, 1, 2, 3, 3, 3, 5, 5]

input: [null,8,null]
output: [null, 8, 8]

input: [1,null,2]
output: [1,1,2]

input: [5,null,null]
output: [5,5,5]

input: [1,null,2,3,null,null,5,null]
output: [1,1,2,3,3,3,5,5]
```