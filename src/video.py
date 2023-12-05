import os

from googleapiclient.discovery import build

api_key = os.getenv('YT_API_KEY')


class Video:
    """ Класс для видео ютуб-канала. """

    data = None
    youtube = None

    def __init__(self, id_video: object) -> object:
        self.data = self.get_data(id_video)
        self.id_video = id_video
        try:
            self.title = self.data['items'][0]['snippet']['title']
            self.viewers = self.data['items'][0]['statistics']['viewCount']
            self.like_count = int(self.data['items'][0]['statistics']['likeCount'])
            self.url = f'https://www.youtube.com/watch?v={self.id_video}'
        except IndexError:
            self.title = self.viewers = self.like_count = self.url = None

    @classmethod
    def get_service(cls):
        """ Возвращает объект для работы с YouTube API. """

        cls.youtube = build('youtube', 'v3', developerKey=api_key)
        return cls.youtube

    @classmethod
    def get_data(cls, id_str):
        """ Получает данные от YouTube. """

        cls.youtube = cls.get_service()
        cls.data = cls.youtube.videos().list(id=id_str, part='snippet, ' \
                                                             'statistics').execute()
        return cls.data

    @classmethod
    def validate(cls, obj):
        """ Проверяет принадлежность объекта к классу Video. """

        if not isinstance(obj, Video):
            raise TypeError('Операнд справа должен быть экземпляром класса '
                            'Video!')
        return True

    def __str__(self):
        """ Строковое представление экземпляра: наименование канала. """

        return f'{self.title}'

    def __lt__(self, other):
        """ Возвращает True или False, по числу likes экземпляров. """

        if self.validate(other):
            return self.like_count < other.like_count


class PLVideo(Video):
    """ Класс для плейлистов ютуб-канала. """

    def __init__(self, id_video, id_playlist):
        super().__init__(id_video)
        self.id_playlist = id_playlist