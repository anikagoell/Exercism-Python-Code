SUBLIST = 'SUBLIST'
SUPERLIST = 'SUPERLIST'
EQUAL = 'EQUAL'
UNEQUAL = 'UNEQUAL'


def sublist(a, b):
  if a == b:
    return EQUAL
  elif not a:
    return SUBLIST
  elif not b:
    return SUPERLIST
  elif len(a) > len(b):
    return SUPERLIST if chck(b, a) else UNEQUAL
  elif len(b) > len(a):
    return SUBLIST if chck(a, b) else UNEQUAL
  return UNEQUAL


def chck(l1, l2):
  n1, n2 = len(l1), len(l2)
  for i in range(n2 - n1 + 1):
    if l2[i : i + n1] == l1:
      return True
  return False
