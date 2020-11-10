class Soloution:
    """
    字符串中的单词数
    """

    def countSegments(self, s):
        res = 0
        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
                res += 1
        return res


if __name__ == "__main__":
    s = Soloution()
    n = "Hello, My name is Jiaozn"
    print("输入：", n)
    print("输出：", s.countSegments(n))