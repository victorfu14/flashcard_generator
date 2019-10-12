from flask import Flask, render_template, make_response, send_from_directory
from flask import redirect, request, jsonify, url_for
from getKeyWords import sample_analyze_entities
from fill_blanks import get_blank_questions


app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return render_template('index.html', title='Flashcard Generator')


@app.route("/input-page")
def input_page():
    return render_template('input_page.html', title='Flashcard Generator')


@app.route("/submit-text", methods=['POST'])
def submit_text():
    text = request.form.get('text')
    keywords = sample_analyze_entities(text)
    # Return them
    return render_template('keyword_return.html', keywords=keywords, text=text, title='Customize Your Preference')


@app.route("/submit-keywords", methods=['POST'])
def make_flashcards():
    text = request.form.get('text')
    keywords = request.form.get('keywords').split(",")
    questions = get_blank_questions(text, keywords)
    # Generate PDF flash cards
    # Return them using send_from_directory
    return "1"


if __name__ == "__main__":
    app.run()
