class Solution:
    mem = {n: n for n in range(2)}

    def main(self, num: int) -> int:
        # f(n) = f(n-1) + f(n-2); f(0) = 0; f(1) = 1

        if num in self.mem:
            return self.mem[num]
        else:
            self.mem[num] = self.main(num - 1) + self.main(num - 2)
            return self.mem[num]


if __name__ == "__main__":
    sol = Solution()
    print(sol.main(num=20))
