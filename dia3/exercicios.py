from sre_constants import SUCCESS


def list_nums(n: int):
    numbers = []
    for i in range(1, n+1):
        if(i % 3 == 0 and i % 5 == 0):
            numbers.append('FizzBuzz')
        elif(i % 5 == 0):
            numbers.append('Buzz')
        elif(i % 3 == 0):
            numbers.append('Fizz')
        else: numbers.append(i)
    return numbers


#print(list_nums(30))

def encrypt_phrase(string):
    phrase = ''

    if not 1 < len(string) <= 30:
        raise ValueError("Expression with invalid length")

    for letter in string.upper():
        if (letter in 'ABC'):
            phrase += '2'
        elif (letter in 'DEF'):
            phrase += '3'
        elif (letter in 'GHI'):
            phrase += '4'
        elif (letter in 'JKL'):
            phrase += '5'
        elif (letter in 'MNO'):
            phrase += '6'
        elif (letter in 'PQRS'):
            phrase += '7'
        elif (letter in 'TUV'):
            phrase += '8'
        elif (letter in 'WYXZ'):
            phrase += '9'
        elif (letter in '0-1'):
            phrase += letter
        else:
            raise ValueError("Invalid character")

    return phrase


#print(encrypt_phrase('The quick brown fox jumps over the lazy dog'))


def email_verify(email):
    stringList = email.split('@')
    name_user = stringList[0]
    website = stringList[1].split('.')
    website_name = website[0]
    extension = website[1]
    test_email = True
    
    for letter in name_user:
        if (not name_user[0].isalpha()):
            raise ValueError('O primeiro caracter tem que ser uma letra')
            test_email = False
        elif (not letter.isalpha() and not letter.isnumeric() and letter not in ('-', '_')):
            raise ValueError('O nome do usuário deve conter apenas letras, dígitos, traços ou underscore')
            test_email = False

    for letter in website_name:
        if (letter.isalpha() == False and letter.isnumeric() == False):
            raise ValueError('O nome do website deve conter somente letras e dígitos')
            test_email = False

    if (len(extension) > 3):
        raise ValueError('O tamanho máximo da extensão é de 3 caracteres.')
        test_email = False

    return test_email


#print(email_verify('1andre@gmail.com'))

def verify_list_emails(array: list):
    response = []
    for email in array:
        if (email_verify(email) == True):
            response.append(email)


    return response


print(verify_list_emails(["nome#@dominio.com", "outro@dominio.com"]))