import json
import os
from src.channel import Channel
from datetime import timedelta



from googleapiclient.discovery import build

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('API_KEY_2')
counter = 0

class PlayList(Channel):
    api_key: str = os.getenv('API_KEY_2')

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.title = self.playlists_to_print()['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={playlist_id}"

    @classmethod
    def get_service(cls):
        """создать специальный объект для работы с API"""
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def playlists_to_print(self):
        """Выгружает данные плэйлистов"""
        playlists = self.get_service().playlists().list(channelId='UC1eFXmJNkjITxPFWTy6RsWg',
                                     part='contentDetails,snippet',
                                     maxResults=50,
                                     ).execute()
        #playlist_videos = playlists.list(playlistId=self.playlist_id,part='contentDetails', maxResults=50).execute ( )
        for playlist in playlists['items']:
            if playlist['id'] == self.playlist_id:
                return playlist

    def get_video_response(self):

        playlist_videos = self.get_service().playlistItems ( ).list (playlistId=self.playlist_id,
                                                          part='contentDetails',
                                                          maxResults=50,
                                                          ).execute ( )

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = self.get_service().videos ( ).list (part='contentDetails,statistics',
                                                  id=','.join (video_ids)
                                                  ).execute ( )
        return video_response

    def get_duration(self):
        time_list = []
        counter = 0
        time = self.get_video_response()['items']
        for t in time:
            tratio = time[counter]['contentDetails']['duration']
            time_list.append(tratio)
            counter += 1
        return time_list

    @property
    def total_duration(self):
            minutes = 0
            seconds = 0
            for z in self.get_duration():
                seconds += int (z[5:7])
                minutes += int(z[2:4])
                total_sec = minutes * 60 + seconds
                total_hours = int (total_sec /3600)
                total_minutes = int((total_sec - total_hours*3600)/60)
                total_seconds = int(total_sec - total_hours*3600 - total_minutes*60)
                delta = timedelta(hours=total_hours, minutes=total_minutes, seconds=total_seconds)

            return delta

    def show_best_video(self):

        videos = self.get_video_response()['items']
        for v in videos:
            best_video = max((videos[counter]['statistics']['likeCount']), key=lambda i: int(i))

        return f"https://youtu.be/{v['id']}"









pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
#print(pl.playlists_to_print())
#print(pl.title)
#print(pl.url)
print(pl.get_duration())
#print(pl.get_video_response())
print(pl.total_duration)
#duration = pl.total_duration
#print(duration)
#print(str(duration))
print(pl.show_best_video())
