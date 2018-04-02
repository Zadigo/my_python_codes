# import itertools as it
# n
#  = [9, 7, 2, 4, 8, 7, 0, 8]

# for a in range(1, len(n), 2):
#     nun = (n[a]).__add__(n[a])
#     if nun > 9:
#         nun = nun - 9
#     n[a] = nun

# print(n)

# tota = it.accumulate(n)

# print(tota)

# import re

# SIRET = 828733253
# SIREN = 82873325300011

# PATTERNS ={
#     'siret': r'[0-9]{9}',
#     'siren': r'[0-9]{14}'
# }
# print(re.search(PATTERNS['siret'], str(SIRET)).group(0))
# print(re.search(r'[0-9]{9}', str(SIREN)))

# CO = '1w@Kurri-#2018'
# PATTERN = r'\d[x-z]\@(Kurri)\-\#(2018)'
# print(re.search(PATTERN, str(CO)))