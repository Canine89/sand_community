from rest_framework.response import Response
from rest_framework.views import APIView
from PyPDF2 import PdfFileWriter, PdfFileReader
from django.http import HttpResponse

import io

# Create your views here.
class TransformPdf(APIView):
    def post(self, request, format=None):
        src_file = request.FILES['file']
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment;filename="somefilename.pdf"'
        
        if src_file.content_type == 'application/pdf':
            read_pdf = src_file.read()            
            pdf_file = PdfFileReader(io.BytesIO(read_pdf))
            pdf_file_for_left = PdfFileReader(io.BytesIO(read_pdf))
            pdf_file_for_right = PdfFileReader(io.BytesIO(read_pdf))

            output_pdf_file = PdfFileWriter()

            # print("total page is", pdf_file.getNumPages())
            full_width_size = 0.0
            for i in range(pdf_file.getNumPages()):
                page = pdf_file.getPage(i)
                
                if full_width_size < page.mediaBox.upperRight[0].as_numeric():
                    full_width_size = page.mediaBox.upperRight[0]

            # print("full width size is", full_width_size)

            for i in range(pdf_file.getNumPages()):
                # print("this is", i, "page.")
                # print("upperRight is", pdf_file.getPage(i).mediaBox.upperRight[0])
                if(full_width_size != pdf_file.getPage(i).mediaBox.upperRight[0]):
                    page = pdf_file.getPage(i)
                    output_pdf_file.addPage(page)
                    continue

                # print("cutting work...")
                # print(pdf_file.getPage(i))
                page_left = pdf_file_for_left.getPage(i)
                page_right = pdf_file_for_right.getPage(i)    
                
                # left
                page_left.cropBox.lowerLeft = (0, 0)
                page_left.cropBox.upperRight = (page_left.mediaBox.upperRight[0] / 2, page_left.mediaBox.upperRight[1])
                output_pdf_file.addPage(page_left)

                # right
                page_right.cropBox.lowerLeft = (page_right.mediaBox.upperRight[0] / 2, 0)
                page_right.cropBox.upperRight = (page_right.mediaBox.upperRight[0], page_right.mediaBox.upperRight[1])
                output_pdf_file.addPage(page_right)

            output_pdf_file.write(response)

        return response