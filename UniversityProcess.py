import requests
from bs4 import BeautifulSoup

URL = 'https://vuzopedia.ru'
RATE = '/rate'
EGE = '/kakie-ege-sdavat'
POEGE = '/poege/'
SUBJECTS = {'Математика': 'egemat', 'Русский язык': 'egerus', 'Физика': 'egefiz', 'Вступительные': 'vstup',
            'Информатика': 'egeinform', 'Биология': 'egebiol', 'Химия': 'egehim', 'Обществознание': 'egeobsh',
            'История': 'egeist', 'Иностранный язык': 'egeinyaz', 'Литература': 'egeliter', 'География': 'egegeorg'}


class University:

    def get_universities(self):
        page = requests.get(URL + RATE)
        soup = BeautifulSoup(page.content, 'html.parser')
        uni_rate = soup.find_all('div', {'class': 'col-md-12 vuzRateItem'})

        universities = {}
        k = 1
        for title in uni_rate:
            for a in title.find_all('a', href=True):
                uni = title.find('a').text.strip('>')
                if a['href'] != '/vuz/1415':
                    universities[uni] = {k: a['href']}
            if k == 30:
                return universities
            k += 1

    def get_faculties(self, universities, request):
        response = {}

        for university in universities:
            for ref in universities[university]:
                req = ''
                for el in request:
                    req += SUBJECTS[el] + ';'

                page = requests.get(URL + universities[university][ref] + POEGE + req)
                soup = BeautifulSoup(page.content, 'html.parser')
                faculties = soup.find_all('div', {'class': 'itemSpecAll'})

                result = {}
                for fac in faculties:
                    for title in fac.find_all('a', {'class': 'spectittle'}):
                        try:
                            additional = fac.find_all('a', {'class': 'tooltipq'})[2].text.strip('<')
                            additional2 = fac.find_all('a', {'class': 'tooltipq'})[1].text.strip('<')
                            if additional[3] != '-':
                                try:
                                    result[title.text.strip('<')] = int(additional[3:6])
                                except ValueError:
                                    if additional2[3:6][0] in '1234567890' and additional2[3:6][1] in '1234567890' and \
                                            additional2[3:6][2] in '1234567890':
                                        result[title.text.strip('<')] = int(additional2[3:6])
                        except IndexError:
                            pass
                if result != {}:
                    response[university] = result
        return response
