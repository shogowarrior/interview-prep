# Return Smallest Key

You are given an input dictionary with keys as strings, and values as integers. Complete a function that returns the key with the nth smallest value.

If the solution involves two keys that have the same value, return the the key that is lexicographically earliest.

If n is larger than the number of distinct keys or equal to 0, then return null.

**Signature**
```java
String returnSmallestKey(HashMap<String, Integer> inputDict, int n)
```
**Input**
 - inputDict: Map with a string as the key and integer as the value
 - n: Integer representing the nth smallest value to be returned

**Output**
 - string representing the key

**Examples**
```python
inputDict: {"laptop": 999,"smartphone": 999,"smart tv": 500,"smart watch": 300,"smart home": 9999999}
n: 2 
output: "smart tv" 

inputDict: {"a": 10,"b": 20}
n: 0
output: null

inputDict: {"a": 1,"b": 2,"c": 3,"d": 4,"e": 5}
n: 6 
output: null

inputDict: {"a": 10,"b": 20,"c": 3,"d": 2,"e": 9}
n: 1
output: "d"
```