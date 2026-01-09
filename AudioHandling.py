import whisper

VIDEOS_PATH = "./Videos/"
TRANSCRIPT_PATH = "./Transcripts/"

model = whisper.load_model("base.en")
options = whisper.DecodingOptions(language="en",without_timestamps=True)

writer = whisper.utils.get_writer("txt", f'{TRANSCRIPT_PATH}')

def transcribe (videoId, transcribe=False) :
    result = model.transcribe(f'{VIDEOS_PATH}#{videoId}#.mp4', word_timestamps=True)
    
    if transcribe:
        writer(result, f'{videoId}.txt')
    
    return result