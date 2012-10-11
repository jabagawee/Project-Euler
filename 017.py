words = {0: '',
         1: 'one',
         2: 'two',
         3: 'three',
         4: 'four',
         5: 'five',
         6: 'six',
         7: 'seven',
         8: 'eight',
         9: 'nine',
         10: 'ten',
         11: 'eleven',
         12: 'twelve',
         13: 'thirteen',
         14: 'fourteen',
         15: 'fifteen',
         16: 'sixteen',
         17: 'seventeen',
         18: 'eighteen',
         19: 'nineteen',
         20: 'twenty',
         30: 'thirty',
         40: 'forty',
         50: 'fifty',
         60: 'sixty',
         70: 'seventy',
         80: 'eighty',
         90: 'ninety',
         100: 'hundred',
         1000: 'thousand'}


def num_letters(n):
    if n == 1000:
        return len('onethousand')
    if n % 100 == 0:
        return len('hundred') + len(words[n / 100])
    if n > 100:
        return len('hundred') + len(words[n / 100]) + \
                len('and') + num_letters(n % 100)
    if n > 10 and n < 20:
        return len(words[n])
    return len(words[n % 10]) + len(words[n % 100 - n % 10])


def word(n):
    if n == 1000:
        return 'one thousand'
    if n % 100 == 0:
        return words[n / 100] + ' hundred'
    if n > 100:
        return words[n / 100] + ' hundred and ' + word(n % 100)
    if n > 10 and n < 20:
        return words[n]
    return words[n % 100 - n % 10] + ' ' + words[n % 10]

if __name__ == "__main__":
    print sum(num_letters(x) for x in xrange(1, 1000 + 1))
