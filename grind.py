import math

# ================================================================
#                             Jour 1
# ================================================================

# Retourne la valeur true
def returnTrue() -> bool:
  return None

# Retourne le paramètre donné en entrée
def returnParam(param: int) -> int:
  return None

# Retourne vrai si param est strictement supérieur à 5
# Retourne faux sinon
def isBiggerThan5(param: int) -> bool:
  return None

# Retourne vrai si param est faux
# Retourne faux si param est vrai
def invertBoolean(param: bool) -> bool:
  return None

# ================================================================
#                             Jour 2
# ================================================================

# Retourne la somme des paramètres a b et c, le tout multiplié par 5
def sumTimes5(a: int, b: int, c: int) -> int:
  return None

# Retourne vrai si a ET b sont strictement supérieurs à 5 et strictement inférieurs à 10
# Retourne faux sinon
def areBetween5And10(a: int, b: int) -> bool:
  return None

# ================================================================
#                             Jour 3
# ================================================================

# Si la somme des paramètres est paire, retourner le carré de a.
# Sinon, retourner le cube de b.
def parityComputing(a: int, b: int) -> int:
  return None

# Ajouter n fois la lettre letter au mot word
# Retourner la chaîne de caractères résultante
def addLetters(word: str, letter: str, n: int) -> str:
  return None

# ================================================================
#                             Jour 4
# ================================================================

# Retourne le chiffre des centaines d'un nombre
# (exemple: 5120 -> 1)
# Retourne 0 si le nombre est inférieur à 100
def getHundreds(a: int) -> int:
  return None

# Retourne la somme de tous les éléments du tableau
def sumArray(a: list[int]) -> int:
  return None

# ================================================================
#                             Jour 5
# ================================================================

# Retourne le plus grand nombre contenu dans le tableau
def maxArray(a: list[int]) -> int:
  return None

# Diviser b par 2 et ajouter 5 à a tant que a est inférieur à b
# Une fois que a est strictement supérieur à b, retourner la somme de a et b.
def balanceParams(a: int, b: int) -> int:
  return None

# ================================================================
#                             Jour 6
# ================================================================

# Retourne vrai si le nombre b se trouve dans le tableau a
# Retourne faux sinon
def isNumberInArray(a: list[int], b: int) -> bool:
  return None

# Retourne vrai si la somme des nombres pairs est strictement supérieure
# à la somme des nombres impaires contenus dans le tableau
def biggerTotalOfEvenNumbers(a: list[int]) -> bool:
  return None

# ================================================================
#                             Jour 7
# ================================================================

# Détecte s'il y a une collision entre deux rectangles.
# Un rectangle est représenté par un tableau contenant dans l'ordre :
# - Sa position en x
# - Sa position en y
# - Sa longueur
# - Sa largeur
# Il y a collision si ces deux rectangles se touchent ou se superposent
def isCollisionDetected(rectA: list[int], rectB: list[int]) -> bool:
  return None

# Retourne la somme des matrices a et b (toujours de mêmes dimensions)
def matrixAddition(a, b):
  return None

# ================================================================
#                             Jour 8
# ================================================================

# Un joueur de Mastermind a formulé un certain nombre de propositions pour deviner le code gagnant.
# answer est une ligne de chiffres représentant la combinaison gagnante
# attempts est un tableau de lignes de chiffres, représentant toutes les combinaisons essayées par le joueur
# La fonction retourne vrai si la ligne answer se trouve dans attempts et faux sinon
def mastermind(answer: list[int], attempts: list[int]) -> bool:
  return None

# ================================================================
#                             Jour 9
# ================================================================

# La racine numérique d'un nombre est l'addition de tous ses chiffres
# récursivement jusqu'à ce qu'ils ne donnent qu'un seul chiffre
# (exemple : 598 -> 5+9+8 = 22 -> 2+2 = 4)
def digitalRoot(a: int) -> int:
  return None

# ================================================================
#                             Jour 10
# ================================================================

# Une chaîne est une suite de plusieurs entiers consécutifs croissants (exemple : 5-6-7-8)
# Retourne un tableau contenant les sommes des différentes chaînes contenues dans le tableau
# (exemple : [1, 2, 7, 4, 5, 6] retourne [3, 15] car il y a deux chaînes : 1-2 et 4-5-6)
def chainSums(a: list[int]) -> list[int]:
  return None

