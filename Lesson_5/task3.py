with open('salaries.txt') as file:
    lines = file.readlines()

salaries = []
for line in lines:
    name, salary = line.split(' - ')
    salaries.append(int(salary))
    if int(salary) < 20000:
        print(line, end='')
print('\nСредняя зарплата:', sum(salaries) / len(salaries))