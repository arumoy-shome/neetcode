class Solution:
    DELIM = "#"

    def encode(self, strs: list[str]) -> str:
        res = ""
        counts = [len(s) for s in strs]

        for c, s in zip(counts, strs):
            res = res + str(c) + self.DELIM + s

        return res

    def decode(self, s: str) -> list[str]:
        res = []

        i = 0
        while i < len(s):
            j = i
            while s[j].isnumeric() and s[j] != self.DELIM:
                j += 1
            length = int(s[i:j])

            start = j + 1
            end = start + int(s[i])
            res.append(s[start:end])

            i += 1

        return res


if __name__ == "__main__":
    strs = ["hello", "world"]
    strs = ["hello", "world", "ne#et", "says"]
    strs = ["we", "say", ":", "yes", "!@#$%^&*()"]
    sol = Solution()
    print(sol.decode(sol.encode(strs)))
