import requests, json
from bs4 import BeautifulSoup

from UniversityProcess import University

SUBJECTS = {'Математика': 'egemat', 'Русский язык': 'egerus', 'Физика': 'egefiz', 'Вступительные': 'vstup',
            'Информатика': 'egeinform', 'Биология': 'egebiol', 'Химия': 'egehim', 'Обществознание': 'egeobsh',
            'История': 'egeist', 'Иностранный язык': 'egeinyaz', 'Литература': 'egeliter', 'География': 'egegeorg'}

uni_process = University()
uni_list = uni_process.set_universities()
n = len(SUBJECTS.keys()) - 2
keys = []
for el in SUBJECTS:
    if el != 'Математика' and el != 'Русский язык':
        keys.append(el)

result = {}
for x1 in range(n):
    # d = ['Математика', 'Русский язык', keys[x1]]
    # response = uni_process.get_faculties(uni_list, d)
    # result[' '.join(d)] = response
    for x2 in range(x1 + 1, n):
        d = ['Математика', 'Русский язык', keys[x1], keys[x2]]
        response = uni_process.get_faculties(uni_list, d)
        result[' '.join(d)] = response
        continue
        for x3 in range(x2 + 1, n):
            d = ['Математика', 'Русский язык', keys[x1], keys[x2], keys[x3]]
            response = uni_process.get_faculties(uni_list, d)
            result[' '.join(d)] = response

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

# URL = 'https://vuzopedia.ru'
# RATE = '/rate'
# EGE = '/kakie-ege-sdavat'
# POEGE = '/poege/'
# SUBJECTS = {'Математика': 'egemat', 'Русский язык': 'egerus', 'Физика': 'egefiz', 'Вступительные': 'vstup',
#             'Информатика': 'egeinform', 'Биология': 'egebiol', 'Химия': 'egehim', 'Обществознание': 'egeobsh',
#             'История': 'egeist', 'Иностранный язык': 'egeinyaz', 'Литература': 'egeliter', 'География': 'egegeorg'}
#
# page = requests.get(URL + RATE)
# soup = BeautifulSoup(page.content, 'html.parser')
# uni_rate = soup.find_all('div', {'class': 'col-md-12 vuzRateItem'})
#
# universities = {}
# k = 1
# for title in uni_rate:
#     for a in title.find_all('a', href=True):
#         uni = title.find('a').text.strip('>')
#         if a['href'] != '/vuz/1415':
#             universities[uni] = {k: a['href']}
#     k += 1
#
# request = {'Математика', 'Русский язык', 'Физика'}
# response = {}
#
# for university in universities:
#     for ref in universities[university]:
#         req = ''
#         for el in request:
#             req += SUBJECTS[el] + ';'
#
#         page = requests.get(URL + universities[university][ref] + POEGE + req)
#         soup = BeautifulSoup(page.content, 'html.parser')
#         faculties = soup.find_all('div', {'class': 'itemSpecAll'})
#
#         result = {}
#         for fac in faculties:
#             for title in fac.find_all('a', {'class': 'spectittle'}):
#                 try:
#                     additional = fac.find_all('a', {'class': 'tooltipq'})[2].text.strip('<')
#                     additional2 = fac.find_all('a', {'class': 'tooltipq'})[1].text.strip('<')
#                     if additional[3] != '-':
#                         try:
#                             result[title.text.strip('<')] = int(additional[3:6])
#                         except ValueError:
#                             if additional2[3:6][0] in '1234567890' and additional2[3:6][1] in '1234567890' and \
#                             additional2[3:6][2] in '1234567890':
#                                 result[title.text.strip('<')] = int(additional2[3:6])
#                 except IndexError:
#                     pass
#         if result != {}:
#             response[university] = result
#
# with open('data.json', 'w', encoding='utf-8') as f:
#     json.dump(response, f, ensure_ascii=False, indent=4)
