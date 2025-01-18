from reportlab.pdfgen import canvas

def create_pdf(text_file, output_pdf):
    c = canvas.Canvas(output_pdf)
    with open(text_file, 'r') as f:
        text = f.read()
    textobject = c.beginText(50, 800)
    textobject.textLines(text)
    c.drawText(textobject)
    c.save()

if __name__ == "__main__":
    create_pdf("sample.txt", "sample.pdf")
