import subprocess
import json
import os
from GetVids import get_vid_ids
from AudioHandling import transcribe
import progress as pr

VIDEOS_PATH = "./Videos/"

def download(video_id, progress) :

    if pr.is_downloaded(video_id, progress):
        print(f'Video already downloaded: {video_id}.mp4')
    else:
        result = subprocess.run(['yt-dlp', '-P', './Videos','-o', f'"%(id)s"', '--merge-output-format', 'mp4', f'https://youtube.com/watch?v={video_id}'], 
            text=True, check=True)
    
        try: result.check_returncode()
        except CompletedProcessError:
            delete(f'#{video_id}#.mp4') #might be unnecessary
            raise Exception("Download Failed\n")
    
        print(f"Video downloaded: {video_id}.mp4")
        pr.mark_downloaded(video_id, progress)
        

def delete(video_id) :
    try:
        os.remove(f'{VIDEOS_PATH}#{video_id}#.mp4')
    except FileNotFoundError:
        pass

def download_test():
    video_ids = get_vids_ids()
    
    if video_ids:
    
        print(f"Retrieved {len(video_ids)} videos")

        #test download and delete on first vid
        print(f"Testing download on video: {video_ids[0][1]}")

        download(video_ids[0][0])
        
        print(f"Download successful\nDeleting video")
        delete(video_ids[0][0])
    else:
        print("getVidIds failed, json returned is null")

def main ():
    progress = pr.load_progress()
    video_ids = get_vid_ids()

    if video_ids:
        print(f"Retrieved {len(video_ids)} videos")

        i = 1
        for video in video_ids:
            print(f'Downloading video #{i} \n ID: {video[0]}\n Title: {video[1]}')
            
            try: download(video[0], progress)
            except Exception:
                print(f'Skipping video #{i}')
                i += 1
                continue

            text = transcribe(video[0], progress, True)
            print(f'{text["text"]}')
            #TODO processing

    
if __name__=='__main__':

    main()