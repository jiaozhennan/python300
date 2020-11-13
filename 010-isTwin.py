class Solution:
    def isTwin(self, s, t):
        if len(s) != len(t):
            return "No"
        oddS = []
        evenS = []
        oddT = []
        evenT = []
        for i in range(len(s)):
            if i & 1:
                oddS.append(s[i])
                oddT.append(t[i])
            else:
                evenS.append(s[i])
                evenT.append(t[i])
            oddS.sort()
            oddT.sort()
            evenS.sort()
            evenT.sort()
            for i in range(len(oddS)):
                if oddS[i] != oddT[i]:
                    return "No"
            for i in range(len(evenS)):
                if evenS[i] !=evenT[i]:
                    return "No"
            return "Yes"


if __name__ == '__main__':
    s = "abcd"
    t = "cdab"
    solution = Solution()
    print("s 与 t 分别为：", s, t)
    print("是否是双胞胎：", solution.isTwin(s, t))
