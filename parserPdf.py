import sys
import os
import re
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
import xml.etree.cElementTree as ET

def getTextPdf(filename):
	file = open(filename,'rb')
	parser = PDFParser(file)
	doc = PDFDocument()
	parser.set_document(doc)
	doc.set_parser(parser)
	doc.initialize('')
	rsrcmgr = PDFResourceManager()
	laparams = LAParams()
	laparams.char_margin = 1.0
	laparams.word_margin = 1.0
	device = PDFPageAggregator(rsrcmgr, laparams=laparams)
	interpreter = PDFPageInterpreter(rsrcmgr, device)
	extracted_text = ''
	for page in doc.get_pages():
		interpreter.process_page(page)
		layout = device.get_result()
		for lt_obj in layout:
			if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
			   extracted_text += lt_obj.get_text()
	return extracted_text
