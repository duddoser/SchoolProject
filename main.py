import json
from collections import defaultdict


from UniversityProcess import University

with open('data.json', encoding='utf-8') as f:
    templates = json.load(f)

request = "Математика,Русский язык,Физика,Биология,Вступительные"
result = defaultdict(list)
for key in templates:
    for value in templates[key]:
        if value.get(request) is not None:
            for el in value[request]:
                result[key].append(el + ' - ' + str(value[request][el]))
print(result)


with open('data_test.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