# ================================================================================================================================
#                                                                                                                                #
#                                                      Load functions                                                            #
#                                                                                                                                #
# ================================================================================================================================
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
# ======================================== Day 1 ========================================
print('==================== Day 1 ====================')
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if True == returnTrue() else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'returnTrue()',
  [True, returnTrue()]
)

print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if 5 == returnParam(5) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'returnParam()',
  [5, returnParam(5), 5]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if -12 == returnParam(-12) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'returnParam()',
  [-12, returnParam(-12), -12]
)

print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if True == isBiggerThan5(8) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'isBiggerThan5()',
  [True, isBiggerThan5(8), 8]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if False == isBiggerThan5(-15) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'isBiggerThan5()',
  [False, isBiggerThan5(-15), -15]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if False == isBiggerThan5(5) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'isBiggerThan5()',
  [False, isBiggerThan5(5), 5]
)

print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if False == invertBoolean(True) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'invertBoolean()',
  [False, invertBoolean(True), True]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if True == invertBoolean(False) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'invertBoolean()',
  [True, invertBoolean(False), False]
)

# ======================================== Day 2 ========================================
print()
print('==================== Day 2 ====================')
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if 25 == sumTimes5(-5, 2, 8) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'sumTimes5()',
  [25, sumTimes5(-5, 2, 8), -5, 2, 8]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if 50 == sumTimes5(5, 5, 0) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'sumTimes5()',
  [50, sumTimes5(5, 5, 0), 5, 5, 0]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if 0 == sumTimes5(12, 28, -40) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'sumTimes5()',
  [0, sumTimes5(12, 28, -40), 12, 28, -40]
)

print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if True == areBetween5And10(7, 8) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'areBetween5And10()',
  [True, areBetween5And10(7, 8), 7, 8]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if False == areBetween5And10(2, 6) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'areBetween5And10()',
  [False, areBetween5And10(2, 6), 2, 6]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if False == areBetween5And10(8, 10) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'areBetween5And10()',
  [False, areBetween5And10(8, 10), 8, 10]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if True == areBetween5And10(9, 6) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'areBetween5And10()',
  [True, areBetween5And10(9, 6), 9, 6]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if False == areBetween5And10(5, 6) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'areBetween5And10()',
  [False, areBetween5And10(5, 6), 5, 6]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if False == areBetween5And10(9, 5) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'areBetween5And10()',
  [False, areBetween5And10(9, 5), 9, 5]
)

# ======================================== Day 3 ========================================
print()
print('==================== Day 3 ====================')
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if 25 == parityComputing(5, 7) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'parityComputing()',
  [25, parityComputing(5, 7), 5, 7]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if 3375 == parityComputing(14, 15) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'parityComputing()',
  [3375, parityComputing(14, 15), 14, 15]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if 1 == parityComputing(-1, 1) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'parityComputing()',
  [1, parityComputing(-1, 1), -1, 1]
)

print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if "algoooo" == addLetters("algo", "o", 3) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'addLetters()',
  ["algoooo", addLetters("algo", "o", 3), "algo", "o", 3]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if "bb" == addLetters("", "b", 2) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'addLetters()',
  ["bb", addLetters("", "b", 2), "", "b", 2]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if "Lucky 777" == addLetters("Lucky ", "7", 3) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'addLetters()',
  ["Lucky 777", addLetters("Lucky ", "7", 3), "Lucky ", "7", 3]
)

# ======================================== Day 4 ========================================
print()
print('==================== Day 4 ====================')
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if 8 == getHundreds(822) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'getHundreds()',
  [8, getHundreds(822), 822]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if 1 == getHundreds(4125) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'getHundreds()',
  [1, getHundreds(4125), 4125]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if 0 == getHundreds(1024) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'getHundreds()',
  [0, getHundreds(1024), 1024]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if 0 == getHundreds(5) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'getHundreds()',
  [0, getHundreds(5), 5]
)

