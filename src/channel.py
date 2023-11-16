import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    api_key = 'AIzaSyBye8OSheiQHAy-_tHT7JKneRcHzc9hcig'
    youtube = build('youtube', 'v3', developerKey='AIzaSyBye8OSheiQHAy-_tHT7JKneRcHzc9hcig')


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализирует id канала. Дальше все данные будут подтягиваться по API"""
        self._channel_id = None
        self.__channel_id = channel_id
        self.info = self.get_channel_info
        self.title = self.info['items'][0]['snippet']['title']
        self.description = self.info['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/' + self.info['items'][0]['snippet']['customUrl']
        self.video_count = int(self.info['items'][0]['statistics']['videoCount'])
        self.viewCount = int(self.info['items'][0]['statistics']['viewCount'])

    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале"""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    def to_json(self, json_name):
        '''метод для создания .json файла'''
        data = {'channel_id': self.channel_id,
                'channel_title': self.title,
                'channel_description': self.description,
                'channel_url': self.url,
                'channel_video_count': self.video_count,
                'channel_viewCount': self.viewCount}
        with open(json_name, 'w', encoding='utf=8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey='AIzaSyBye8OSheiQHAy-_tHT7JKneRcHzc9hcig')

    def get_channel_info(self):
        return self.get_service().channels().list(id=self.__channel_id, part="snippet,statistics").execute()

    @property
    def channel_id(self):
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
