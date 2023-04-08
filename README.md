# Данная программа позволяет получать информацию о вакансиях с платформ hh.ru и superjob.ru

# Проект содержит:
# 1) Модуль engine_requests.py, позволяющий получить данные с сайта через request и API сайтов.
# 2) Модуль vacancy_classes.py для создания объектов-вакансий с необходимыми данными
# 3) Модуль connector_classes.py, позволяющий записать данные в файл с форматом .json или .txt, а также осуществлять работу с этим файлом (чтение, сортировка, удаление)
# 4) user_interaction.py с функцией для работы с файлом

# Для старта программы необходимо запустить файл main.py и вводить запрашиваемые данные с соблюдением предложенного формата ответа (если есть)

# Зависимости указаны в файлах poetry.toml и poetry.lock