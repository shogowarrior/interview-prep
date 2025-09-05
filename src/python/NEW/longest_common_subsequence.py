from utils import assert_custom, print_test_index


# recursive
def helper(self, s1, s2, i, j):
    if i == len(s1) or j == len(s2):
        return 0
    if s1[i] == s2[j]:
        return 1 + self.helper(s1, s2, i + 1, j + 1)
    else:
        return max(self.helper(s1, s2, i + 1, j), self.helper(s1, s2, i, j + 1))


# recursive with memoization
def longestCommonSubsequence(self, s1: str, s2: str) -> int:
    m = len(s1)
    n = len(s2)
    memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
    return self.helper(s1, s2, 0, 0, memo)

    def helper(self, s1, s2, i, j, memo):
        if memo[i][j] < 0:
            if i == len(s1) or j == len(s2):
                memo[i][j] = 0
            elif s1[i] == s2[j]:
                memo[i][j] = 1 + self.helper(s1, s2, i + 1, j + 1, memo)
            else:
                memo[i][j] = max(
                    self.helper(s1, s2, i + 1, j, memo),
                    self.helper(s1, s2, i, j + 1, memo),
                )
                return memo[i][j]


def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
    for i, c in enumerate(text1):
        for j, d in enumerate(text2):
            dp[i + 1][j + 1] = (
                1 + dp[i][j] if c == d else max(dp[i][j + 1], dp[i + 1][j])
            )
    return dp[-1][-1]


def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
    m, n = map(len, (text1, text2))
    if m < n:
        text1, text2 = text2, text1
    dp = [0] * (n + 1)
    for c in text1:
        prevRow, prevRowPrevCol = 0, 0
        for j, d in enumerate(text2):
            prevRow, prevRowPrevCol = dp[j + 1], prevRow
            dp[j + 1] = prevRowPrevCol + 1 if c == d else max(dp[j], prevRow)
    return dp[-1]


def longestCommonSubsequence3(self, text1: str, text2: str) -> int:
    m, n = map(len, (text1, text2))
    if m < n:
        text1, text2 = text2, text1
    dp = [0] * (n + 1)
    for c in text1:
        prevRow, prevRowPrevCol = 0, 0
        for j, d in enumerate(text2):
            prevRow, prevRowPrevCol = dp[j + 1], prevRow
            dp[j + 1] = prevRowPrevCol + 1 if c == d else max(dp[j], prevRow)
    return dp[-1]


test_cases = [
    {"text1": "abcde", "text2": "ace", "expected": 3},
    {"text1": "abc", "text2": "abc", "expected": 3},
    {"text1": "ababccde", "text2": "def", "expected": 0},
]


for index in range(len(test_cases)):
    print_test_index(index)
    test_case = test_cases[index]
