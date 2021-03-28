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
        soup = BeautifulSoup(page.content, 'html.parser')import requests
from bs4 import BeautifulSoup

URL = 'https://vuzopedia.ru'
RATE = '/rate'
EGE = '/kakie-ege-sdavat'
POEGE = '/poege/'
SUBJECTS = {'Математика': 'egemat', 'Русский язык': 'egerus', 'Физика': 'egefiz', 'Вступительные': 'vstup',
            'Информатика': 'egeinform', 'Биология': 'egebiol', 'Химия': 'egehim', 'Обществознание': 'egeobsh',
            'История': 'egeist', 'Иностранный язык': 'egeinyaz', 'Литература': 'egeliter', 'География': 'egegeorg'}

UNIVERSITY_PICS = {'Московский государственный университет имени М.В. Ломоносова': 'https://vuzopedia.ru/storage/app/uploads/public/6fe/fe8/729/thumb__59_59_0_0_auto.png',
                   'Московский физико-технический институт (Государственный университет)': 'https://vuzopedia.ru/storage/app/uploads/public/b48/2e2/3a7/thumb__59_59_0_0_auto.png',
                   'Национальный исследовательский ядерный университет «МИФИ»': 'https://vuzopedia.ru/storage/app/uploads/public/258/27d/4e3/thumb__59_59_0_0_auto.png',
                   'Национальный исследовательский университет «Высшая школа экономики»': 'https://vuzopedia.ru/storage/app/uploads/public/2e6/64a/712/thumb__59_59_0_0_auto.png',
                   'Московский государственный институт международных отношений (Университет) МИД России': 'https://vuzopedia.ru/storage/app/uploads/public/bff/e64/054/thumb__59_59_0_0_auto.png',
                   'Санкт-Петербургский государственный университет': 'https://vuzopedia.ru/storage/app/uploads/public/b71/95e/456/thumb__59_59_0_0_auto.png',
                   'Московский государственный технический университет им. Н.Э. Баумана': 'https://vuzopedia.ru/storage/app/uploads/public/e31/f13/0cb/thumb__59_59_0_0_auto.png',
                   'Национальный исследовательский Томский политехнический университет': 'https://vuzopedia.ru/storage/app/uploads/public/d75/933/76a/thumb__59_59_0_0_auto.png',
                   'Санкт-Петербургский политехнический университет Петра Великого': 'https://vuzopedia.ru/storage/app/uploads/public/f0a/04e/7ac/thumb__59_59_0_0_auto.png',
                   'Российская академия народного хозяйства и государственной службы при Президенте Российской Федерации': 'https://vuzopedia.ru/storage/app/uploads/public/f87/949/66d/thumb__59_59_0_0_auto.png',
                   'Уральский федеральный университет имени первого Президента России Б. Н. Ельцина': 'https://vuzopedia.ru/storage/app/uploads/public/b1f/ee0/0ef/thumb__59_59_0_0_auto.png',
                   'Казанский (Приволжский) федеральный университет': 'https://vuzopedia.ru/storage/app/uploads/public/579/27c/1e0/thumb__59_59_0_0_auto.png',
                   'Национальный исследовательский Томский государственный университет': 'https://vuzopedia.ru/storage/app/uploads/public/848/19d/354/thumb__59_59_0_0_auto.png',
                   'Финансовый университет при Правительстве Российской Федерации': 'https://vuzopedia.ru/storage/app/uploads/public/b02/af5/31c/thumb__59_59_0_0_auto.png',
                   'Российский экономический университет имени Г.В. Плеханова': 'https://vuzopedia.ru/storage/app/uploads/public/654/7ae/a6f/thumb__59_59_0_0_auto.png',
                   'Национальный исследовательский технологический университет «МИСиС»': 'https://vuzopedia.ru/storage/app/uploads/public/29e/d42/2bc/thumb__59_59_0_0_auto.png',
                   'Сибирский федеральный университет': 'https://vuzopedia.ru/storage/app/uploads/public/91f/358/245/thumb__59_59_0_0_auto.png',
                   'Российский государственный университет нефти и газа им. И.М. Губкина': 'https://vuzopedia.ru/storage/app/uploads/public/950/bf8/7e4/thumb__59_59_0_0_auto.png',
                   'Национальный исследовательский университет «МЭИ»': 'https://vuzopedia.ru/storage/app/uploads/public/fc2/727/dad/thumb__59_59_0_0_auto.png',
                   'Санкт-Петербургский национальный исследовательский университет информационных технологий, механики и оптики': 'https://vuzopedia.ru/storage/app/uploads/public/c10/e72/7ae/thumb__59_59_0_0_auto.png',
                   'Первый Московский государственный медицинский университет им. И.М.Сеченова': 'https://vuzopedia.ru/storage/app/uploads/public/f1f/741/422/thumb__59_59_0_0_auto.png',
                   'Российский университет дружбы народов': 'https://vuzopedia.ru/storage/app/uploads/public/ed1/9f6/9c5/thumb__59_59_0_0_auto.png',
                   'Российский национальный исследовательский медицинский университет имени Н. И. Пирогова': 'https://vuzopedia.ru/storage/app/uploads/public/534/62b/88b/thumb__59_59_0_0_auto.png',
                   'Московский государственный лингвистический университет': 'https://vuzopedia.ru/storage/app/uploads/public/2c3/400/cb5/thumb__59_59_0_0_auto.png',
                   'Нижегородский государственный университет им. Н.И. Лобачевского': 'https://vuzopedia.ru/storage/app/uploads/public/fcf/dde/eef/thumb__59_59_0_0_auto.png',
                   'Южный федеральный университет': 'https://vuzopedia.ru/storage/app/uploads/public/791/100/bf4/thumb__59_59_0_0_auto.png',
                   'Самарский национальный исследовательский университет имени академика С.П. Королева': 'https://vuzopedia.ru/storage/app/uploads/public/402/a1e/b16/thumb__59_59_0_0_auto.png',
                   'Всероссийская академия внешней торговли Министерства экономического развития России': 'https://vuzopedia.ru/storage/app/uploads/public/614/241/8ef/thumb__59_59_0_0_auto.png',
                   'Московский авиационный институт': 'https://vuzopedia.ru/storage/app/uploads/public/9f6/23d/9fa/thumb__59_59_0_0_auto.png'}


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
                    response[university] = [result, UNIVERSITY_PICS[university]]
        return response

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
