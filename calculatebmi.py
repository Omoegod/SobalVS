weight = input('Indicate your weight, kg: ')
growth = input('Indicate your growth, m: ')
IndexBMI = int(int(weight) // (float(growth) * float(growth)))
scale = ("0" + "=" * IndexBMI)
scale2 = ("=" * (40 - IndexBMI) + "40")

if IndexBMI <= 18:
    print('Ваш вес ниже нормы: ' + str(IndexBMI))
    print(scale + "|" +  scale2)
elif IndexBMI <= 25:
    print('Ваш вес в норме: ' + str(IndexBMI))
    print(scale + "|" +  scale2)
elif IndexBMI <= 40:
    print('У Вас избыточный вес, пора бы заняться собой: ' + str(IndexBMI))
    print(scale + "|" +  scale2)        
else:
    print('Возможно вы не смогли встать что бы ввести данные')

