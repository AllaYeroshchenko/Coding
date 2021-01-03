# 13. Roman to Integer


def romanToInt(s: str):
        roman={"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        number=0
        prev=s[-1]
        for symb in s[::-1]:
            print(prev, symb)
            print(number)
            print(roman[prev], roman[symb])
            if roman[prev]>roman[symb]:
                number=number-roman[symb]    
            else:    
                number=number+roman[symb]
            prev=symb[:]  
        return number        
                        
print(romanToInt("IV"))                        