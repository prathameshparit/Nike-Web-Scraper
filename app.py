import webbrowser
import pandas as pd
import numpy as np
from nikescrap import nike_scrap
from IPython.core.display import HTML
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/form', methods=['GET', 'POST'])
def form():
    global data
    error = ''

    def path_to_image_html(path):
        return '<img src="' + path + '" width="60" >'

    if request.method == "POST":

        count = request.form.get("count")

        anchor = request.form.get("anchor")

        country = request.form.get("country")

        country_language = request.form.get("country_language")

        query = request.form.get("query")

        data = [count, anchor, country, country_language, query]

        data_csv = nike_scrap(int(count), int(anchor), country, country_language, query)

        if (len(error) == 0):
            return render_template("results.html",
                                   data=HTML(data_csv.to_html(classes='mystyle', index=False, escape=False,
                                                              formatters=dict(ImageURL=path_to_image_html))))
        else:
            return render_template('index.html', error=error)

    return render_template("form.html")


@app.route('/test', methods=['GET', 'POST'])
def test():
    global data
    error = ''

    def path_to_image_html(path):
        return '<img src="' + path + '" width="60" >'

    if request.method == "POST":

        count = request.form.get("count")

        anchor = request.form.get("anchor")

        country = request.form.get("country")

        country_language = request.form.get("country_language")

        query = request.form.get("query")

        data = [count, anchor, country, country_language, query]

        data_csv = nike_scrap(int(count), int(anchor), country, country_language, query)

        if (len(error) == 0):
            return render_template("results.html",
                                   data=HTML(data_csv.to_html(classes='mystyle', index=False, escape=False,
                                                              formatters=dict(ImageURL=path_to_image_html))))
        else:
            return render_template('index.html', error=error)

    return render_template("test.html")


if __name__ == "__main__":
    webbrowser.open_new('http://127.0.0.1:2000/')
    app.run(debug=True, port=2000)
