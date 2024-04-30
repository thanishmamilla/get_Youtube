from flask import Flask, render_template, request, jsonify,send_file
from pytube import YouTube
import base64
from pytube.exceptions import RegexMatchError, VideoUnavailable
from flask_cors import CORS


app = Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/submitform",methods=[ "POST"])
def videodownload():
    link=request.form['url']
    try:
        # link = "https://youtube.com/shorts/L4AWZDRbpQM?si=dO_bswFJLItlA7IX"
        print(link)
        video = YouTube(link,allow_oauth_cache=True)
        video_stream = video.streams.get_highest_resolution()
        video_path = f"videos.mp4"
        # video_stream.download()
        video_stream.download(output_path="static", filename=video_path)
        print("YouTube video downloaded successfully")
        return send_file(f"static/{video_path}",as_attachment=True)


    except Exception as e:
        return jsonify({"error":e})
    

if __name__== '__main__':
    app.run(host='0.0.0.0',port=5001)
    


