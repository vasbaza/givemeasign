from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)


@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html',
                           the_title='Позвольте вашему мозгу работать за Вас')

@app.route('/results', methods=['POST', 'GET'])
def results_page():
    return render_template('results.html',
                           the_title='Подумайте, может в этом что-то есть?')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int("80"))