print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if 5 == sumArray([1, 1, 1, 1, 1]) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'sumArray()',
  [5, sumArray([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1]]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if 0 == sumArray([2, -2, 2, -2]) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'sumArray()',
  [0, sumArray([2, -2, 2, -2]), [2, -2, 2, -2]]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if 45 == sumArray([1, 2, 3, 4, 5, 6, 7, 8, 9]) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'sumArray()',
  [45, sumArray([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9]]
)

# ======================================== Day 5 ========================================
print()
print('==================== Day 5 ====================')
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if 12 == maxArray([10, 8, 12, 6, 4]) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'maxArray()',
  [12, maxArray([10, 8, 12, 6, 4]), [10, 8, 12, 6, 4]]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if 20 == maxArray([10, -30, 20]) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'maxArray()',
  [20, maxArray([10, -30, 20]), [10, -30, 20]]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if -2 == maxArray([-3, -2, -8, -7]) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'maxArray()',
  [-2, maxArray([-3, -2, -8, -7]), [-3, -2, -8, -7]]
)

print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if 8.5 == balanceParams(-8, 12) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'balanceParams()',
  [8.5, balanceParams(-8, 12), -8, 12]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if 220 == balanceParams(200, 20) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'balanceParams()',
  [220, balanceParams(200, 20), 200, 20]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if 57.5 == balanceParams(30, 70) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'balanceParams()',
  [57.5, balanceParams(30, 70), 30, 70]
)

# ======================================== Day 6 ========================================
print()
print('==================== Day 6 ====================')
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if True == isNumberInArray([7, 5, 12, 3, 9], 3) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'isNumberInArray()',
  [True, isNumberInArray([7, 5, 12, 3, 9], 3), [7, 5, 12, 3, 9], 3]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if False == isNumberInArray([8, 8, 8, 8, 8], 88) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'isNumberInArray()',
  [False, isNumberInArray([8, 8, 8, 8, 8], 88), [8, 8, 8, 8, 8], 88]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if False == isNumberInArray([], 4) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'isNumberInArray()',
  [False, isNumberInArray([], 4), [], 4]
)

print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if True == biggerTotalOfEvenNumbers([4, 8, 12, 16]) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'biggerTotalOfEvenNumbers()',
  [True, biggerTotalOfEvenNumbers([4, 8, 12, 16]), [4, 8, 12, 16]]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if False == biggerTotalOfEvenNumbers([3, 7, 11, 15]) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'biggerTotalOfEvenNumbers()',
  [False, biggerTotalOfEvenNumbers([3, 7, 11, 15]), [3, 7, 11, 15]]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if True == biggerTotalOfEvenNumbers([2, 3, 4, 5, 6]) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'biggerTotalOfEvenNumbers()',
  [True, biggerTotalOfEvenNumbers([2, 3, 4, 5, 6]), [2, 3, 4, 5, 6]]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if False == biggerTotalOfEvenNumbers([0, 1, 0, 1, 0, 1]) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'biggerTotalOfEvenNumbers()',
  [False, biggerTotalOfEvenNumbers([0, 1, 0, 1, 0, 1]), [0, 1, 0, 1, 0, 1]]
)

# ======================================== Day 7 ========================================
print()
print('==================== Day 7 ====================')
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if True == isCollisionDetected([0, 0, 50, 50], [20, 20, 50, 50]) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'isCollisionDetected()',
  [True, isCollisionDetected([0, 0, 50, 50], [20, 20, 50, 50]), [0, 0, 50, 50], [20, 20, 50, 50]],
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if False == isCollisionDetected([200, 200, 50, 50], [100, 100, 50, 70]) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'isCollisionDetected()',
  [False, isCollisionDetected([200, 200, 50, 50], [100, 100, 50, 70]), [200, 200, 50, 50], [100, 100, 50, 70]],
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if True == isCollisionDetected([500, 800, 10, 10], [495, 795, 5, 5]) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'isCollisionDetected()',
  [True, isCollisionDetected([500, 800, 10, 10], [495, 795, 5, 5]), [500, 800, 10, 10], [495, 795, 5, 5]],
)

