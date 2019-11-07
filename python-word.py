import os
from docx import Document 
from docx.shared import Inches
from docx.oxml.ns import qn
from win32com import client as wc
word = wc.Dispatch("Word.Application")

ul=r"C:\\Users\\Jim\\Desktop\\test" #需要处理的文件所在文件夹目录
filenamelist=os.listdir(ul)
for y in range(len(filenamelist)): #for循环处理整个目录下的文件
    doc = word.Documents.Open(ul+"\\"+filenamelist[y])
    for para in doc.paragraphs:
        print(doc.text)
#    doc.font.name = u'宋体'
#    doc.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')
    doc.Save() #12表示docx格式
doc.Close()
word.Quit()
