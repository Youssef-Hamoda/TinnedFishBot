import subprocess
import json
import os
from GetVids import get_vid_ids

VIDEOS_PATH = "./Videos/"

def get_vids() :
    #API Implementation in GetVids.py
    return get_vid_ids()

def download(video_id) :
    result = subprocess.run(['yt-dlp', '-P', './Videos','-o', f'"%(id)s"', '-t', 'mp4', f'https://youtube.com/watch?v={video_id}'], 
        text=True, check=True)
    
    if (result.check_returncode() != 0):
        delete(f'{video_id}')
        return 1
    
    print(f"Video downloaded: {video_id}.mp4")

def delete(video_id) :
    try:
        os.remove(f'{VIDEOS_PATH}#{video_id}#.mp4')
    except FileNotFoundError:
        pass

def main():
    video_ids = get_vids()
    
    if video_ids:
    
        print(f"Retrieved {len(video_ids)} videos")

        #test download and delete on first vid
        print(f"Testing download on video: {video_ids[0][1]}")

        download(video_ids[0][0])
        
        print(f"Download successful\nDeleting video")
        delete(video_ids[0][0])
    else:
        print("getVidIds failed, json returned is null")
    
if __name__=='__main__':
    main()