#dalej programowanie funkcyjne

#Kolekcje - zbiory - wartości są unikalne
#nawiasy klamrowe jak w słowniku. Dodajemy tylko po jednej wartości
liczby1 = {0, 1, 2, 4, 2}
liczby2 = set() #twotzenie pustego zbioru
print(liczby2)
print(liczby1)

#konwersja listy na zbior
slowa = set(["a", "b", "c", "b"]) #funkcja set to konwertuje
print(slowa)
print("----")
lista = [1,2,3,3,4]
print(f"Lista: {lista}")
print(f"Element listy: {lista[2]}")
print(f"Zbiór: {slowa}")
#Nie da się wypisać tak pojedynczego elementu zbioru
# print(slowa[1])
print("----")

liczby1.add(5)
print(liczby1)
liczby1.remove(0)
print(liczby1)
liczby1.pop() #usuwa pierwszy element
print(liczby1)

#nie doda się 5 ponieważ już istnieje w zbiorze
liczby1.add(5)
print(liczby1)

#funkcja, która sprawdza czy dane wyrażenie jest w zbiorze
print(1 in liczby1)

#Operacje na zbiorach
liczby1 = {0, 1, 2, 3, 4}
liczby2 = {3, 4, 5, 6}

#Logiczna suma
print(liczby1 | liczby2)
#logiczny iloczyn tylko element wspólny
print(liczby1 & liczby2)
# operator różnicy
print(liczby1 - liczby2)
print(liczby2 - liczby1)

#Różnica symetryczna
print("---")
print(liczby1 ^ liczby2)
print(liczby1.symmetric_difference(liczby2))

#część wspólna
print(liczby1.intersection(liczby2))

# wszystkie unikalne wartości
print(liczby1.union(liczby2))

# operator różnicy
print(liczby1.difference(liczby2))