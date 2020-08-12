# soal 1 
def count_words(text):
    split_text = text.split(' ')
    count = len(split_text)
    return f'the number of sentences = {count}'

# print(count_words('Anugrah Nurhamid')) 


# soal 2
def small_enough(myList,parameter):
    
    total = 0
    for iList in myList:
        total += iList
    
    if total > parameter : 
        return False
    else:
        return True

# print(small_enough([20,30,31,11,22,33,57],100))


# soal 3
def remove_duplicate(text):
    new_text = text.lower()
    my_list = new_text.split(' ')
    ln_my_list = len(my_list)
    
    tmp = [] 
    for i in range(ln_my_list):
        if my_list[i] not in tmp:
            tmp.append(my_list[i])
    return ' '.join(tmp)
    # ln_tmp = len(tmp)
    # sentence = ''
    # for j in range(ln_tmp):
    #     sentence += f'{tmp[j]} '
    # return sentence

# print(remove_duplicate('anugrah Nurhamid anugrah nurhamid nurhamid anugrah'))

import math
# soal 4 
def stringify(num):
    tmp = ''  
    if num % 2 == 0:
        for i in range(num//2):
            tmp += '10'
        return tmp
    else:
        p = num/2
        itr = math.ceil(p)
        one = '1'
        for i in range(itr-1):
            one += '0'
            one += '1'
        return one

        
print(stringify(11))

# Soal 5
# def wave(text):

#     iterasi = len(text)
#     kal = [] 
#     for i in range(iterasi):
#         kal.append(text)
#     print(kal)

# print(wave('sindi'))

# gak selesai lagi :'((((((((((((((((((((((((