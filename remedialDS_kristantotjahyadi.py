# soal no 1
def find_short(s):
    tampungan = []
    kata = str(s)
    splitKata = (kata.split(' '))
    for i in splitKata:
        tampungan.append(len(i))
    tampungan.sort()
    return print(tampungan[0])

find_short('Many people get up early in the morning')
find_short('Every office would getting newest monitor')
find_short('Create new file after this morning')

# soal no 2
def persistence(n):
    z = 1
    y = 0
    angka = list(str(n))
    while len(angka) > 1:
        for i in angka:
            z *= int(i)
        y += 1
        angka = list(str(z))
        z = 1
    return print(y)

persistence(39)
persistence(999)
persistence(4)

# soal no 3
def multiplication_table(row,col):
    tampungan_1 = []
    tampungan_2 = []
    z = ''
    for i in range (col):
        tampungan_2.append(i+1)
    for j in range (row):
        tampungan_1.append(list(map(lambda num: num * (j+1), tampungan_2)))
    for k in range (row):
        for l in range (col):
            z += ' {} '.format(str(tampungan_1[k][l]))
        z += '\n'
    return print(z)

multiplication_table(3,3)
multiplication_table(5,3)
multiplication_table(3,5)

# soal no 4
def alphabet_position(text):
    z = ''
    for i in range(len(text)):
        if text[i] == 'a' or text[i] == 'A':
            z += str(1)
            z += ' '
        elif text[i] == 'b' or text[i] == 'B':
            z += str(2)
            z += ' '
        elif text[i] == 'c' or text[i] == 'C':
                z += str(3)
                z += ' '
        elif text[i] == 'd' or text[i] == 'D':
            z += str(4)
            z += ' '
        elif text[i] == 'e' or text[i] == 'E':
            z += str(5)
            z += ' '
        elif text[i] == 'f' or text[i] == 'F':
            z += str(6)
            z += ' '
        elif text[i] == 'g' or text[i] == 'G':
                z += str(7)
                z += ' '
        elif text[i] == 'h' or text[i] == 'H':
            z += str(8)
            z += ' '
        elif text[i] == 'i' or text[i] == 'I':
            z += str(9)
            z += ' '
        elif text[i] == 'j' or text[i] == 'J':
            z += str(10)
            z += ' '
        elif text[i] == 'k' or text[i] == 'K':
                z += str(11)
                z += ' '
        elif text[i] == 'l' or text[i] == 'L':
            z += str(12)
            z += ' '
        elif text[i] == 'm' or text[i] == 'M':
            z += str(13)
            z += ' '
        elif text[i] == 'n' or text[i] == 'N':
            z += str(14)
            z += ' '
        elif text[i] == 'o' or text[i] == 'O':
                z += str(15)
                z += ' '
        elif text[i] == 'p' or text[i] == 'P':
            z += str(16)
            z += ' '
        elif text[i] == 'q' or text[i] == 'Q':
            z += str(17)
            z += ' '
        elif text[i] == 'r' or text[i] == 'R':
            z += str(18)
            z += ' '
        elif text[i] == 's' or text[i] == 'S':
                z += str(19)
                z += ' '
        elif text[i] == 't' or text[i] == 'T':
            z += str(20)
            z += ' '
        elif text[i] == 'u' or text[i] == 'U':
            z += str(21)
            z += ' '
        elif text[i] == 'v' or text[i] == 'V':
            z += str(22)
            z += ' '
        elif text[i] == 'w' or text[i] == 'W':
                z += str(23)
                z += ' '
        elif text[i] == 'x' or text[i] == 'X':
            z += str(24)
            z += ' '
        elif text[i] == 'y' or text[i] == 'Y':
            z += str(25)
            z += ' '
        elif text[i] == 'z' or text[i] == 'Z':
            z += str(26)
            z += ' '
        else:
            z += ''
    
    return print('" ' + z + '"')
          
alphabet_position("The sunset sets at twelve o'clock.")
alphabet_position("it's never too late to try")
alphabet_position("Have you done your homework?")

# soal tambahan
def prima(num):
    prima = True
    for bil in range(2, num//2 +1):
        if num % bil == 0:
            prima = False
            break
    return prima
def is_prime(num):
    if prima(num):
        print('True')
    else:
        print('False')

is_prime(5099)


