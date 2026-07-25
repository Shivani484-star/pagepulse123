from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    user_text = ""
    word_count = 0
    char_count = 0
    
    if request.method == 'POST':
        user_text = request.form.get('user_text')
        word_count = len(user_text.split())
        char_count = len(user_text)
        
        # Save to file
        with open("messages.txt", "a", encoding="utf-8") as f:
            f.write(user_text + "\n")

    return render_template("index.html", text=user_text, w=word_count, c=char_count)

if __name__ == "__main__":
    app.run(debug=True)
