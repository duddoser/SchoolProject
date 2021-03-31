from flask import Flask, make_response, jsonify, request
from UniversityProcess import University


app = Flask(__name__)
app.config['SECRET_KEY'] = 'android_game_secret_key'
uni_process = University()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/get_unversities', methods=["POST"])
def get_universities():
    university_list = uni_process.get_universities()
    return jsonify({'universities': university_list})


@app.route('/get_faculties', methods=["POST"])
def get_faculties():
    result = request.get_json()
    subjects = [s for s in result['subjects']]
    unis = [u for u in result['universities']]
    snippet = uni_process.get_faculties(unis, subjects)
    return jsonify(snippet)


if __name__ == '__main__':
    app.run()
