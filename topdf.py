import pdfkit
from markdown import markdown

def md2pdf():
    input = "C:\\Users\\28230\\Desktop\\database\\lab3\\query_result.md"
    output = "C:\\Users\\28230\\Desktop\\database\\lab3\\query_result.docx"

    with open(input, encoding='utf-8') as f:
        text = f.read()

    html = markdown(text, output_format='html')  # MarkDown转HTML

    htmltopdf = 'D:\\htmltopdf\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    configuration = pdfkit.configuration(wkhtmltopdf=htmltopdf)
    pdfkit.from_string(html, output_path=output, configuration=configuration, options={'encoding': 'utf-8'})  # HTML转PDF

    
    """with open(input, encoding='utf-8') as f:
        text = f.read()
    
    html = markdown(text, output_format='html')  # MarkDown转HTML
    
    
    htmltopdf = r'D:\\htmltopdf\wkhtmltopdf\bin\wkhtmltopdf.exe'
    configuration = pdfkit.configuration(wkhtmltopdf=htmltopdf)
    pdfkit.from_string(html, output_path=output, configuration=configuration, options={'encoding': 'utf-8'})  # HTML转PDF"""
