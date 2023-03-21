from flask import render_template, Flask, request
from testSearchToolsLangChain import main
from claim_extraction.src.pipeline import read_pdf, run


app = Flask(__name__, template_folder='templates', static_folder="assets")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/done', methods=['GET', 'POST'])
def check():
    output = request.form.to_dict()
    print(output)
    # pdf = request.files['myfile']
    query: str = output['claim']
    print(query)
    # if pdf.filename != '':
    #     pdf.save(pdf.filename)
    #     query = run(read_pdf(pdf.filename))
    evaluation = main(query)
    answer = evaluation[0]
    sources = evaluation[1][0]
    # print(answer)
    return render_template('index.html', query=query, answer=answer, sources=sources)

if __name__ == '__main__':
    app.run(debug=True, port=5001)