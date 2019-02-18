#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import pandas as pd
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from pdfminer.converter import PDFPageAggregator

base_path = r"C:\Users\Menda Jawahar\Desktop\PDF"
my_file = os.path.join(base_path + "/" + "IV India Offer Letter_Menda Jawahar - signed (1).pdf")

fp = open(my_file, "rb")
parser = PDFParser(fp)
document = PDFDocument(parser)
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)

extracted_text = ""
for page in PDFPage.create_pages(document):
    interpreter.process_page(page)
    layout = device.get_result()
    for lt_obj in layout:
        if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
            extracted_text += lt_obj.get_text()

l1=[]
for line in extracted_text.splitlines():
    l1.append(line)

pos1000=l1.index('1,000+ EMPLOYEES')
pos500=l1.index('500-999 EMPLOYEES')
pos250=l1.index('250-499 EMPLOYEES')
poslast=l1.index('Steel Fabricator')
import re

list_of_1000=l1[pos1000+1:pos500]
list_of_500=l1[pos500+1:pos250]
list_of_250=l1[pos250+1:poslast]

df1=pd.DataFrame(columns=['URL','State','Street','Co_Name'])
URL=[]
state=[]
street=[]
co_name=[]
j=0
for line in extracted_text.splitlines():
    if line.startswith('www'):
        URL.append(line)
        pos_url=l1.index(line)
    if 'OK' in line:
        pos_state=l1.index(line)
        state.append(line)
        street.append(l1[pos_state-1])
        co_name.append(l1[pos_state-2])


# In[7]:


get_ipython().system('pip install pdfminer')


# In[4]:


import os
import pandas as pd
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from pdfminer.converter import PDFPageAggregator

base_path = r"C:\Users\Menda Jawahar\Desktop"
my_file = os.path.join(base_path + "/" + "Microsoft Word - IPA Membership Directory.pdf")

fp = open(my_file, "rb")
parser = PDFParser(fp)
document = PDFDocument(parser)
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)

extracted_text = ""
for page in PDFPage.create_pages(document):
    interpreter.process_page(page)
    layout = device.get_result()
    for lt_obj in layout:
        if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
            extracted_text += lt_obj.get_text()


# In[2]:


extracted_text


# In[3]:


my_file


# In[ ]:




