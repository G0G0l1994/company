
"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.

Ваши задачи такие:
1. Вывести названия всех отделов done
2. Вывести имена всех сотрудников компании. done (optimization need)
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают. done (optimization need)
4. Вывести имена всех сотрудников компании, которые получают больше 100к. done (optimization need)
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями). done
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела. done

Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём. done
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём. done
9. Вывести среднюю зарплату по всей компании. done
10. Вывести названия должностей, которые получают больше 90к без повторений.done
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин). done
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву. done

Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.

13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""


departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

def get_emp(departments: list, emp_lst = []):
    """ 
    Получаем список славарей на каждого сотрудника для дальнейших манипуляций
    
    """
    lst = [dep['employers'] for dep in departments]
    c = 0
    for num in lst:
        for emp in num:
            emp.setdefault('title', departments[c]['title'])
        c += 1
    for emp in lst:
        emp_lst += emp
          
    return emp_lst

# для блока 1
def show_title(departments: list):
    return [dep['title'] for dep in departments]  
    

def show_name_emp(departments: list,name_emp = []):
    
    for name in get_emp(departments):
        name_emp.append(f"Name: {name['first_name']} {name['last_name']}")
    return name_emp
    
def show_name_with_title(departments: list, name_emp = [] ):
    
    for name in get_emp(departments):
        name_emp.append(f"Name: {name['first_name']} {name['last_name']}, departments: {name['title']}")
    return name_emp

def show_emp_over_100(departments: list, emp_income = []):
    
    for name in get_emp(departments): 
        if name['salary_rub'] > 100000:
            emp_income.append(f"Name: {name['first_name']} {name['last_name']}, salary: {name['salary_rub']}")
    return emp_income

def get_less_80(departments: list):
    return [name['position'] for name in get_emp(departments) if name['salary_rub'] < 80000]

def dep_expenses(departments: list):
    for name_title in departments:
         print(f"{name_title['title']}: {sum([name['salary_rub'] for name in get_emp(departments) if name['title'] == name_title['title']])}")
# для блока 2


def min_salary(departments: list):
    for name_title in departments:
        lst = [name['salary_rub'] for name in get_emp(departments) if name['title'] == name_title['title']]
        print(f"{name_title['title']} : минимальная заработная плата {min(lst)}")
              
def salary_title(departments: list):
    for name_title in departments:
        lst = [name['salary_rub'] for name in get_emp(departments) if name['title'] == name_title['title']]
        
        print(f"Минимальная заработная плата в отделе {name_title['title']} :{min(lst)}")
        print(f"Максимальная заработная плата в отделе {name_title['title']} :{max(lst)}")
        print(f"Средняя заработная плата в отделе {name_title['title']} :{int(sum(lst)/len(lst))}")

def average_salary(departments: list):
    lst = [name['salary_rub'] for name in get_emp(departments)]
    return f"Средняя заработная плата в компании: {sum(lst)/len(lst)}"

def high_position(departmants: list):
    lst = set([name['position'] for name in get_emp(departments) if name['salary_rub'] > 90000])
    return lst

def women_salary(departments):
    women = ["Michelle","Nicole","Christina","Caitlin"]
    lst = [name["salary_rub"] for name in get_emp(departments) if name['first_name'] in women]
    return f"Средняя заработная плата среди девушек компании : {int(sum(lst)/len(lst))}"

def vowel_letter_end(departments):
    letters = "aeiouy"
    lst = set([name['first_name'] for name in get_emp(departments) if name['last_name'][-1] in letters])
    return lst


# для блока 3



# первый блок
print(*show_title(departments), sep = ', ') 
print(*show_name_emp(departments), sep = ', ')
print(*show_name_with_title(departments), sep = ', ')
print(*show_emp_over_100(departments), sep = ', ')
print(*get_less_80(departments), sep = ', ')
dep_expenses(departments)

# второй блок
min_salary(departments)
salary_title(departments)
print(average_salary(departments))
print(high_position(departments))
print(women_salary(departments))
print(*vowel_letter_end(departments), sep = ', ')

# третий блок







