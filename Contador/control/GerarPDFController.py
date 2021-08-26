import requests
import requests.auth
from requests.auth import HTTPDigestAuth
from bs4 import BeautifulSoup
import os.path
from os import path as ospath
import pdfkit

class GerarPDFController:
	"""docstring for GerarPDFController"""
	def __init__(self, user = None, password = None):
		super(GerarPDFController, self).__init__()
		self.user = user
		self.password = password
		
	def gerar_pdf_por_url(self,url="",path="",filename="oi"):
		try:
			if self.user is not None and self.password is not None:
				request = requests.get(url, auth=HTTPDigestAuth(self.user,self.password))
			else:
				request = requests.get(url)#, auth=HTTPDigestAuth('user', 'pass'))
			pdfkit.from_string(request.text,path+filename+".pdf")
			return True
		except Exception as e:
			#print("Error")
			#print(e)
			if ospath.exists(path+filename+".pdf") is False:
				return False
			return True;

