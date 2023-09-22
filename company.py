from collections import Counter
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

13. Вывести список отделов со средним налогом на сотрудников этого отдела.  fuking done
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов. done
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки. done
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год. done
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов. done
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
    {"department": "IT department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

def get_emp(departments: list):
    """ 
    Получаем список славарей на каждого сотрудника для дальнейших манипуляций
    
    """
    global emp_lst
    emp_lst = []
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
    for dep in departments:
        print(dep['title'])
    

def show_name_emp(departments: list):
    
    for name in get_emp(departments):
        print(f"Name: {name['first_name']} {name['last_name']}")
    
    
def show_name_with_title(departments: list):
    
    for name in get_emp(departments):
        print(f"Name: {name['first_name']} {name['last_name']}, departments: {name['title']}")
    

def show_emp_over_100(departments: list):
    print("Получают больше 100 000:")
    for name in get_emp(departments): 
        if name['salary_rub'] > 100000:
            print(f"Name: {name['first_name']} {name['last_name']}, salary: {name['salary_rub']}")

def get_less_80(departments: list):
    print("Получают меньше 80 000:")
    for name in get_emp(departments):
        if name['salary_rub'] < 80000:
            print(name['position'])  
        

def dep_expenses(departments: list):
    print("Затраты на отдел в месяц:")
    for name_title in departments:
         print(f"{name_title['title']}: {sum([name['salary_rub'] for name in get_emp(departments) if name['title'] == name_title['title']])}")
# для блока 2


def min_salary(departments: list):
    print("Минимальная заработная плата по отделам:")
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
    print("Должности с оплатой выше 90 000:")
    lst = set([name['position'] for name in get_emp(departments) if name['salary_rub'] > 90000])
    return lst

def women_salary(departments):
    women = ["Michelle","Nicole","Christina","Caitlin"]
    lst = [name["salary_rub"] for name in get_emp(departments) if name['first_name'] in women]
    return f"Средняя заработная плата среди девушек компании : {int(sum(lst)/len(lst))}"

def vowel_letter_end(departments):
    print("Фамилии, оканчивающиеся на гласную букву :")
    letters = "aeiouy"
    lst = set([name['first_name'] for name in get_emp(departments) if name['last_name'][-1] in letters])
    return lst


# для блока 3
def tax_for_department():
    
    name_department = [title['title'] for title in departments]
    tax_department = {}
   
    for name in name_department:
        for tax in taxes:
            if tax['department'] == None:
                tax_department[name] = tax['value_percents']/100
                
            if tax['department'] == name:
                tax_department[name] += tax['value_percents']/100
    
    return tax_department
    
def sum_tax():
    global sum_tax
    tax_department = tax_for_department()
    payment_dict = {}
    sum_tax = {}

    lst_emp = get_emp(departments)
    name_department = [title['title'] for title in departments]
    
    
    for payment in lst_emp:
        if payment['title'] in payment_dict:
            payment_dict[payment['title']] += payment['salary_rub']
        else:
            payment_dict[payment['title']] = payment['salary_rub']
            
    for name in name_department:
        sum_tax[name] = payment_dict[name] * tax_department[name]

    return sum_tax

def payment_for_employers():
    tax = tax_for_department()
    lst_emp = get_emp(departments)
    payment_with_tax = {}
    for department in tax.keys():
        for employer in lst_emp:
            if employer['title'] == department:
                payment_with_tax[employer['last_name']] = employer['salary_rub'] - (employer['salary_rub'] * tax[employer['title']])
    
    for employer in lst_emp:
        print(f"Заработная плата {employer['first_name']} {employer['last_name']} из отдела {employer['title']} 'на руки' - {payment_with_tax[employer['last_name']]}") 

def month_tax_load():
    lst = sum_tax
    return sorted(lst, key =lst.get)

def tax_over_100():
    global over_100
    lst_emp = emp_lst
    tax = tax_for_department()
    over_100 = [f"{employer['first_name']} {employer['last_name']}" 
                for employer in lst_emp if ((employer['salary_rub'] * tax[employer['title']])*12) > 100000]
    return over_100
    
def min_tax_employer():
    lst_over_100 = over_100
    for employer in emp_lst:
        name = f"{employer['first_name']} {employer['last_name']}"
        if name  not in lst_over_100:
            return name
    

# первый блок
show_title(departments)
show_name_emp(departments)
show_name_with_title(departments)
show_emp_over_100(departments)
get_less_80(departments)
dep_expenses(departments)

# второй блок
min_salary(departments)
salary_title(departments)
print(average_salary(departments))
print(high_position(departments))
print(women_salary(departments))
print(*vowel_letter_end(departments), sep = ', ')

# третий блок
print(sum_tax())
print(tax_for_department())
payment_for_employers()
print(month_tax_load())
print(*tax_over_100(), sep = ", ")
print(min_tax_employer())




