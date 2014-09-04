def dash_insert(num):
    str_ = str(num)
    i = len(str_) - 1
    while i > 0:
        if int(str_[i]) % 2 != 0 and int(str_[i-1]) % 2 != 0:
            str_ = str_[:i] + '-' + str_[i:]
        i -= 1
    return str_

print(dash_insert(99977))
print(dash_insert(56730))
print(dash_insert(9994643004975902345703457))
print(dash_insert(567300475927450745207540235442))