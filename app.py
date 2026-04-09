from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = None
    msg_type = None

    if request.method == "POST":
        singer = request.form.get("singer")
        videos = int(request.form.get("videos", 0))
        duration = int(request.form.get("duration", 0))
        email = request.form.get("email")

        
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        
        if videos <= 10:
            message, msg_type = "Number of videos must be greater than 10.", "error"
        elif duration <= 20:
            message, msg_type = "Audio duration must be greater than 20 seconds.", "error"
        elif not re.match(email_regex, email):
            message, msg_type = "Invalid email format.", "error"
        else:
            
            message, msg_type = f"Success! Processing {videos} videos of {singer} and sending to {email}.", "success"

    return render_template("index.html", message=message, msg_type=msg_type)


if __name__ == "__main__":
    app.run(debug=True)