# soal no 1
def calculate_years(principal, interest, tax, desired):
    year = 0
    while principal < desired :
        principal = principal + ((principal*interest)-((principal*interest)*tax))
        year += 1
    return year

print(calculate_years(1200,0.17,0.05,2000))

# soal no 2
def expandedForm(num):
    strBil = str(num)
    hasil = ''
    for indeks in range(0,len(strBil)):
        nomor = strBil[indeks]
        hasil = hasil + nomor + ((len(strBil)-indeks -1)*str(0)) + ' + '
    print(hasil)

expandedForm(12321332)

# soal no 3
def tower_builder(n_floors, block_size):
    z= ''
    for i in range (0,10,1):
        for j in range (0, 21):
            if j >= 10-i and j <= 10+i:
                z += ' * '
            else: 
                z += '   '    
        z += '\n'
    print (z)       