#pip install Converter
# Gerekli kütüphane içeri aktarılır
from pdf2docx import Converter

# PDF konumu girilir
pdf_file = r"D:\Egitimler\GDAT_Arda\Instructor\GDAT_9.0_to_GDAT_10.0_CompareDoc.pdf"

# Oluşturulacak docx konumu girilir
docx_file = r"D:\Egitimler\GDAT_Arda\Instructor\example.docx"

# Girdi tipi parametresi
cv = Converter(pdf_file)

# Saklama tipi parametresi
cv.convert(docx_file)

# Dönüşüm sonu kapatma
cv.close()


