# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат

flag = True
for x in range(0, 2):
    for y in range(0,2):
        for z in range (0,2):
            if ((not x) & (not y) & (not z)) != (not (x | y | z)):
                flag=False
                break
if flag:
    print ("Утверждение истинно при любых значения X Y Z")
else:
    print ("Утверждение не истинно")

