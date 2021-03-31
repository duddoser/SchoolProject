from flask import Flask, make_response, jsonify, request
from UniversityProcess import University


app = Flask(__name__)
app.config['SECRET_KEY'] = 'android_secret_key'
uni_process = University()
UNIVERSITY_DICT = uni_process.get_universities()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/get_universities', methods=["POST"])
def get_universities():
    result = request.get_json()
    subjects = []
    for el in result:
        subjects.append(el)
    snippet = uni_process.get_faculties(UNIVERSITY_DICT, subjects)
    return jsonify(snippet)


if __name__ == '__main__':
    app.run()
