from flask import Flask, render_template
from modules.dbConnection import cur, look_for_sign

app = Flask(__name__)


@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html',
                           the_title='Перед началом закройте глаза на 30 секунд')


@app.route('/results', methods=['POST', 'GET'])
def results_page():
    result = look_for_sign(cur)
    return render_template('results.html',
                           the_title='Подумайте, может в этом что-то есть?',
                           the_sign=result)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int("80"))
