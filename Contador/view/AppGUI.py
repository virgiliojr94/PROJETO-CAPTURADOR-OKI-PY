from control.GerarPDFController import GerarPDFController as controller
from tkinter import *
from tkinter import filedialog
from tkinter import ttk 
import os as os




class AppGUI(object):
	
	def __init__(self, title):
		super(AppGUI, self).__init__()
		self.root       = Tk()
		self.root.title = title
		self.path = os.path.abspath(os.getcwd()+"/pdf")
		#self.root.directory = FileDialog.askdirectory()
		#filename2 =  filedialog.askopenfilename(title = "Select file",filetypes = (("Excel files", ".html"),))
		
		#print (self.root.directory)

		self.label_username        = Label(self.root, text="Username")
		self.label_password        = Label(self.root, text="Password")
		self.label_protocol		   = Label(self.root, text="Protocolo")
		self.label_project_context = Label(self.root, text="Contexto do projeto")

		self.label_ip 	        = Label(self.root, text="Lista de Ips")
		self.label_log 	        = Label(self.root, text="log")
		
		self.entry_username     = Entry(self.root)
		self.entry_password     = Entry(self.root)
		self.entry_protocol     = ttk.Combobox(self.root, values = ["http://","https://"])
		self.entry_url_context  = Entry(self.root)
		
		self.text_box_ip 	    =  Text(self.root, width=50, height=10)
		self.text_box_log 	    =  Text(self.root, width=50, height=10)

		self.buttom_limpar_ip   = Button(self.root, text="Limpar")#, command=open_file) 
		self.buttom_gerar_pdf   = Button(self.root, text="Gerar PDF")#, command=open_file) 
		self.buttom_abrir_pasta = Button(self.root, text="Abrir pasta")#, command=open_file) 


		
		self.text_box_ip.config(highlightbackground="black",highlightcolor= "red")
		self.text_box_log.config(highlightbackground="black",highlightcolor= "red", state="disable")

		self.entry_url_context.insert(0,"/printer/infotosave.htm")
		self.entry_protocol.insert(0, "http://")

		self.label_username.grid(row=0, column=0);
		self.label_password.grid(row=0, column=1);

		self.entry_username.grid(row=1, column=0);
		self.entry_password.grid(row=1, column=1);

		self.label_protocol.grid(row=2, column=0);
		self.entry_protocol.grid(row=3, column=0);

		self.label_project_context.grid(row=2, column=1);
		self.entry_url_context.grid(row=3, column=1);
		
		self.label_ip.grid(row=4, column=0);
		self.label_log.grid(row=4, column=1);

		self.text_box_ip.grid(row=5, column=0, padx=16, pady=16);
		self.text_box_log.grid(row=5, column=1,padx=16, pady=16);

		self.buttom_gerar_pdf.grid(row=6, column=0);
		self.buttom_abrir_pasta.grid(row=6, column=1);
		self.buttom_limpar_ip.grid(row=7, column=0);


		self.buttom_gerar_pdf["command"]   = self.command_gerar_pdf
		self.buttom_abrir_pasta["command"] = self.command_abrir_pasta
		self.buttom_limpar_ip["command"]   = self.command_limpar


	def command_gerar_pdf(self):
		
		count = 0
		ips   = self.text_box_ip.get("1.0","end-1c").split(",")
		self.text_box_log.configure(state="normal")
		self.text_box_log.delete(1.0,"end-1c")
		for ip in ips:
			
			url = self.entry_protocol.get().strip()+ip.strip()+self.entry_url_context.get().strip()
			#print(url)
			if( self.entry_username.get()!="" and self.entry_password.get()!=""):
				ispdf = controller(self.entry_username.get(), self.entry_password.get() ).gerar_pdf_por_url(url,self.path+"/","pdf-"+str(count))
			else:
				ispdf = controller().gerar_pdf_por_url(url,self.path+"/","pdf-"+str(count))

			count += 1
			if ispdf is False:
				self.text_box_log.insert(1.0, ip.strip()+".....Fail\n")
				continue
			self.text_box_log.insert(1.0, ip.strip()+".....ok\n")
		self.text_box_log.configure(state="disable")


	def command_abrir_pasta(self):
		path = self.path
		os.system(f'open {os.path.realpath(path)}')
	def command_limpar(self):
		self.text_box_ip.delete(1.0,"end-1c")
		self.text_box_log.delete(1.0,"end-1c")

	
	def start(self):
		self.root.mainloop();