print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if [] == matrixAddition([], []) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'matrixAddition()',
  [[], matrixAddition([], []), [], []]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if [[2, 2, 2], [2, 2, 2]] == matrixAddition([[0, 2, 0], [2, 0, 2]], [[2, 0, 2], [0, 2, 0]]) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'matrixAddition()',
  [[[2, 2, 2], [2, 2, 2]], matrixAddition([[0, 2, 0], [2, 0, 2]], [[2, 0, 2], [0, 2, 0]]), [[0, 2, 0], [2, 0, 2]], [[2, 0, 2], [0, 2, 0]]]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if [[12, 4], [-9, 5]] == matrixAddition([[7, -3], [-5, 5]], [[5, 7], [-4, 0]]) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'matrixAddition()',
  [[[12, 4], [-9, 5]], matrixAddition([[7, -3], [-5, 5]], [[5, 7], [-4, 0]]), [[7, -3], [-5, 5]], [[5, 7], [-4, 0]]]
)

# ======================================== Day 8 ========================================
print()
print('==================== Day 8 ====================')
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if False == mastermind([1, 2, 3, 4, 5], []) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'mastermind()',
  [False, mastermind([1, 2, 3, 4, 5], []), [1, 2, 3, 4, 5], []]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if False == mastermind([2, 2, 2, 3, 2], [[1, 1, 1, 1, 1], [2, 2, 2, 2, 3], [2, 1, 2, 1, 2]]) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'mastermind()',
  [False, mastermind([2, 2, 2, 3, 2], [[1, 1, 1, 1, 1], [2, 2, 2, 2, 3], [2, 1, 2, 1, 2]]), [2, 2, 2, 3, 2], [[1, 1, 1, 1, 1], [2, 2, 2, 2, 3], [2, 1, 2, 1, 2]]]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if True == mastermind([5, 3, 4, 1, 2], [[5, 5, 5, 5, 5], [4, 4, 4, 4, 4], [3, 3, 3, 3, 3], [2, 2, 2, 2, 2], [1, 1, 1, 1, 1], [5, 4, 3, 2, 1], [5, 3, 4, 1, 2], [3, 5, 4, 2, 1]]) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'mastermind()',
  [True, mastermind([5, 3, 4, 1, 2], [[5, 5, 5, 5, 5], [4, 4, 4, 4, 4], [3, 3, 3, 3, 3], [2, 2, 2, 2, 2], [1, 1, 1, 1, 1], [5, 4, 3, 2, 1], [5, 3, 4, 1, 2], [3, 5, 4, 2, 1]]), [5, 3, 4, 1, 2], [[5, 5, 5, 5, 5], [4, 4, 4, 4, 4], [3, 3, 3, 3, 3], [2, 2, 2, 2, 2], [1, 1, 1, 1, 1], [5, 4, 3, 2, 1], [5, 3, 4, 1, 2], [3, 5, 4, 2, 1]]]
)

# ======================================== Day 9 ========================================
print()
print('==================== Day 9 ====================')
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if 9 == digitalRoot(123456789) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'digitalRoot()',
  [9, digitalRoot(123456789), 123456789]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if 3 == digitalRoot(555555) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'digitalRoot()',
  [3, digitalRoot(555555), 555555]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if 6 == digitalRoot(101010101010) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'digitalRoot()',
  [6, digitalRoot(101010101010), 101010101010]
)

# ======================================== Day 10 ========================================
print()
print('==================== Day 10 ====================')
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if [6] == chainSums([1, 2, 3]) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'chainSums()', 
  [[6], chainSums([1, 2, 3]), [1, 2, 3]]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if [5, 30] == chainSums([8, 4, 3, 2, 3, 5, 9, 10, 11]) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'chainSums()', 
  [[5, 30], chainSums([8, 4, 3, 2, 3, 5, 9, 10, 11]), [8, 4, 3, 2, 3, 5, 9, 10, 11]]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if [-18, 18] == chainSums([-7, -6, -5, 5, 6, 7]) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'chainSums()', 
  [[-18, 18], chainSums([-7, -6, -5, 5, 6, 7]), [-7, -6, -5, 5, 6, 7]]
)
print(
  f"{bcolors.OKGREEN}True{bcolors.ENDC}" if [] == chainSums([]) else f"{bcolors.FAIL}False{bcolors.ENDC}",
  'chainSums()', 
  [[], chainSums([]), []]
)
