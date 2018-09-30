import crypt
import itertools
import string

salt = '$6$OD/Xgaj9$'
passwd_to_break = '$6$OD/Xgaj9$4sEa6XKEmW12wcphq4cerOegP2fL/fnoGeEcLyiWKBAnash0DQT.ngy9mYI4rusYtW87OvqdFUaGIwCeLtrGp0'


def check_passwd(passwd, salt):
    crypted_passwd = crypt.crypt(passwd, salt)
    print('Crypted password: ', crypted_passwd, '\n')
    if crypted_passwd == passwd_to_break:
        print('Password found: ', passwd, ' !!!')
        return True
    else:
        return False


def search_passwd(passwd, salt):
    for i in range(0, len(passwd) + 1):
        for passwd_combination in itertools.permutations(passwd, i):
            new_passwd_combination = ''.join(passwd_combination)
            print('Password combination: ', new_passwd_combination)
            if (check_passwd(new_passwd_combination, salt)):
                quit()
            else:
                continue
    print('Not found!')


passwd_chars = list(string.ascii_lowercase)
search_passwd(passwd_chars, salt)
