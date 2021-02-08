#!/usr/bin/env python3

import codecs
import mmh3

from flask import Flask, render_template, redirect, request

app = Flask(__name__)
version = '0.1.0'

# Limit uploads to 32k max
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024

# https://en.wikipedia.org/wiki/Favicon#File_format_support
ALLOWED_EXTENSIONS = ['ico', 'png', 'gif', 'jpeg', 'jpg', 'svg']

# Should do more extensive checks obviously
def allowed_ext(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def front():
    return render_template('index.html', version=version)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        try:
            f = request.files['file']

            if allowed_ext(f.filename):
                data = f.stream.read()
                favicon = codecs.encode(data, 'base64')
                hash = mmh3.hash(favicon)
            else:
                return render_template('error.html', error='Invalid file extension', version=version)
        except Exception as e:
            return render_template('error.html', error=e, version=version)

        return render_template('result.html', hash=str(hash), version=version)
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run()
