import os
from abc import ABC, abstractmethod
import json


class Connector(ABC):
    """Abstract class for writing information to some file"""

    @abstractmethod
    def insert_hh(self, data_to_save):
        pass

    @abstractmethod
    def insert_sj(self, data_to_save):
        pass

    @abstractmethod
    def select_data(self, parameter, clue):
        pass


class ConnectorJson(Connector):
    """Class for working with json file"""

    def __init__(self, filename='vacancies.json'):
        """Make file with given filename"""
        self.filepath = f'..\src\{filename}'

        if not os.path.exists(self.filepath):
            file = open(self.filepath, 'w', encoding='utf8')
            file.close()
        elif filename[-5:] != '.json':
            raise NameError('Wrong format. Correct format filename.json')
        else:
            raise OSError('File already exists. Choose a different filename')

        self.__file = filename

    @property
    def filename(self):
        """Getter for filename"""
        return self.__file

    @filename.setter
    def filename(self, new_name):
        """Setter for new filename"""
        if new_name[-5:] == '.json':
            os.rename(self.filepath, f'../src/{new_name}')
            self.__file = new_name
        else:
            raise NameError('Wrong format. Correct format filename.json')

    def insert_hh(self, data_to_save: dict):
        """Write into the file hh vacancies object by object"""

        with open(self.filepath, 'a', encoding='utf-8') as f:
            json.dump(data_to_save, f, ensure_ascii=False)
            f.write(',')
            f.write('\n')

    def insert_sj(self, data_to_save):
        """Write into the file sj vacancies object by object"""

        with open(self.filepath, 'a', encoding='utf-8') as f:
            json.dump(data_to_save, f, ensure_ascii=False)
            f.write(',')
            f.write('\n')

    def select_data(self, parameter, clue):
        """Select data by parameter and clue"""
        result = []

        with open(self.filepath, 'r', encoding='utf-8') as f:
            text = f.read()
            text_divided = f'[{text.strip().strip(",")}]'

        data = json.loads(text_divided)

        for item in data:
            try:
                if item[parameter] == clue or clue in item[parameter]:
                    result.append(item)
            except KeyError:
                print('This parameter does not exist. Please choose another')

        if len(result) == 0:
            print('There is no data for this parameter ')
        return result

    def select_by_salary(self, clue_from, clue_to):
        """Select data by salary"""
        result = []

        with open(self.filepath, 'r', encoding='utf-8') as f:
            text = f.read()
            text_divided = f'[{text.strip().strip(",")}]'

        data = json.loads(text_divided)

        for item in data:
            if clue_to and clue_from:
                if item['Нижняя граница з/п'] >= clue_from and item['Верхняя граница з/п'] <= clue_to:
                    result.append(item)
            elif clue_to:
                if item['Верхняя граница з/п'] <= clue_to:
                    result.append(item)
            elif clue_from:
                if item['Нижняя граница з/п'] >= clue_from:
                    result.append(item)

        if len(result) == 0:
            print('There is no data for this parameter ')
        return result

    def delete_data(self):
        pass

    def delete_data_by_clue(self, parameter, clue):
        pass
