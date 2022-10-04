class Solution:
    def reverse(self, x: int) -> int:
        digit = 0
        reversed_list = []
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x != 0:
            if x >= 0:
                reversed_list.append(x % 10)
                x //= 10
                digit += 1
        for n in range(digit, 0, -1):
            reversed_list[digit - n] *= (10 ** (n - 1))
        result = sign * sum(reversed_list)
        return 0 if result <= -2**31 or result >= 2**31 -1 else result


solution = Solution()
x_rev = solution.reverse(1534236469)
print(x_rev)
