import re

import pdfminer.high_level
from pdfminer.high_level import extract_pages, extract_text
from flask import Flask, redirect, url_for, render_template, request, flash

app = Flask(__name__)

PDF_PATH = r"C:\Users\Ibrahim\TrendallProject\RVP.pdf"


@app.route('/')
def main():  # put application's code here
    #text = pdfminer.high_level.extract_text(PDF_PATH, maxpages=10)
    keyword = "PLATE"
    sentences = []
    text = extract_text(PDF_PATH)
    index = text.find("GENERAL INTRODUCTION")
    sentence_list = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text[index:])
    for sentence in sentence_list:
        if keyword.lower() in sentence.lower():
            sentences.append(sentence)
            if len(sentences) == 50:
                break   
    return render_template("index.html", text_data=sentences)
    


if __name__ == '__main__':
    app.run(debug=True)
