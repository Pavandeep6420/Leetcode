class Solution:
    def intToRoman(self, num: int) -> str:
        # List of value-symbol pairs in descending order, including subtractive combinations
        val_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        res = []
        for val, symbol in val_map:
            if num == 0:
                break
            count, num = divmod(num, val)
            res.append(symbol * count)
            
        return "".join(res)