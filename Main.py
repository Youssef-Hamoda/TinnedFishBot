import subprocess
import json
import os

def getVidIds() :
    result = subprocess.run(['ruby', 'YtApiCall.rb'],                                   #call YtApiCall
        capture_output=True, text=True)   
    return json.loads(result.stdout)                                                    #recieve json

def download(video_id) :
    result = subprocess.run(['yt-dlp', '-P', './Videos', '-o', f'{video_id}.mp4', f'https://youtube.com/watch?v={video_id}'], 
        text=True, check=True)
    if (result.check_returncode() != 0):
        delete(f'./Videos/{video_id}.mp4')
        return -1

def delete(video_path) :
    subprocess.run(['rm', '-f', f'{video_path}'])

