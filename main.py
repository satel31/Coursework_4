from src.engine_requests import HHRequest, SJRequest
from src.connector_classes import ConnectorJson
from src.vacancy_classes import Vacancy


# Query for searching

print('Добрый день! Введите поисковой запрос для поиска вакансий на платформах HeadHunter и SuperJob')
search_query = input()

# Query the name of the file
print('Укажите имя файла, куда будут записаны результаты, в формате filename.json. '
      'По умолчанию файл будет называться vacancies.json. Укажите "ок", если согласны с названием')
filename = input()
if filename.lower() == 'ок':
    connection = ConnectorJson()
else:
    connection = ConnectorJson(filename)

# Request for vacancies
hh = HHRequest(search_query)
sj = SJRequest(search_query)

# Write to file
hh.pass_by_page(connection)
sj.pass_by_page(connection)

print(f'Вакансии по Вашему запросу записаны в файл {connection.filename}')

def user_interaction(connection):
    print('Теперь Вы можете:\n'
          '1) Сортировка вакансий\n'
          '2) Вывести топ вакансии по уровню з/п\n'
          '3) Удалить вакансии\n'
          '4) Вывести все вакансии\n'
          '5) Удалить файл')

    parameters_to_sort = '1) Название вакансии\n'\
                         '2) Нижняя граница з/п\n'\
                         '3) Верхняя граница з/п\n'\
                         '4) Нижняя граница з/п и верхняя граница з/п\n'\
                         '5) Валюта з/п\n'\
                         '6) Компания'

    user_action = input('Введите действие ')

    if user_action == 'Сортировка вакансий':
        print(f'Выберите один из доступных параметров для сортировки:{parameters_to_sort}')
        user_parameter_sort = input()
        if user_parameter_sort == 'Нижняя граница з/п':
            print('Введите сумму для сортировки')
            clue_from = int(input())
            clue_to = None
            result = connection.select_by_salary(clue_from, clue_to)
        elif user_parameter_sort == 'Верхняя граница з/п':
            print('Введите сумму для сортировки')
            clue_from = None
            clue_to = int(input())
            result = connection.select_by_salary(clue_from, clue_to)
        elif user_parameter_sort == 'Нижняя граница з/п и верхняя граница з/п':
            print('Введите суммы для сортировки в формате ХХХ - ХХХ')
            clues = input().split(' - ')
            clue_from = int(clues[0])
            clue_to = int(clues[1])
            result = connection.select_by_salary(clue_from, clue_to)
        else:
            print('Введите ключевое слово для сортировки')
            clue = input()
            result = connection.select_data(user_parameter_sort, clue)

        for item in result:
            print(item)
    elif user_action == 'Вывести топ вакансии по уровню з/п':
        print('Введите количество вакансий в топе')
        amount = int(input())
        data = connection.read_file
        result = Vacancy.top_vacancies(amount, data)

        for item in result:
            print(item)

    elif user_action == 'Удалить вакансии':
        print(f'Выберите один из доступных параметров для сортировки:{parameters_to_sort}')
        user_parameter_del = input()
        print('Введите ключевое слово для удаления')
        if user_parameter_del == 'Нижняя граница з/п' or user_parameter_del == 'Верхняя граница з/п':
            clue_del = int(input())
            connection.delete_by_clue(user_parameter_del, clue_del)
        elif user_parameter_del == 'Нижняя граница з/п и верхняя граница з/п':
            print('Введите суммы для сортировки в формате ХХХ - ХХХ')
            clues = input().split(' - ')
            clue_from = int(clues[0])
            clue_to = int(clues[1])
            connection.delete_by_clue(user_parameter_del, clue_from)
            connection.delete_by_clue(user_parameter_del, clue_to)
        else:
            clue_del = input()
            connection.delete_data_by_clue(user_parameter_del, clue_del)

    elif user_action == 'Вывести все вакансии':
        result = connection.read_file

        for item in result:
            print(item)

    elif user_action == 'Удалить файл':
        connection.delete_data()
        print('Работа завершена. Файл успешно удалён')


if __name__ == '__main__':
    user_action = input('Вы хотите продолжить? ')
    while user_action.lower() == 'да':
        user_interaction(connection)
        user_action = input('Вы хотите продолжить? ')

