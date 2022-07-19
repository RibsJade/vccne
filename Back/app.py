from flask import Flask, jsonify, request
import os
import shutil

import sys


app = Flask(__name__)


def saveFile(directory, file, allowed):
    message = None
    if file.filename != '':
        name, fileext = os.path.splitext(file.filename)
        if fileext.lower() in allowed:
            filepath = os.path.join(directory, file.filename)
            if os.path.exists(filepath):
                os.remove(filepath)
            file.save(filepath)
        else:
            str_allowed = ""
            if len(allowed) > 1:
                for i in allowed:
                    str_allowed = str_allowed + i + " or "
                str_allowed = str_allowed[:-4]
            else:
                str_allowed = allowed[0]
            message = name+' extension must be '+str_allowed
    else:
        message = 'Please fill in everything!'

    return message


@app.route('/Back/upload', methods=['POST'])
def filehandling():
    if request.method == 'POST':
        directory = request.form.get("username")

        message = []
        if directory != "":
            if not os.path.isdir("users"):
                os.mkdir("users")

            directory = os.path.join("users", directory)
            if os.path.isdir(directory):
                shutil.rmtree(directory)
            os.mkdir(directory)

            file = request.files['file1']  # as is

            allowed = ['.csv']
            temp = saveFile(directory, file, allowed)
            if temp is not None:
                if temp not in message:
                    message.append(temp)

            file = request.files['file2']
            allowed = ['.xls', '.xlsx']
            temp = saveFile(directory, file, allowed)
            if temp is not None:
                if temp not in message:
                    message.append(temp)
            shutil.rmtree(directory)
        else:
            message.append('Please fill in everything!')
        if not message:
            message.append('file uploaded successfully')
        return jsonify(message)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
