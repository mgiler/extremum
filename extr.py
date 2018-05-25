import numpy as np


def funkcja1(x, y):
    return -(x + 3) ** 2 - (y - 2) ** 2 + 7


print("Extremum funkcji =" + str(funkcja1(-3, 2)))

# krok 1 algorytmu wybranie punktu poczatkowego

x0 = np.array([0, 0])
xMin = x0
xMax = x0

# krok 2 zbiór kierunków

directions = np.array([[1, 0], [0, 1], [-1, 0], [0, -1]])

# krok 3 poczatek petli algorytmu

print("Wynik w punkcie startowym: " + str(funkcja1(x0[0], x0[1])))

results = np.array([0, 0, 0, 0])


def maximum(x, y):
    counter = 0
    for i in directions:
        currentX = y + i
        x[counter] = funkcja1(currentX[0], currentX[1])
        counter += 1
    return results.argmax()


def minimum(x, y):
    counter = 0
    for i in directions:
        currentX = y + i
        x[counter] = funkcja1(currentX[0], currentX[1])
        counter += 1
    return results.argmin()


terminatorMax = 0
while True:
    currentResult = maximum(results, xMax)
    step = directions[currentResult]
    tmp = xMax + step
    if funkcja1(tmp[0], tmp[1]) > funkcja1(xMax[0], xMax[1]):
        xMax = tmp
        # print(str(xMax) + str(results[currentResult]))
        terminatorMax += 1
        if terminatorMax >= 1000:
            print("Nie ma minimum")
            break
    else:
        print("Maximum to: " + str(funkcja1(xMax[0], xMax[1])) + " w punkcie: " + str(xMax))
        break

terminatorMin = 0
while True:
    currentResult = minimum(results, xMin)
    step = directions[currentResult]
    tmp = xMin + step
    if funkcja1(tmp[0], tmp[1]) < funkcja1(xMin[0], xMin[1]):
        xMin = tmp
        # print(str(xMin) + str(results[currentResult]))
        terminatorMin += 1
        if terminatorMin >= 1000:
            print("Nie ma minimum")
            break
    else:
        print("Minimum to: " + str(funkcja1(xMin[0], xMin[1])) + " w punkcie: " + str(xMin))
        break

# print("Wynik po petli: " + str(results))

# liczba = 10
#
# liczba2 = int(input("podaj liczbe"))
#
# print("twoja liczba:" + str(liczba2 + liczba))
# if liczba2 == 2:
#     print("git")
#
# else:
#     print("źle")
#
#
# def przyklad(w, d):
#     for y in range(w, d):
#         print("twój " + str(y))
#
#
# przyklad(10, 20)*/
