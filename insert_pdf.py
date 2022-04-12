from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import xml_to_csv

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
can.drawString(170, 766, xml_to_csv.read_value("/path/to/Chun Hsin Dia 35 OV TR17.xml"))
can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)

# create a new PDF with Reportlab
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("/path/to/Prestige 20 Header Settings Form V2.0.pdf", "rb"))
first_page = existing_pdf.getPage(0)
print(first_page.extractText())

#print(existing_pdf.getPage(0)['/Contents'])

#for elem in existing_pdf.getPage(0)['/Resources']['/ProcSet']:
#    print(elem)


output = PdfFileWriter()
#output.updatePageFormFieldValues(1, )
#exit
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = open("output.pdf", "wb")
output.write(outputStream)
outputStream.close()
