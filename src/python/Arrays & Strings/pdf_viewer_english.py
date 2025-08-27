# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

heights = (1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7)
word = input()
max_h = max(heights[ord(c)-97] for c in word)
print(max_h * len(word))
