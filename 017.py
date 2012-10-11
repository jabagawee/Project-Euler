words = dict(zip((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1000), ('', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 'thousand')))

def num_letters(n):
    if n == 1000:
        return len('onethousand')
    if n % 100 == 0:
        return len('hundred') + len(words[n/100])
    if n > 100:
        return len('hundred') + len(words[n/100]) + len('and') + num_letters(n%100)
    if n > 10 and n < 20:
        return len(words[n])
    return len(words[n%10]) + len(words[n%100-n%10])

def word(n):
    if n == 1000:
        return 'one thousand'
    if n % 100 == 0:
        return words[n/100] + ' hundred'
    if n > 100:
        return words[n/100] + ' hundred and ' + word(n%100)
    if n > 10 and n < 20:
        return words[n]
    return words[n%100-n%10] + ' ' + words[n%10]
        

ans = 0
for x in xrange(1, 1000+1):
    ans += num_letters(x)

print ans
