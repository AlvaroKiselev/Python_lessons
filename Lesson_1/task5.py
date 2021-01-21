proceeds = int(input('Введите выручку компании')) # выручка компании
expenses = int(input('Введите издержки компании')) # издержки компании
profit = proceeds - expenses # доход компании
if profit > 0:
    profitability = profit / proceeds
    print('Ваша компания приносит доход, равный {}  \nРентабельность компании составляет {:.3f}'.format(profit, profitability))
    staff = int(input('Введите численность сотрудников компании'))
    print (f'Прибыль компании в расчёте на одного сотрудника составляет {(profit / staff):.3f}')
elif profit == 0:
    print('Выручка и издержки компании совпадают, прибыль отсутствует')
else:
    print('Ваша компания убыточна, убыток составляет {}'.format(profit))