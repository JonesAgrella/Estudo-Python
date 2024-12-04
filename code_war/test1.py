def maskify(cc):
    txt = ''
    accountant = 0
    for letter in cc:
        if accountant < (len(cc) - 4):
            accountant += 1
            letter = '#'
            txt += letter
        else:
            txt += letter
    return txt

print(maskify('joaovictoragrella'))
