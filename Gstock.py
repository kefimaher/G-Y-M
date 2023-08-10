import tkinter as tk
from PIL import ImageTk, Image
r = tk.Tk()
# Titre du page
r.title('Stock Net')
def item_visibility():
 items.place(x=400, y=145)
 setting.place(x=1500, y=800)
 news.place(x=1500, y=800)
 document.place(x=1500, y=800)
 exp.place(x=1500, y=800)
def settings_visibility():
 setting.place(x=400, y=145)
 items.place(x=1500, y=800)
 news.place(x=1500, y=800)
 document.place(x=1500, y=800)
 exp.place(x=1500, y=800)
def news_visibility():
 news.place(x=400, y=145)
 setting.place(x=1500, y=800)
 items.place(x=1500, y=800)
 document.place(x=1500, y=800)
 exp.place(x=1500, y=800)
def document_visibility():
 news.place(x=1500, y=800)
 setting.place(x=1500, y=800)
 items.place(x=1500, y=800)
 document.place(x=400, y=145)
 exp.place(x=1500, y=800)
def exp_visibility():
 news.place(x=1500, y=800)
 setting.place(x=1500, y=800)
 items.place(x=1500, y=800)
 document.place(x=1500, y=800)
 exp.place(x=400, y=145)
canvas = tk.Canvas(r, width=1500, height=800, background='grey')
# line
canvas.create_line(400, 0, 400, 800)
# barre de navigation a gauche
canvas.create_rectangle(0, 800, 400, 0, fill="#3E4146")
# page content
canvas.create_rectangle(400, 800, 1500, 0, fill="white")
# barre de navigation a haut a droite
canvas.create_rectangle(400, 70, 1500, 0, fill="#55259F")
# barre de navigation a haut a droite
canvas.create_rectangle(0, 70, 400, 0, fill="#492089")
canvas.create_line(400, 145, 1500, 145, fill="#492089", width=2)
Title = canvas.create_text(200, 40, text="Stock Net", fill="white", font='Helvetica 15 bold')
# x = canvas.create_rectangle(400, 800, 1500, 146, fill="white")
# y = canvas.create_rectangle(400, 800, 1500, 146, fill="grey")
canvas.pack()
# button name + width
logout = tk.Button(r, text='Log out', width=10, command=r.destroy, background="white", fg="#683FA9")
logout.place(x=1380, y=10)
# button name + width
search = tk.Button(r, text='Search', width=10, background="#683FA9", fg="white")
search.place(x=1380, y=113)
# button name + width
test1 = tk.Button(r, text='test1', width=10, background="#683FA9", fg="white")
test1.place(x=420, y=113)
# button name + width
test2 = tk.Button(r, text='test2', width=10, background="#683FA9", fg="white")
test2.place(x=550, y=113)
# button navbar a gauche vertical
#Item list : afficher un page contien la list des produit dans la table (id,image,nom,prix,quantite)
items = tk.Button(r, text='Items List', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white", command=item_visibility)
items.place(x=1, y=180)
#Button New items : ajouter un produit dans la table (id,image,nom,prix,quantite)
news = tk.Button(r, text='New Items', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white", command=news_visibility)
news.place(x=1, y=230)
#Tout les fisher
document = tk.Button(r, text='Document', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white", command=document_visibility)
document.place(x=1, y=280)
#Tout les entrant et sorant
exp = tk.Button(r, text='Expences', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white", command=exp_visibility)
exp.place(x=1, y=330)
#Modifer
setting = tk.Button(r, text='Setting', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white", command=settings_visibility)
setting.place(x=1, y=380)
#button links
setting = tk.Frame(canvas, width=1500, height=800, background='grey')
items = tk.Frame(canvas, width=1500, height=800, background='grey')
exp  = tk.Frame(canvas, width=1500, height=800, background='grey')
document = tk.Frame(canvas, width=1500, height=800, background='grey')
news = tk.Frame(canvas, width=1500, height=800, background='grey')
items_page_text = tk.Label(items, text="Contenu du page items ", font=("Arial", 20), fg="#683FA9", background="grey")
items_page_text.place (x=0, y=10)
new_page_text = tk.Label(news, text="Contenu du page news ", font=("Arial", 20), fg="#683FA9", background="grey")
new_page_text.place (x=0, y=10)
doc_page_text = tk.Label(document, text="Contenu du page document", font=("Arial", 20), fg="#683FA9", background="grey")
doc_page_text.place (x=0, y=10 )
exp_page_text = tk.Label(exp, text="Contenu du page Expences ", font=("Arial", 20), fg="#683FA9", background="grey")
exp_page_text.place (x=0, y=10 )
setting_page_text = tk.Label(setting, text="Contenu du page setting", font=("Arial", 20), fg="#683FA9", background="grey")
setting_page_text.place(x=0, y=10)
r.mainloop()
