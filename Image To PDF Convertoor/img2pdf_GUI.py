from tkinter import Label
import tkinter as tk
# from  back_end import upload_image , Execute_pdf
from tkinter import Canvas
from PIL import ImageTk , Image
import os 
from tkinter import filedialog

# GUI image to pdf
front_end =  tk.Tk()
# Heading
Txt = tk.Text(front_end , height = 2 , width = 30)

Txt.insert(tk.END , "CONVERT IMAGE TO PDF ONLY ") 
Txt.grid(row = 0 , column = 0)
# size of window / Application 
front_end.geometry("700x600")

# Set BackGround
load = Image.open("Images//bg.png")
render = ImageTk.PhotoImage(load)
img = Label(front_end , image = render)
img.place(x=0,y=0)

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ 

front_end.title("Image To PDF Convertor")

# GUI Favicon
front_end.iconphoto(False , tk.PhotoImage(file = "Images//pdf.png"))

# Use TO Fix THe Size of Window
front_end.resizable(0,0)
'''///////////'''

# use to disable and enable the upload_button and Execute_Button 
def disable(btn):
    btn['state']='disabled'

def enable(btn):
    btn['state']='active'

# Upload Image 

files = {}
def upload_image():
    global files
    files['filename']=filedialog.askopenfilenames(filetypes=[('All FIles','*.*')]
    ,initialdir = os.getcwd(), title = 'Choose Image/Images OR Photo/Photos')
    if len(files['filename'])!=0:
        enable(Execute_Button)
    pass

# Excecute PDF 

def Execute_pdf():
    try:
        img_list = []
        for file in files['filename']:
            img_list.append(Image.open(file).convert('RGB'))
        save_file_name = filedialog.asksaveasfilename(filetypes = [('PDF','*.pdf')], initialdir = os.getcwd() , title = 'Save File')
        img_list[0].save(f'{save_file_name}.pdf', save_all = True, append_images = img_list[1:])
        T = tk.Label(front_end, text="Your Pdf Completed \n Location is ")
        T1= tk.Label(front_end, text=save_file_name)
        T.grid()
        T1.grid()

        disable(Execute_Button)
    except:
        return
    pass

# Main BODY
# main Image
canvas = Canvas(front_end , width = 280 , height = 283)
canvas.grid(row = 0, column = 0 , sticky = tk.N, padx= 220 , pady = 25) # .grid() use At what place i want to put this Image
main_img = ImageTk.PhotoImage(Image.open("Images//cs1.png"))
canvas.create_image(150,150 , image = main_img)

# Upload Button 
upload_button = tk.Button(front_end , text = 'UPLOAD IMAGE', width = 20 , height = 1 , font = ('arial' , 14 , 'bold'), bg ='#9FE2BF' , fg ='#FFFF00' , command=upload_image)

upload_button.grid(row = 3 , column = 0 , padx = 200 , pady = 20)

# Execute Button 
# def Execute_pdf():
#     pass

# Execute_Button
Execute_Button = tk.Button(front_end , text = 'Execute PDF', width = 20 , height = 1 , font = ('arial' , 14 , 'bold'), bg ='#9FE2BF' , fg ='#FF0000' , command=Execute_pdf)
Execute_Button.grid(row = 7 , column = 0 , padx = 200 , pady = 20)
disable(Execute_Button)


front_end.mainloop()
