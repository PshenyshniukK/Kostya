email = "aaa@b.ccc"  # True
email2 = email.replace('@', '').replace('.', '')

if email[0].isalpha() and email[0] != '@' and email[-1].isalpha() and email[-1] != '.' and '@' in email and '.' in email and email.index('@') < email.index('.') and "ab12\n\tQ".isascii() and email2.isalnum() and email.count('@') == 1 and email.count('.') == 1:
    print('True')
else:
    print('False')