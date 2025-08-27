# Colorful Numbers

Objective: Given a number, find out whether it is colorful.

Colorful Number: When in a given number, the product of every contiguous sub-sequence is different. That number is called a Colorful Number. 

## Example 1:
```
Given Number : 3245
Output: Colorful

Number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
this number is a colorful number, since product of every digit of a sub-sequence are different.
That is, 3 2 4 5 (3*2)=6 (2*4)=8 (4*5)=20, (3*2*4)= 24 (2*4*5)= 40
```

## Example 2:

```
Given Number : 326
Output: Not Colorful.

326 is not a colorful number as it generates 3 2 6 (3*2)=6 (2*6)=12.
```

## Approach

The idea is to get the product of all possible subarrays and keep storing it in a Set, if any time the current subarray product is already in a Set, return false, else at the end return true 

Read - Print all subarrays of a given array Video - https://www.youtube.com/watch?v=xHwMaxq2Qxo

## Steps

1. Initialize a Set
2. Get the length of the number (number of digits)
3. Use Two nested loops, 
4. The first loop sets the starting point of the subarray and the second loop will decide the length of the subarray. This will give one of the possible subarrays, get the product, and check if the product already exists in Set. If yes, then return false, the number is not colorful.
5. If done with iterations, and all products are added to Set, that means no two subarrays have the same product, return true since the number is colorful