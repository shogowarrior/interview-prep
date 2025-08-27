# Character Frequency
Complete a function that returns the number of times a given character occurs in the given string.

**Note**: Please avoid importing libraries like Counter from collections (if using python) to get the correct solution. The interviewer would like to gauge your experience with initializing/populating dictionaries.

**Tips**: Think about how to solve this without using an imported library, like Counter in collections if using python.

**Signature**
```java
int returnCharNum(string word, char c)
```
**Input**
- **word**: a string
- **c**: a character
- **Note**: Assume that the characters are case sensitive (capital letters are interpreted differently than lower case characters).

**Output**
- An int representing the number of occurrences of the input character (c) in the word.

**Examples**
```shell
word: "Mississippi", c: "s"
output: 4 

word: "Rainbow", c: "j" 
output: 0 

word: "Mirror", c: "m"
output: 0

word: "", c: "c"
output: 0 

word: "hello", c: ""
output: 0
```

