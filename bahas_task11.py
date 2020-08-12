def stringify(number):
    hasil = ''
    for item in range(number):
        if item % 2 == 0:
            hasil += '1'
        else:
            hasil += '0'
    return hasil

# print(stringify(11))

def wave(text):
    list_wave = []
    for i in range(len(text)):
        out = ' '
        for j in range(len(text)):
            if i == j :
                out += text[j].upper()
            else:
                out+= text[j]
        list_wave.append(out)
    return list_wave

print(wave('anugrah'))