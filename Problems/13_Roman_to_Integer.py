class Solution(object):
    def romanToInt(self, s):
        # Create an dictionary for the roman numerals and their valules
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        replacements = [
            ("IV", "IIII"),
            ("IX", "VIIII"),
            ("XL", "XXXX"),
            ("XC", "LXXXX"),
            ("CD", "CCCC"),
            ("CM", "DCCCC")
        ]
        # Determines if given roman numeral is within the length and character constraints
        while len(s) == 0 or len(s) > 15:
            s = input("Please enter a roman numeral (1-15 characters long) to determine its value: ")
        # Check if char in given roman numeral are valid roman symbols
        for letter in s:
            if letter not in symbols:
                print("An invalid input was entered. Try again later. Goodbye.")
                break
            # Checks for and replaces any exceptions found within the given roman numeral.
            else:
                for exception, replacement in replacements:
                    s = s.replace(exception, replacement)

                roman_val = 0
                for letter in s:
                    roman_val += symbols[letter]
                return roman_val 
