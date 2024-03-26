import re

import pdfminer.high_level
from pdfminer.high_level import extract_pages, extract_text
from flask import Flask, redirect, url_for, render_template, request, flash

app = Flask(__name__)

PDF_PATH = r"D:\TrendalDocumentation.pdf"


@app.route('/')
def main():  # put application's code here
    text = pdfminer.high_level.extract_text(PDF_PATH, maxpages=10)
    return render_template("index.html", text_data=text[:1000])


if __name__ == '__main__':
    app.run(debug=True)
