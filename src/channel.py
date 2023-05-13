import json
import os

from googleapiclient.discovery import build

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('API_KEY_2')

class Channel:
    """"Класс для ютуб-канала"""
    api_key: str = os.getenv('API_KEY_2')

    def __init__(self, channel_id='UCMCgOm8GZkHp8zJ6l7_hIuA'):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.title = self.print_info()['items'][0]['snippet']['title']
        self.description = self.print_info()['items'][0]['snippet']['description']
        self.url = self.print_info()['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscriber = self.print_info()['items'][0]['statistics']['subscriberCount']
        self.video_count = self.print_info()['items'][0]['statistics']['videoCount']
        self.view_count = self.print_info()['items'][0]['statistics']['viewCount']

    @property
    def channel_id(self):
        return self.__channel_id
    @channel_id.setter
    def channel_id(self, channel_id=None):
        if channel_id == None:
            self.__channel_id
        else:
            raise ValueError(f"# AttributeError: property 'channel_id' of 'Channel' object has no setter")

    @classmethod
    def get_service(cls):
        """создать специальный объект для работы с API"""
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        channel = self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        return channel

    def to_json(self, youtube_file):
        youtube_file = 'vdud.json'
        json_data = {"title": self.title, "description": self.description, "url": self.url, "subscriber": self.subscriber, "video_count": self.video_count, "video_view": self.view_count}
        with open(youtube_file, 'w') as f:
            json.dump(json_data, f)

#vdud = Channel()
#print(vdud.print_info())
#print(vdud.title)
#print(vdud.description)
#print(vdud.url)
#print(vdud.subscriber)
#print(vdud.video)
#print(vdud.view)
#print(Channel.get_service())
#print(vdud.channel_id)
#print(vdud.channel_id)
#vdud.channel_id = "sss"
#vdud.to_json('vdud.json')





