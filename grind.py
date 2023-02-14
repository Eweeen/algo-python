import math

# ================================================================
#                             Jour 1
# ================================================================

# Retourne la valeur true
def returnTrue() -> bool:
  return True

# Retourne le paramètre donné en entrée
def returnParam(param: int) -> int:
  return param

# Retourne vrai si param est strictement supérieur à 5
# Retourne faux sinon
def isBiggerThan5(param: int) -> bool:
  return True if param > 5 else False

# Retourne vrai si param est faux
# Retourne faux si param est vrai
def invertBoolean(param: bool) -> bool:
  return not param

# ================================================================
#                             Jour 2
# ================================================================

# Retourne la somme des paramètres a b et c, le tout multiplié par 5
def sumTimes5(a: int, b: int, c: int) -> int:
  return (a + b + c) * 5

# Retourne vrai si a ET b sont strictement supérieurs à 5 et strictement inférieurs à 10
# Retourne faux sinon
def areBetween5And10(a: int, b: int) -> bool:
  return True if 10 > a > 5 and 10 > b > 5 else False

# ================================================================
#                             Jour 3
# ================================================================

# Si la somme des paramètres est paire, retourner le carré de a.
# Sinon, retourner le cube de b.
def parityComputing(a: int, b: int) -> int:
  return pow(a, 2) if (a + b) % 2 == 0 else pow(b, 3)

# Ajouter n fois la lettre letter au mot word
# Retourner la chaîne de caractères résultante
def addLetters(word: str, letter: str, n: int) -> str:
  for i in range(n): word += letter
  return word

# ================================================================
#                             Jour 4
# ================================================================

# Retourne le chiffre des centaines d'un nombre
# (exemple: 5120 -> 1)
# Retourne 0 si le nombre est inférieur à 100
def getHundreds(a: int) -> int:
  return math.floor((a - (math.floor(a/1000) * 1000)) / 100)

# Retourne la somme de tous les éléments du tableau
def sumArray(a: list[int]) -> int:
  somme = 0

  for i in range(len(a)):
    somme += a[i]

  return somme

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
