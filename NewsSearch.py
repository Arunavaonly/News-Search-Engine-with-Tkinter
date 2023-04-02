from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox as msg
import json
import requests
import webbrowser

#getting the news articles
def get_articles(query):
    url = f'https://newsapi.org/v2/everything?q={query}&from=2023-03-20&apiKey=<your api key from newsapi>'

    news = requests.get(url)

    obj = json.loads(news.text)

    newslist = obj['articles']
    headlines = []
    links =[]
    for article in newslist:
        headlines.append(article['title'])
        links.append(article['url'])    
    return headlines, links
   
def help():
      msg.showinfo('Help', 'Provide a search topic, for example- "football, and news will be fetched on the basis that search topic. Click on the home menu to return to the home page"')
def about():
      msg.showinfo('Developer Information', 'Hi, I am Arunava Kar. I am a linguist by profession and an amateur programmer.')

def clear_widgets(frame):
	# select all frame widgets and delete them
	for widget in frame.winfo_children():
		widget.destroy()

#GUI and logic for the homepage
def home():
    clear_widgets(frame2)
    frame2.grid_forget()
    frame.tkraise
    frame.pack_propagate(False)
    img = PhotoImage(file = 'icon.png')
    print('icon.png')
    root.iconphoto(False, img)

    label1 = Label(frame, text = 'NewSearch by Arunava\n Your Own News Search Engine', fg = 'pink', bg= '#1d6950', font = 'TkHeadingfont 15 italic bold' )
    label1.grid(row =0, column =0, padx= 20, pady =25)
    img2 = PhotoImage(file= 'logo1.png')
    label2 = Label(frame, image= img2)
    label2.grid(row =1, column=0)
    label2.image = img2
    label3 = Label(frame, text ='Provide the search topic', bg='#1d6950')
    label3.grid(row =2, column=0, pady =15, padx = 20, sticky=EW)

    global queryval
    queryval = StringVar()
    entry = Entry(frame, textvariable= queryval)
    entry.grid(row =3, column =0)

    search = Button(frame, text= 'Search News', font= ('TkHeadingfont', 20), bg ='#28393a', fg ='white',        cursor="hand2",activebackground="#badee2", activeforeground="black", command = load_frame2)
    search.grid(row =7, column=0, pady =50)      

#GUI and logic for the news page
def load_frame2():
    try:
        query = queryval.get()
        clear_widgets(frame)
        frame2.grid(row =0, column=0)
        frame2.tkraise()
    

        headlines, links = get_articles(query)

        img = PhotoImage(file = 'icon.png')
        root.iconphoto(False, img)
    
        l1 = Label(frame2, text = 'News Sorted Based on Popularity', font= ('TkHeadingfont', 15),  borderwidth=5, relief= GROOVE)
        l1.pack(anchor= W, expand= True, fill = X)

        text = ScrolledText(frame2, height = 40, width= 165, bg ='#1d6950',  state= 'disable')
        text.pack(expand= True, fill =BOTH)
        new_frame = Frame(text, bg ='#1d6950')
        text.window_create('1.0', window = new_frame)

        for i in range(len(headlines)):
            if len(headlines[i]) >140:
                headlines[i] = headlines[i][:140] + '\n' + headlines[i][140:]
            Label(new_frame, text = headlines[i], fg = 'white', bg = '#1d6950', padx =15, pady =10, font= 'Shanti 12').grid(row =i, column=0)
            Button(new_frame, text = 'Go to Website', bg = '#28793a', padx = 5, cursor="hand2",activebackground="#badee2", activeforeground="black", command= lambda i=i: webbrowser.open_new_tab(links[i])).grid(row =i, column=1, sticky=W)
    except:
         home()
         msg.showerror('Error', 'Unable to search, please check whether you have provided a search topic')

#starting a tkinnter window
root = Tk()

root.title('NewSearch by Arunava')

#adding menubar
mainmenu = Menu(root, background= '#28793a', cursor= 'hand2', relief= SUNKEN, borderwidth=3, tearoff= 0)
mainmenu.add_command(label= 'Home', foreground= 'red', font= 'ubuntu', command = home)
mainmenu.add_command(label= 'About', command= about)
mainmenu.add_command(label= 'Help', command = help)
root.config(menu=mainmenu)

#creating two frames
frame = Frame(root, height = 600, width=700, borderwidth= 5, relief= SUNKEN, bg= '#1d6950')
frame.grid(row =0, column =0)

frame2 = Frame(root, borderwidth= 5, relief= SUNKEN, bg ='#1d6950',)
frame2.grid(row=0, column =0)

#finally loading the homepage
home()


root.mainloop()
