import os
from yt_dlp import YoutubeDL

def download_video(video_url):
    try:
        # yt-dlp options
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Best quality video and audio
            'outtmpl': '%(title)s - Episode %(episode_number)s.%(ext)s',  # Filename template
            'merge_output_format': 'mp4',         # Output format as MP4
        }

        # Download video
        with YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading from: {video_url}")
            result = ydl.download([video_url])
            if result == 0:
                print(f"Download complete for: {video_url}")
            else:
                print(f"An error occurred during download from: {video_url}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get multiple video links from the user
    video_links = input("Enter the video links (separated by commas): ").split(',')
    
    # Trim any leading/trailing spaces and download each video
    for link in video_links:
        link = link.strip()  # Remove any extra spaces
        if link:
            download_video(link)
