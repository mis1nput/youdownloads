#imports
from tkinter import*
from pytube import YouTube

#gui
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Youdownloads by ~~~ Mis!nput")
background_image = PhotoImage(file='/home/misinput/Documents/Python Programs/youdownloads/background.png')
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
Label(root,text = 'Youtube Video Downloader', font = 'arial 20 bold', bg = 'light blue').pack()
link = StringVar()
Label(root, text = 'Paste Link Here: ', font = 'arial 20 bold', bg = 'light blue').pack()
link_enter = Entry(root, width = 53, textvariable = link)
link_enter.place(x = 32, y = 120)


#Downloading Function
def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x=180 , y =210)

Button(root,text = 'DOWNLOAD', font ='arial 15 bold', bg = 'light blue', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()

input('Press Enter to Exit')
