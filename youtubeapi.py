import os
from googleapiclient.discovery import build
import requests
import json
from secrets import *
import csv

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
youtube = build('youtube', 'v3', developerKey="AIzaSyDBAQwtfnUb2XEs-vfXnOTcALWe5j60Fk8")

def get_video_stats(ids):
   
    stats_list = []

    for i in range(0, len(ids), 25):
        request= youtube.videos().list(
            part="statistics",
            id=ids[i:i+25]
        )

        data = request.execute()
        for video in data['items']:
            view_count=video['statistics'].get('viewCount',0)
            like_count=video['statistics'].get('likeCount',0)
            dislike_count=video['statistics'].get('dislikeCount',0)
            comment_count=video['statistics'].get('commentCount',0)
            stats_dict=dict(view_count=view_count, like_count=like_count, dislike_count=dislike_count, comment_count=comment_count)
            stats_list.append(stats_dict)

    return stats_list


def main():
    # test with despacito
    ids = ["kJQP7kiw5Fk"]
    print(get_video_stats(ids))

if __name__ == "__main__":
    main()