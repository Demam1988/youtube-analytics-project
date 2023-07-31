import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""


api_key = '7f6bbe76cc9ec194ef0cfb5f1440783d'
youtube = build('youtube', 'v3', developerKey=api_key)


def __init__(self, channel_id: str) -> None:
    """Экземпляр инициализирует id канала. Дальше все данные будут подтягиваться по API"""
    self.channel_id = channel_id


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


def print_info(self) -> None:
    """Выводит в консоль информацию о канале"""
    channel = self.youtube.channel().list(id=self.channel_id, pert='snippet,statistics').execute()
    print(self.channel_id)
    print(json.dumps(channel, indent=2, ensure_ascii=False))
