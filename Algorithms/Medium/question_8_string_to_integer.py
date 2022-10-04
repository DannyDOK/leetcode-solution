class Solution:
    def myAtoi(self, s: str) -> int:
        sign_dict = {"-": -1,
                     "+": 1}

        sign = 1
        num_list = []
        sign_read = False
        digit_read = False

        for c in s:
            if c.isnumeric():
                digit_read = True
                num_list.append(c)
            else:
                if sign_dict.get(c) is not None:
                    if digit_read:
                        break
                    sign = sign_dict.get(c)
                    sign_read = True
                    sign_dict.clear()
                elif c == " ":
                    if digit_read or sign_read:
                        break
                    pass
                else:
                    break

        if not num_list:
            num_list.append("0")

        try:
            result = sign * int(''.join(num_list))
            if sign == 1:
                return min(result, 2 ** 31 - 1)
            else:
                return max(result, -2 ** 31)
        except:
            return 0




solution = Solution()
parsed_int = solution.myAtoi("  asdf  -413")
print(parsed_int)
# print(int(''.join([])))