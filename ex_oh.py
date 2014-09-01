def ex_oh(str_):
    str_ = str_.lower()
    return str_.count('o') == str_.count('x')


print(ex_oh('xoxoox'))
print(ex_oh('oooxoo'))
print(ex_oh('xoxoxoxoxooXox'))