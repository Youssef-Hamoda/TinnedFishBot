import json
import os

def load_progress():
    """Load progress tracking"""
    if os.path.exists('progress.json'):
        with open('progress.json', 'r') as f:
            return json.load(f)
    return {"downloaded": [], "transcribed": []}

def save_progress(progress):
    """Save progress tracking"""
    with open('progress.json', 'w') as f:
        json.dump(progress, f, indent=2)

def is_downloaded(video_id, progress):
    return video_id in progress["downloaded"]

def is_transcribed(video_id, progress):
    return video_id in progress["transcribed"]

def mark_downloaded(video_id, progress):
    if video_id not in progress["downloaded"]:
        progress["downloaded"].append(video_id)
        save_progress(progress)

def mark_transcribed(video_id, progress):
    if video_id not in progress["transcribed"]:
        progress["transcribed"].append(video_id)
        save_progress(progress)
