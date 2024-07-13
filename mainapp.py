from doctest import OutputChecker
import sys 
from pytube import YouTube
import os
from pydub import AudioSegment
from flask import Flask, redirect, url_for, render_template, request, send_from_directory, jsonfy

app = Flask(__name__)
DOWNLOAD_FOLDER = 'downloads'
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download_video', methods=['POST'])
def download_video():
    url = request.form['url']
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_file= audio_stream.download(output_path = DOWNLOAD_FOLDER)
    
    base, ext = os.path.splitext(audio_file)
    mp3_file = base + '.mp3'
    
    AudioSegment.from_file(audio_file).export(mp3_file, format="mp3")
    os.remove(audio_file)
    
    filename= os.path.basename(mp3_file)
    return render_template('download.html',filename=filename)

@app.route('/download/<filename>')
def serve_file(filename):
    return
    send_from_directory(DOWNLOAD_FOLDER, filename)

@app.route('/api/download', methods=['POST'])
def api_download():
    data=request.get_json()
    url = data['url']
    yt =YouTube(url)
    audio_stream= yt.stream.filter(only_audio=True).first()
    audio_file= audio_stream.download(output_path=DOWNLOAD_FOLDER)

    base.ext=os.path.splitext(audio_file).export(mp3_file, format="mp3")
    os.remove(audio_file)

    filename=os.path.basename(mp3_file)
    return jsonfy(filename=filename, download_url=url_for)('serve_file',
filename=filename, _external=True)

if __name__ == '__main__':
    app.run(debug=True)
