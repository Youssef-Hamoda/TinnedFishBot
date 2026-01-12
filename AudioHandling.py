import whisper
import progress as pr

VIDEOS_PATH = "./Videos/"
TRANSCRIPT_PATH = "./Transcripts/"

model = whisper.load_model("base.en")
options = whisper.DecodingOptions(language="en",without_timestamps=True)

writer = whisper.utils.get_writer("txt", f'{TRANSCRIPT_PATH}')

def transcribe (videoId, progress, times=False) :
    if pr.is_transcribed(id, progress):
        print(f'Video already trancribed: {videoId}')
    else:
        result = model.transcribe(f'{VIDEOS_PATH}#{videoId}#.mp4', word_timestamps=times)
        writer(result, f'{videoId}.txt')
        
        pr.mark_downloaded(videoId, progress)