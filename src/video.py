import json
import os


from googleapiclient.discovery import build

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('API_KEY_2')

class Video():
    api_key: str = os.getenv('API_KEY_2')

    def __init__(self, video_id):
        self.video_id = video_id
        self.title = self.video_to_print()['items'][0]['snippet']['title']
        self.video_url = self.video_to_print()['items'][0]['snippet']['thumbnails']['default']['url']
        self.view_count = self.video_to_print()['items'][0]['statistics']['viewCount']
        self.like_count = self.video_to_print()['items'][0]['statistics']['likeCount']

    @classmethod
    def get_service(cls):
        """создать специальный объект для работы с API"""
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def video_to_print(self):
        """Добавляет в список данные канала"""
        video_list = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails', id=self.video_id).execute()
        return video_list
    #     video_file = 'video.json'
    #     with open (video_file, 'w') as f:
    #         json.dump(video_list, f)
    #
    # def load_file(self, video_file):
    #      with open (video_file, 'r') as f:
    #           data = json.load(f)
    #      return data

    def __str__(self):
         return f"{self.title}"
#
class PLvideo(Video):
     def __init__(self, video_id, playlist_id):
         super().__init__(video_id)
         self.playlist_id = playlist_id
         self.title = self.video_to_print()['items'][0]['snippet']['title']
         self.video_url = self.video_to_print()['items'][0]['snippet']['thumbnails']['default']['url']
         self.view_count = self.video_to_print()['items'][0]['statistics']['viewCount']
         self.like_count = self.video_to_print()['items'][0]['statistics']['likeCount']

#
     def play_to_json(self) :
         """Добавляет в список данные канала"""
         playlist = self.get_service( ).playlistItems().list(playlistId=self.playlist_id, part='contentDetails', maxResults=50).execute()
         return playlist

#         # return video_list
#         play_file = 'playlist.json'
#         with open (play_file, 'w') as f :
#             json.dump (playlist, f)
#
#     def load_playfile(self, play_file) :
#         with open (play_file, 'r') as f :
#             data = json.load (f)
#         return data

video1 = Video('9lO06Zxhu88')
video2 = PLvideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')

print(video1)
print(video2)
#print(video2.video_id)
#print(video1.video_to_json())
#print(video2.play_to_json())
#video1.loa
# d_file('video.json')
#print(video2.load_file('video.json'))
