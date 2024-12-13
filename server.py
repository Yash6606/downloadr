from flask import Flask, render_template, request, send_file
import yt_dlp

app = Flask(__name__)

# Function to download Instagram Reel
def download_instagram_reel(reel_url):
    try:
        ydl_opts = {
            'outtmpl': 'static/reel_video.mp4',  # Save to 'static' folder
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([reel_url])
        return 'static/reel_video.mp4'
    except Exception as e:
        return str(e)

# Function to download YouTube Video
def download_youtube_video(youtube_url):
    try:
        ydl_opts = {
            'outtmpl': 'static/youtube_video.mp4',  # Save to 'static' folder
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        return 'static/youtube_video.mp4'
    except Exception as e:
        return str(e)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        platform = request.form.get("platform")

        if platform == "instagram":
            file_path = download_instagram_reel(url)
        elif platform == "youtube":
            file_path = download_youtube_video(url)
        else:
            file_path = "Invalid platform"

        if file_path.startswith('static'):
            return send_file(file_path, as_attachment=True)
        else:
            return f"Error: {file_path}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)