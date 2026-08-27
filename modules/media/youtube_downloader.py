import os
print("--- YouTube Downloader ---")
url = input("Enter YouTube URL: ") 
os.system(f"yt-dlp {url}")