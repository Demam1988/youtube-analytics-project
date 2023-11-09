import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    api_key = 'AIzaSyBye8OSheiQHAy-_tHT7JKneRcHzc9hcig'
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализирует id канала. Дальше все данные будут подтягиваться по API"""
        self.channel_id = channel_id


    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале"""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))


class Video:
    def __init__(self, video_id: str):
        self.id_video = video_id
        video_response = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                          id=video_id).execute()
        self.title: str = video_response['items'][0]['snippet']['title']

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=os.getenv('AIzaSyDNal8EcMuEsVzrNkIdbkMWo2d_Nu6w2PI'))
