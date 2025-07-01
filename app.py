from flask import Flask, request, send_file
from pdf2docx import Converter

app = Flask(_name_)

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    file.save("input.pdf")

    cv = Converter("input.pdf")
    cv.convert("output.docx", start=0, end=None)
    cv.close()

    return send_file("output.docx", as_attachment=True)

if _name_ == "_main_":
    app.run()   
