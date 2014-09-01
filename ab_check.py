def ab_check(str_):
    str_ = str_.lower()
    for i in range(len(str_) - 4):
        if sorted([str_[i], str_[i+4]]) == ['a', 'b']:
            return True
    return False


print(ab_check('after badly'))
print(ab_check('Laura sobs'))
print(ab_check('A   b'))
print(ab_check('Something a babsomething'))
