import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    api_key = 'AIzaSyBye8OSheiQHAy-_tHT7JKneRcHzc9hcig'
        #'AIzaSyBye8OSheiQHAy-_tHT7JKneRcHzc9hcig'
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализирует id канала. Дальше все данные будут подтягиваться по API"""
        self.channel_id = channel_id
        self.info = self.get_service(channel_id)
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
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet_statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    def to_json(self, param):
        pass


    @classmethod
    def get_service(slc, channel_id):
        return build('youtube', 'v3', developerKey='AIzaSyBye8OSheiQHAy-_tHT7JKneRcHzc9hcig')

