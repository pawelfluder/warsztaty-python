x = []
y = []

for linia in open('reference.csv'):
    dane = linia.split(',')
    x.append(float(dane[0]))
    y.append(float(dane[1]))
    
liczba_linii = len(x)

# generowanie nowego pliku

plik = open('wynik.csv','w')
plik.write(str(liczba_linii) + "\n")

for indeks in range(liczba_linii):
    linia = '{:.3e};{:.3f}\n'.format(x[indeks],y[indeks])
    plik.write(linia)

plik.close()
