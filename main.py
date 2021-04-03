import json
from flask import Flask, make_response, jsonify, request
from UniversityProcess import University
from collections import defaultdict

app = Flask(__name__)
app.config['SECRET_KEY'] = 'school_secret_key'
uni_process = University()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/get_faculties', methods=["POST"])
def get_faculties():
    result = request.get_json()
    subjects = [s for s in result['subjects']]
    return jsonify(get_info(",".join(subjects)))


def get_info(request):
    with open('data.json', encoding='utf-8') as f:
        templates = json.load(f)

    result = defaultdict(list)
    for key in templates:
        for value in templates[key]:
            if value.get(request) is not None:
                for el in value[request]:
                    result[key].append(el + ' - ' + str(value[request][el]))
    return result


if __name__ == '__main__':
    app.run()
