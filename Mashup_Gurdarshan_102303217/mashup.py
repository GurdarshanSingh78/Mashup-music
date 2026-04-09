import os
import sys
from yt_dlp import YoutubeDL
from pydub import AudioSegment

def download_videos(singer_name, num_videos):
    print(f"Searching and downloading {num_videos} videos for '{singer_name}'...")
    
    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    ydl_opts = {
        'format': 'bestaudio/best',
        'extract_audio': True,
        'outtmpl': 'downloads/%(title)s.%(ext)s', 
        'noplaylist': True,
        'default_search': 'ytsearch',
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"ytsearch{num_videos}:{singer_name} audio"])
        print("Download complete!\n")
    except Exception as e:
        print(f"An error occurred during download: {e}")
        sys.exit(1) # Exit if download fails

def process_audios(duration_sec, output_filename):
    print(f"Processing audios: Cutting first {duration_sec} seconds and merging...")
    
    downloaded_files = [f for f in os.listdir("downloads") if os.path.isfile(os.path.join("downloads", f))]
    
    if not downloaded_files:
        print("Error: No downloaded files found to process.")
        sys.exit(1)

    merged_audio = AudioSegment.empty()
    duration_ms = duration_sec * 1000 

    for file in downloaded_files:
        filepath = os.path.join("downloads", file)
        print(f"Cutting: {file}")
        try:
            audio = AudioSegment.from_file(filepath)
            cut_audio = audio[:duration_ms]
            merged_audio += cut_audio
        except Exception as e:
            print(f"Error processing {file}: {e}")

    print(f"\nSaving final mashup as '{output_filename}'...")
    try:
        merged_audio.export(output_filename, format="mp3")
        print("Mashup created successfully!")
    except Exception as e:
        print(f"Error saving file: {e}")

def main():
    
    if len(sys.argv) != 5:
        print("Error: Incorrect number of parameters.")
        print("Usage: python 102303217.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        sys.exit(1)

    singer_name = sys.argv[1]

    
    try:
        num_videos = int(sys.argv[2])
        if num_videos <= 10:
            print("Error: Number of videos (N) must be greater than 10.")
            sys.exit(1)
    except ValueError:
        print("Error: Number of videos must be an integer.")
        sys.exit(1)

    
    try:
        audio_duration = int(sys.argv[3])
        if audio_duration <= 20:
            print("Error: Audio duration (Y) must be greater than 20 seconds.")
            sys.exit(1)
    except ValueError:
        print("Error: Audio duration must be an integer.")
        sys.exit(1)

    output_filename = sys.argv[4]
    
    
    if not output_filename.endswith('.mp3'):
        output_filename += '.mp3'

    
    download_videos(singer_name, num_videos)
    process_audios(audio_duration, output_filename)

if __name__ == "__main__":
    main()