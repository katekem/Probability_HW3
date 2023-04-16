# В первом ящике находится 10 мячей, из которых 7 - белые.
# Во втором ящике - 11 мячей, из которых 9 белых.
# Из каждого ящика вытаскивают случайным образом по два мяча.
# Какова вероятность того, что все мячи белые?
# Какова вероятность того, что ровно два мяча белые?
# Какова вероятность того, что хотя бы один мяч белый?

import comb as c

all1 = 10
white1 = 7
other1 = all1 - white1

all2 = 11
white2 = 9
other2 = all2 - white2

# все исходы
n1 = c.combinations(all1, 2) # 45
n2 = c.combinations(all2, 2) # 55

#------------------------------------------------------------------------------------------------
task1 = 'Вероятность того, что все мячи белые' # 2 и 2

# благоприятные исходы
am1 = c.combinations(white1, 2) # 21
am2 = c.combinations(white2, 2) # 36

aresult1 = am1 / n1
aresult2 = am2 / n2
aresult = aresult1 * aresult2

print(f'{task1} = {round(aresult * 100, 2)}%.') # 30.55%

#------------------------------------------------------------------------------------------------
task2 = 'Вероятность того, что ровно два мяча белые' # 0 и 2; 1 и 1; 2 и 0

# благоприятные исходы
bm1 = c.combinations(white1, 0) * c.combinations(other1, 2) # 3
bm2 = c.combinations(white2, 2) * c.combinations(other2, 0) # 36
bm3 = c.combinations(white1, 1) * c.combinations(other1, 1) # 21
bm4 = c.combinations(white2, 1) * c.combinations(other2, 1) # 18
bm5 = c.combinations(white1, 2) * c.combinations(other1, 0) # 21
bm6 = c.combinations(white2, 0) * c.combinations(other2, 2) # 1

bresult1 = (bm1 / n1) * (bm2 / n2)
bresult2 = (bm3 / n1) * (bm4 / n2)
bresult3 = (bm5 / n1) * (bm6 / n2)
bresult = bresult1 + bresult2 + bresult3

print(f'{task2} = {round(bresult * 100, 2)}%.') # 20.48%

#------------------------------------------------------------------------------------------------
task3 = 'Вероятность того, что хотя бы один мяч белый'
# 0 и 1; 0 и 2; 1 и 0; 1 и 1; 1 и 2; 2 и 0; 2 и 1; 2 и 2

# благоприятные исходы (их составляющие)

# из 1 корзины - 0
anum = c.combinations(white1, 0) * c.combinations(other1, 2) # 3
# из 2 корзины - 0
bnum = c.combinations(white2, 0) * c.combinations(other2, 2) # 1
# из 1 корзины - 1
cnum = c.combinations(white1, 1) * c.combinations(other1, 1) # 21
# из 2 корзины - 1
dnum = c.combinations(white2, 1) * c.combinations(other2, 1) # 18
# из 1 корзины - 2
enum = c.combinations(white1, 2) * c.combinations(other1, 0) # 21
# из 2 корзины - 2
fnum = c.combinations(white2, 2) * c.combinations(other2, 0) # 36

cresult1 = (anum / n1) * (dnum / n2)
cresult2 = (anum / n1) * (fnum / n2)
cresult3 = (cnum / n1) * (bnum / n2)
cresult4 = (cnum / n1) * (dnum / n2)
cresult5 = (cnum / n1) * (fnum / n2)
cresult6 = (enum / n1) * (bnum / n2)
cresult7 = (enum / n1) * (dnum / n2)
cresult8 = (enum / n1) * (fnum / n2)

cresult = cresult1 + cresult2 + cresult3 + cresult4 + cresult5 + cresult6 + cresult7 + cresult8

print(f'{task3} = {round(cresult * 100, 2)}%.') # 99.88%