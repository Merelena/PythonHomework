class NumberConverter:
    numbers = {
        3000:'MMM',
        2000:'MM',
        900:'CM',
        800:'DCCC',
        700:'DCC',
        600:'DC',
        500:'CDC',
        400:'CD',
        300:'CCC',
        200:'CC',
        90:'XC',
        80:'LXXX',
        70:'LXX',
        60:'LX',
        50:'XLX',
        40:'XL',
        30:'XXX',
        20:'XX',
        11:'XI',
        10:'IXI',
        9:'IX',
        8:'VIII',
        7:'VII',
        6:'VI',
        5:'IVI',
        4:'IV',
        3:'III',
        2:'II',
        1000:'M',
        500:'D',
        100:'C',
        50:'L',
        10:'X',
        5:'V',
        1:'I'
    }

    def convert_to_integer(self, number: str) -> int:
        result = 0
        while number:
            for key, value in self.numbers.items():
                if value in number:
                    result += key
                    number = number.replace(value, "")
        return result

    def convert_to_roman(self, number: int) -> str:
        n = 10 ** (len(str(number)) - 1)
        result = ''
        while n != 1:
            if number == number % n:
                n /= 10
                continue
            result += self.numbers[number - number % n]
            number %= n
            n /= 10
        result += self.numbers[number]
        return result


c = NumberConverter()
roman = c.convert_to_roman(2049)
print(roman)