import json
import os
# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    api_key = 'AIzaSyBye8OSheiQHAy-_tHT7JKneRcHzc9hcig'
    youtube = build('youtube', 'v3', developerKey='AIzaSyBye8OSheiQHAy-_tHT7JKneRcHzc9hcig')
    data = None

    def __init__(self, channel_id: str, id_str=None) -> None:
        """Экземпляр инициализирует id канала. Дальше все данные будут подтягиваться по API"""
        self.data = self.get_data(channel_id)
        self.__channel_id = channel_id
        self.info = self.get_channel_info()
        self.title = self.info['items'][0]['snippet']['title']
        self.description = self.info['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/' + self.info['items'][0]['snippet']['customUrl']
        self.subscriber = int(self.data['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(self.info['items'][0]['statistics']['videoCount'])
        self.viewCount = int(self.info['items'][0]['statistics']['viewCount'])

    def __str__(self):
        return f'{self.title}, {self.url}'

    def __add__(self, other):
        return self.subscriber + other.subscriber

    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def print_info(self) -> None:
        """
        Выводит в консоль информацию о канале в json-подобном удобном
        формате с отступами.
        """

        data = self.get_service().channels().list(id=self.channel_id,
                                                  part='snippet,statistics').execute()
        print(json.dumps(data, indent=2, ensure_ascii=False))

    def to_json(self, json_name):
        """метод для создания .json файла"""
        data = {'channel_id': self.channel_id,
                'channel_title': self.title,
                'channel_description': self.description,
                'channel_url': self.url,
                'channel_video_count': self.video_count,
                'channel_viewCount': self.viewCount}
        with open(json_name, 'w', encoding='utf=8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def __eq__(self, other):
        """ Возвращает True или False (равенство числа подписчиков) """
        if self.validate(other):
            return self.subscriber == other.subscriber

    def __add__(self, other):
        """ Возвращает сумму числа подписчиков двух экземпляров """
        if self.validate(other):
            return self.subscriber + other.subscriber

    def __sub__(self, other):
        """ Возвращает разность числа подписчиков двух экземпляров """
        if self.validate(other):
            return self.subscriber - other.subscriber

    def __lt__(self, other):
        """ Возвращает True или False, по числу подписчиков экземпляров. """
        if self.validate(other):
            return self.subscriber < other.subscriber

    def __le__(self, other):
        """ Возвращает True или False, по числу подписчиков экземпляров. """
        if self.validate(other):
            return self.subscriber <= other.subscriber

    def __gt__(self, other):
        """ Возвращает True или False, по числу подписчиков экземпляров. """
        if self.validate(other):
            return self.subscriber > other.subscriber

    def __ge__(self, other):
        """ Возвращает True или False, по числу подписчиков экземпляров. """
        if self.validate(other):
            return self.subscriber >= other.subscriber

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey='AIzaSyBye8OSheiQHAy-_tHT7JKneRcHzc9hcig')

    def get_channel_info(self):
        return self.get_service().channels().list(id=self.__channel_id, part="snippet,statistics").execute()

    @property
    def channel_id(self):
        """ Возвращаем id канала. """
        return self.__channel_id

    @classmethod
    def validate(cls, obj):
        """ Проверяет принадлежность объекта к классу Channel. """
        if not isinstance(obj, Channel):
            raise TypeError('Операнд справа должен быть экземпляром класса''Channel!')
        return True

    @classmethod
    def get_data(cls, channel_id):
        """ Получает данные от YouTube. """
        cls.youtube = cls.get_service()
        cls.data = cls.youtube.channels().list(id=channel_id,part='snippet,statistics').execute()
        return cls.data
