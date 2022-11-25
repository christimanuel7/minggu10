from flask import Flask, render_template
import pdfkit
import os

app=Flask(__name__)
app.config['PDF_FOLDER']=os.path.realpath('')+'/static/pdf'
app.config['TEMPLATE_FOLDER']=os.path.realpath('')+'/templates'
path_wkhtmltopdf=b'D:\\31190086_Christopher Imanuel\wkhtml\wkhtmltopdf\\bin\wkhtmltopdf.exe'
config=pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/konversi')
def konversi():
    htmlfile=app.config['TEMPLATE_FOLDER']+'/index.html'
    pdffile = app.config['PDF_FOLDER'] + '/demo4.pdf'
    pdfkit.from_file(htmlfile,pdffile,configuration=config)
    return'''
        Proses konversi ke PDF telah berhasil. <br />
        Klik <a href="http://localhost:5000/static/pdf/demo4.pdf">di sini</a>
        untuk membuka file tersebut
        '''

if __name__=='__main__':
    app.run(debug=True)