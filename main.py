import json
from collections import defaultdict


from UniversityProcess import University

university_mod = University()
universities_list = university_mod.get_universities()
subjects = ['Физика', 'Информатика', 'Биология', 'Химия', 'Обществознание', 'История',
            'Иностранный язык', 'Литература', 'География', 'Вступительные']
# прогнать по одному вузу каждую комбинацию
result = defaultdict(list)
u = 'Московский государственный университет имени М.В. Ломоносова'
rate = 1
for i in range(len(subjects)):
    subjects_now = ['Математика', 'Русский язык', subjects[i]]
    response = university_mod.get_faculties(universities_list, subjects_now)
    print(response)
    for j in range(i + 1, len(subjects)):
        subjects_now = ['Математика', 'Русский язык', subjects[i], subjects[j]]
        response = university_mod.get_faculties(universities_list, subjects_now)
        print(response)

        for k in range(j + 1, len(subjects)):
            subjects_now = ['Математика', 'Русский язык', subjects[i], subjects[j], subjects[k]]
            response = university_mod.get_faculties(universities_list, subjects_now)



# with open('data.json', 'w', encoding='utf-8') as f:
#     json.dump(result, f, ensure_ascii=False, indent=4)

