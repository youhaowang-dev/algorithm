# Implement an upper method to convert all characters in a string to uppercase.
# The characters not in alphabet don't need to convert.
# https://www.lintcode.com/problem/146/


class LowercasetoUppercaseII:
    def lowercaseToUppercase2(self, letters: str) -> str:
        converted_letters = []
        for letter in letters:
            if letter.islower:
                converted_letters.append(letter.upper())
            else:
                converted_letters.append(letter)

        return "".join(converted_letters)
