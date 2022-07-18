from flask import Flask, jsonify, request
import os
import shutil

import sys


app = Flask(__name__)


def saveFile(directory, file, allowed):
    errors = []
    if file.filename != '':
        name, fileext = os.path.splitext(file.filename)
        if fileext.lower() in allowed:
            filepath = os.path.join(directory, file.filename)
            if os.path.exists(filepath):
                os.remove(filepath)
            file.save(filepath)
            print("indicator daw be: "+directory, file=sys.stderr)
        else:
            str_allowed = ""
            if len(allowed) > 1:
                for i in allowed:
                    str_allowed = str_allowed + i + " or "
                str_allowed = str_allowed[:-4]
            else:
                str_allowed = allowed[0]
            errors.append(name+'extension must be '+str_allowed)
    else:
        errors.append('Please fill in everything!')

    return errors


@app.route('/Back/upload', methods=['POST'])
def filehandling():
    if request.method == 'POST':
        directory = request.form.get("username")

        if not os.path.isdir("users"):
            os.mkdir("users")

        errors = []
        if directory != "":
            directory = os.path.join("users", directory)
            if os.path.isdir(directory):
                shutil.rmtree(directory)
            os.mkdir(directory)

            file = request.files['file1']  # as is

            allowed = ['.csv']
            temp = saveFile(directory, file, allowed)
            errors += temp

            file = request.files['file2']
            allowed = ['.xls', '.xlsx']
            temp = saveFile(directory, file, allowed)
            errors += temp
            print(temp, file=sys.stderr)
        else:
            errors.append('Please fill in everything!')
        shutil.rmtree(directory)
        if not errors:
            return jsonify('file uploaded successfully')
        else:
            return jsonify(errors)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
