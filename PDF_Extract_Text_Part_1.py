
import tkinter as tk 
import PyPDF2
from PIL import Image , ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk() 

canvas = tk.Canvas(root , width=600 , height= 300)
canvas.grid(columnspan=3 , rowspan=3)

# application logo

logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = logo)
logo_label.image = logo 
logo_label.grid(column=1 , row=0)

# message to select pdf file and button to browse file 

selecting_file_message = tk.Label(root , text="Select a PDF File on your computer to extract its text :" , font= "Raleway")
selecting_file_message.grid(columnspan=3 , column=0 , row=1)

# opening file function 

def open_file():

    Browse_text.set("loading...")
    file = askopenfile(parent=root , mode="rb" , title="choose a file" , filetype=[("pdf file" , "*.pdf")])

    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        text_box = tk.Text(root , height=10 , width=50 , padx=15 , pady=15)
        text_box.insert(1.0 , page_content)
        text_box.tag_configure("center" , justify="center")
        text_box.tag_add("center" , 1.0 , "end")
        text_box.grid(column=1 , row=3)

        Browse_text.set("Browse")

Browse_text = tk.StringVar()
Browse_Button = tk.Button(root , textvariable=Browse_text , command=lambda:open_file() , font="Raleway" , 
                          bg="#20bebe" ,font_color="white" , height=2 , width=15)

Browse_text.set("Browse")
Browse_Button.grid(column=1 , row=2)

canvas = tk.Canvas(root , width=600 , height= 250)
canvas.grid(columnspan=3)


root.mainloop()

