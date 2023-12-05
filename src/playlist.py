import datetime
import os

import isodate
from googleapiclient.discovery import build

from src.video import Video, PLVideo

api_key = os.getenv('YT_API_KEY')


class MixVideo:
    """
    Класс с методами получения данных по видеороликам в плейлисте и получением
    списка их id.
    """
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, id_playlist):
        self.id_playlist = id_playlist

    def get_video(self):
        """ Получаем данные по видеороликам в плейлисте. """

        video = self.youtube.playlistItems().list(playlistId=self.id_playlist,
                                                  part='contentDetails',
                                                  maxResults=50,
                                                  ).execute()
        return video

    def get_video_id(self):
        """ Получаем все id видеороликов из плейлиста. """

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in
                                self.get_video()['items']]
        return video_ids


class PlayList(MixVideo, PLVideo):

    def __init__(self, id_playlist):
        super().__init__(id_playlist)
        self.data = self.get_data(id_playlist)
        self.title = self.data['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={id_playlist}'

    def get_data(self, id_playlist):
        """ Получает данные от YouTube по id плейлиста. """

        self.data = self.youtube.playlists().list(part='snippet',
                                                  id=id_playlist).execute()
        return self.data

    def show_best_video(self):
        """
        Возвращает ссылку на самое популярное видео из плейлиста (по
        количеству лайков).
        """

        lst_video = []
        for video in self.get_video_id():
            v = Video(video)
            lst_video.append(v)
        return f'https://youtube/{max(lst_video).id_video}'

    @property
    def total_duration(self):
        """
        Возвращает объект класса `datetime.timedelta` с суммарной
        длительность плейлиста.
        """

        video_response = self.youtube.videos().list(
            part='contentDetails,statistics',
            id=','.join(self.get_video_id())
        ).execute()
        total_time = datetime.timedelta()

        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_time += duration
        return total_time
