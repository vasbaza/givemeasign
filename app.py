from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)


@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


@app.route('/search4', methods=['POST', 'GET'])
def do_search():
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           the_letters=letters,
                           the_phrase=phrase,
                           the_results=results,
                           the_title=title)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int("80"))
