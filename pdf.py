# https://github.com/aneagoie/watermarker/blob/master/pdf.py

import PyPDF2

# import sys
# 217
# inputs = sys.argv[1:]
# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('super.pdf')
# pdf_combiner(inputs)

# 216
# with open('dummy.pdf', 'rb') as file:
# 22/7/17 rb: read the binary
# reader = PyPDF2.PdfFileReader(file)
# print(reader.numPages)

# 219
template = PyPDF2.PdfFileReader(open('dummy.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    # c.f. numPages
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    # 因為watermark檔只有這一頁
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)
