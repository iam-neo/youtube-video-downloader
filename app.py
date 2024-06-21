from flask import Flask, render_template, request, redirect, url_for, send_file
from pytube import YouTube
import os

app = Flask(__name__)
video_streams = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global video_streams
    thumbnail_url = None
    if request.method == 'POST':
        url = request.form['url']
        try:
            yt = YouTube(url)
            video_streams = yt.streams.filter(progressive=True, file_extension='mp4').all()
            thumbnail_url = yt.thumbnail_url
            return render_template('index.html', streams=enumerate(video_streams), thumbnail_url=thumbnail_url)
        except Exception as e:
            return str(e)
    return render_template('index.html', streams=None, thumbnail_url=thumbnail_url)

@app.route('/download/<int:stream_index>', methods=['GET'])
def download(stream_index):
    try:
        stream = video_streams[stream_index]
        file_path = stream.download()
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
