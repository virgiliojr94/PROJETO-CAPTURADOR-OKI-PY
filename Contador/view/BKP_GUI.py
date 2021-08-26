import tkinter as kinter
from control.GerarPDFController import GerarPDFController as controller
import os as os
class GUI(object):
	"""docstring for ClassName"""
	window   = "";
	kinter   = ""
	text_box = "insert ips"
	log_box  = "log"
	path = "//Users//charlotte//Desktop//desk//Contador/pdf"
	
	def __init__(self, arg):
		super(GUI, self).__init__()
		self.arg = arg
		self.kinter = kinter
		self.window = kinter.Tk()
		
	def start(self):
		self.createWindow(1,2);
		self.setTextBox(self.window,"https://google.com",0,0,10,50);
		self.setLogBox(self.window,"log->",0,2,10,50,"disable");
		self.btn_frame = self.kinter.Frame(self.window);
		self.btn_frame.grid(columnspan=3, rowspan=2,row=0, column=0)
		self.addAddBtn(self.btn_frame, "Gerar", self.gerarPDF_event,0,0)
		self.addAddBtn(self.btn_frame, "Abrir pasta", self.abrirPasta_event,0,1)
		self.addAddBtn(self.btn_frame, "Limpar", self.limpar_event,1,0)
		self.addAddBtn(self.btn_frame, "Envar por Email", self.enviarEmail_event,1,1,"disable")
		self.startMainLoop()
		
	def createWindow(self, num_row, num_column):
		self.window.geometry("800x400")
		self.window.title("Contador")
		self.window.rowconfigure(0,minsize=num_row, weight=1)
		self.window.columnconfigure(1, minsize=num_column, weight=1)
		self.window.config(highlightbackground="black",highlightcolor= "red")
		
	
	def setTextBox(self, target,value, x, y, w,h, s = "normal" ):
		self.text_box = kinter.Text(target, height=w, width=h)
		self.text_box.config(highlightbackground="black",highlightcolor= "red")
		if value is not None:
			self.text_box.insert(1.0,value)
		self.text_box.grid(row=x, column=y , padx=2,pady=2 ,sticky="n")#,sticky="n")
		self.text_box.config(state=s)
		return self.text_box

	def setLogBox(self, target,value, x, y, w,h, s = "normal" ):
		self.log_box = kinter.Text(target, height=w, width=h)
		self.log_box.config(highlightbackground="black",highlightcolor= "red")
		if value is not None:
			self.log_box.insert(1.0,value)
		self.log_box.grid(row=x, column=y , padx=2,pady=2 ,sticky="n")#,sticky="n")
		self.log_box.config(state=s)
		

	def addAddBtn(self,target, name, cmd, x,y, s = "normal"):
		self.btn  = kinter.Button(target, text=name)#, command=open_file)
		self.btn["command"] = cmd
		self.btn.grid(row=x,column=y)
		self.btn.config(state=s);

	def startMainLoop(self):
		self.window.mainloop()

	



	def gerarPDF_event(self):
		
		ips = self.text_box.get("1.0","end-1c").split(",")
		self.log_box.configure(state="normal")
		self.log_box.delete(1.0,"end-1c")
		count = 0
		for ip in ips:
			url = "http://"+ip+"/printer/infotosave.htm"
			url = ip
			ispdf = controller().gerar_pdf_por_url(url,self.path+"/","pdf-"+str(count))
			count += 1
			if ispdf is False:
				self.log_box.insert(1.0, ip.strip()+".....Fail\n")
				continue
			self.log_box.insert(1.0, ip.strip()+".....ok\n")
		self.log_box.configure(state="disable")
		
	
	def abrirPasta_event(self):
		path = self.path
		os.system(f'open {os.path.realpath(path)}')
	
	def limpar_event(self):
		self.text_box.delete(1.0,"end-1c")
	
	def enviarEmail_event(self):
		print("Enviar por Email")
