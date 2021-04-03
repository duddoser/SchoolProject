import json
from collections import defaultdict


from UniversityProcess import University

university_mod = University()
universities_list = university_mod.get_universities()
subjects = ['Физика', 'Информатика', 'Биология', 'Химия', 'Обществознание', 'История',
            'Иностранный язык', 'Литература', 'География', 'Вступительные']
# прогнать по одному вузу каждую комбинацию
unis = ['Первый Московский государственный медицинский университет им. И.М.Сеченова',
        'Российский университет дружбы народов',
        'Новосибирский государственный технический университет',
        'Российский национальный исследовательский медицинский университет имени Н. И. Пирогова',
        'Московский государственный лингвистический университет',
        'Нижегородский государственный университет им. Н.И. Лобачевского',
        'Южный федеральный университет',
        'Самарский национальный исследовательский университет имени академика С.П. Королева',
        'Всероссийская академия внешней торговли Министерства экономического развития России',
        'Московский авиационный институт']
rate = 1
with open('data.json', 'w', encoding='utf-8') as f:
    final = {}
    for u in unis:
        result = defaultdict(list)
        for i in range(len(subjects)):
            subjects_now = ['Математика', 'Русский язык', subjects[i]]
            response = university_mod.get_faculties(universities_list[u], subjects_now)
            if response is not None:
                result[u].append({','.join(subjects_now): response})
            for j in range(i + 1, len(subjects)):
                subjects_now = ['Математика', 'Русский язык', subjects[i], subjects[j]]
                response = university_mod.get_faculties(universities_list[u], subjects_now)
                if response is not None:
                    result[u].append({','.join(subjects_now): response})

                for k in range(j + 1, len(subjects)):
                    subjects_now = ['Математика', 'Русский язык', subjects[i], subjects[j], subjects[k]]
                    response = university_mod.get_faculties(universities_list[u], subjects_now)
                    if response is not None:
                        result[u].append({','.join(subjects_now): response})
        if result is not None:
            final[u] = result[u]
    json.dump(final, f, ensure_ascii=False, indent=4)

# with open('data.json', 'w', encoding='utf-8') as f:
#     json.dump(result, f, ensure_ascii=False, indent=4)
