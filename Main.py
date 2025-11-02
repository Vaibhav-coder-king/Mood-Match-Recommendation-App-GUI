#Movies and Web series Recommendation App 
import csv
import random as rd
from tkinter import messagebox as mb 
from customtkinter import *
from PIL import Image
from threading import Thread
import urllib.request, json
from io import BytesIO 

#CTkListbox with the help of CTkScrollableFrame
class CTkListbox(CTkScrollableFrame):
	def __init__(self,master,items=[],command=None,**kwargs):
		super().__init__(master,**kwargs)
		self.command=command
		self.buttons=[]
		for i in items:
			self.add_item(i)
			
	#for adding item
	def add_item(self,item):
		btn=CTkButton(self,text=item,text_color=("blue","#00ff00"),font=("Roboto",40),fg_color="transparent", bg_color="transparent",hover_color="grey",command=lambda x=item: self.on_select(x),anchor="w",border_color=("blue","green"),border_width=3,corner_radius=60)
		btn._text_label.configure(wraplength=self.master.winfo_screenwidth()*0.7)
		btn.pack(fill="x",pady=2)
		self.buttons.append(btn)
	
	def on_select(self,x):
		if self.command:
			self.command(x)
			
	#for clear all items
	def clear_items(self):
		for i in self.buttons:
			i.destroy()
			self.master.update_idletasks()
		self.buttons.clear()
	
	
class App:
	
	#Starting interface and building of window
	def __init__(self):
		
		#load api key
		with open(r"Api_omdb.txt",encoding="utf-8") as f:
			self.api_key=f.read()
		
		#heading 
		self.heading="Mood Match\nRecommendation\nApp"
		
		#for ensure it start only once
		self.chk_start=0
		
		#create the main window
		self.main=CTk()
		self.main.title("Mood Match Recommendation App")
		
		
		set_appearance_mode("dark")
		set_default_color_theme("dark-blue")
		self.current_thm="dark"
		
		
		#background image extraction 
		self.b_image=Image.open(r"Back_photo_laptop.png").convert("RGBA")
		
		self.back_image=CTkImage(light_image=self.b_image,dark_image=self.b_image,size=(self.main.winfo_screenwidth(),self.main.winfo_screenheight()))
		
		#background image creation
		self.back_image_label=CTkLabel(self.main,image=self.back_image,text="")
		self.back_image_label.pack()
		
		#Heading lab
		self.heading_label=CTkLabel(self.main,text=self.heading,font=("Noto Serif",75,"bold"),fg_color="#002960",text_color="#fdc500",bg_color="#002960",anchor="center")
		self.heading_label.place(relx=0.22,rely=0.2,relwidth=0.6)
		#for hover over heading
		self.heading_label.bind("<Enter>",self.on_enter_main_head)
		self.heading_label.bind("<Leave>",self.on_leave_main_head)

		
		#tap to start label
		self.start_info=CTkLabel(self.main,text="",font=("Noto Serif",30),fg_color="#002960",text_color="#EDF7F6",anchor="w",bg_color="#002960")
		self.start_info.place(relx=0.4,rely=0.6)
		
		#for bind 
		self.main.bind_all("<Button-1>",self.options_menu)
		
			
		#call start_animation
		self.main.after(500,self.start_animation)
		
		self.main.mainloop()
		
	

	#for hover over main heading
	def on_enter_main_head(self,event):
		if not self.chk_start==0:
			return
		for i in range(75,91,5):
			self.heading_label.configure(font=("Noto Serif",i,"bold"))
			self.main.update_idletasks()
			self.main.after(20)

	#for release from hover
	def on_leave_main_head(self,event):
		if not self.chk_start==0:
			return
		for i in range(90,74,-5):
			self.heading_label.configure(font=("Noto Serif",i,"bold"))
			self.main.update_idletasks()
			self.main.after(20)

	
	#for getting to previous page
	def go_back_pg(self,crt_frm):
		try:
			a=rd.randint(1,5)
			if a==1:
				for i in range(60,0,-1):
					b=-1+(60/i)
					crt_frm.place(relx=b,rely=0)
					self.main.update()
					self.main.after(2)
			elif a==2:
				for i in range(100,0,-1):
					b=-1+(100/i)
					crt_frm.place(relx=0,rely=b)
					self.main.update()
					self.main.after(2)
			elif a==3:
				for i in range(60,0,-1):
					b=1-(60/i)
					crt_frm.place(relx=b,rely=0)
					self.main.update()
					self.main.after(2)
			elif a==4:
				for i in range(100,0,-1):
					b=1-(100/i)
					crt_frm.place(relx=0,rely=b)
					self.main.update()
					self.main.after(2)
			else:
				for i in range(10,0,-1):
					c=((0.5/10)*i)
					b=0.5-c
					crt_frm.configure(width=self.main.winfo_screenwidth()*2*c,height=self.main.winfo_screenheight()*2*c)
					crt_frm.place(relx=b,rely=b)
					self.main.update()
					self.main.after(2)
			crt_frm.destroy()
		except:
			pass
				
	
	
	#for getting to next page
	def go_next_pg(self,nxt_frm):
		try:
			a=rd.randint(1,5)
			if a==1:
				nxt_frm.place(relx=-1,rely=0)
				self.main.update()
				for i in range(1,61):
					b=-1+(60/i)
					nxt_frm.place(relx=b,rely=0)
					self.main.update()
					self.main.after(2)
			elif a==2:
				nxt_frm.place(relx=0,rely=-1)
				self.main.update()
				for i in range(1,101):
					b=-1+(100/i)
					nxt_frm.place(relx=0,rely=b)
					self.main.update()
					self.main.after(2)
			elif a==3:
				nxt_frm.place(relx=1,rely=0)
				self.main.update()
				for i in range(1,61):
					b=1-(60/i)
					nxt_frm.place(relx=b,rely=0)
					self.main.update()
					self.main.after(2)
			elif a==4:
				nxt_frm.place(relx=0,rely=1)
				self.main.update()
				for i in range(1,101):
					b=1-(100/i)
					nxt_frm.place(relx=0,rely=b)
					self.main.update()
					self.main.after(2)
			else:
				for i in range(1,11):
					c=((0.5/10)*i)
					b=0.5-c
					nxt_frm.configure(width=self.main.winfo_screenwidth()*2*c,height=self.main.winfo_screenheight()*2*c)
					nxt_frm.place(relx=b,rely=b)
					self.main.update()
					self.main.after(2)
			#for enable animation
			self.start_start=True
		except:
			pass
				
		
			
			
				
	#start animation for initial interface
	def start_animation(self):
		self.heading_label.configure(font=("Noto Serif",75,"bold"))
		#for lower animation 
		if self.chk_start==0:
			start_line="Tap AnyWhere to Start"
			#for writing 
			for i in range(len(start_line)):
				if self.chk_start==0:
					self.start_info.configure(text=start_line[:i]+"_")
					self.main.update()
					self.main.after(100)
				else:
					break 
			self.start_info.configure(text=start_line)
			self.main.update()
			self.main.after(100)
			
			#for erasing 
			for j in range(len(start_line)):
				if self.chk_start==0:
					self.start_info.configure(text=" "*j+start_line[j:])
					self.main.update()
					self.main.after(100)
				else:
					break 
		if self.chk_start==0:
			self.main.after(200,self.start_animation())
		
	
	#options menu functions:-
	#exit function
	def exit(self):
		if mb.askyesno(title="Exit",message="Are You Sure\nYou Want to Exit?"):
			self.main.destroy()
				
						
				
	#change theme 
	def chnge_thm(self):
		val=self.theme_val.get()
		set_appearance_mode(val)
		self.main.update()
		self.current_thm=val
		
	#change theme with button
	def chnge_theme_but(self):
		self.change_theme.toggle()

	
	#Change text when hover
	def on_enter_but(self,event,button):
		button.configure(text_color=("white","#1c1c1c"),fg_color=("#002960","#00ff00"))
		self.main.update()
	
	#Change text when release from hover
	def on_leave_but(self,event,button):
		button.configure(text_color=("#002960","#00ff00"),fg_color="transparent")
		self.main.update()
	
	
	#go to home page from menu frm
	def go_to_homepage(self):
		self.start_info.configure(text="")
		self.go_back_pg(self.menu_frm)
		self.chk_start=0
		self.start_animation()
		
		
	# options menu __________________________
	def options_menu(self,event):
		#for stopping double clicking
		if self.chk_start==1:
			return 
		#for stopping animation 
		self.chk_start=1
		
		#options menu Frame
		self.menu_frm=CTkFrame(self.main,width=self.main.winfo_screenwidth(),height=self.main.winfo_screenheight())
		
		
		#add things in Frame
		#heading
		self.menu_head=CTkLabel(self.menu_frm,text="\n"+self.heading,font=("Noto Serif",65,"bold"),fg_color="#002960",text_color="#fdc500",corner_radius=80)
		self.menu_head.place(relx=0,rely=-0.1,relwidth=1,relheight=0.42)
		
		#exit button
		self.exit_but=CTkButton(self.menu_frm,text="Exit",font=("Roboto Medium", 60,"bold"),text_color="#002960",fg_color="brown",corner_radius=60,command=self.exit,hover_color="black",bg_color="#002960")
		self.exit_but.place(relx=0.87,rely=0.01,relheight=0.1,relwidth=0.1)
		self.main.bind("<Escape>",lambda event: self.exit())
		
		#change theme
		self.theme_val=StringVar(value="dark")
		
		self.change_theme=CTkSwitch(self.menu_frm,text="",switch_width=80 ,switch_height=40,bg_color="#002960",progress_color="black",fg_color=("#fdc500","black"),button_color="white",button_hover_color="white",command=self.chnge_thm,variable=self.theme_val, onvalue="dark",offvalue="light")
		self.change_theme.place(relx=0.12,rely=0.015)
		#to make sure the switch is in correct direction
		if self.current_thm=="dark":
			self.change_theme.select()
		elif self.current_thm=="light":
			self.change_theme.deselect()
		
		
		#Label change theme
		self.change_theme_label=CTkButton(self.menu_frm,text="Theme",font=("Roboto",40,"bold"),border_width=0,fg_color="#002960",bg_color="#002960",text_color="#fdc500",hover_color="#002960",command=self.chnge_theme_but)
		self.change_theme_label.place(relx=0.02,rely=0.01)
		
		#sub heading
		self.sub_heading=CTkLabel(self.menu_frm,text="Looking For",text_color=("#002960","#00ff00"),font=("Roboto Medium",70,"bold"))
		self.sub_heading.place(relx=0.35,rely=0.35)
		
		#moive button
		self.movie_but=CTkButton(self.menu_frm,text="Movies",text_color=("#002960","#00ff00"),font=("Roboto Medium",70),fg_color="transparent",bg_color="transparent",border_color=("#002960","#00ff00"),border_width=3,corner_radius=40,hover_color=("#002960","#00ff00"),width=420,height=100,command=lambda x="movies": self.search_menu(x))
		self.movie_but.place(relx=0.1,rely=0.45)
		#for text color change when hover
		self.movie_but.bind("<Enter>",lambda event: self.on_enter_but(event, self.movie_but))
		self.movie_but.bind("<Leave>",lambda event: self.on_leave_but(event, self.movie_but))
		
		
		#web series button
		self.ott_but=CTkButton(self.menu_frm,text="Webseries",text_color=("#002960","#00ff00"),font=("Roboto Medium",70),fg_color="transparent",bg_color="transparent",border_color=("#002960","#00ff00"),border_width=3,corner_radius=40,width=420,height=100,hover_color=("#002960","#00ff00"),command=lambda x="webseries": self.search_menu(x))
		self.ott_but.place(relx=0.55,rely=0.45)
		#for text color change when hover
		self.ott_but.bind("<Enter>",lambda event: self.on_enter_but(event, self.ott_but))
		self.ott_but.bind("<Leave>",lambda event: self.on_leave_but(event, self.ott_but))
		
		
		
		
		#k drama Button
		self.kdm_but=CTkButton(self.menu_frm,text="K drama",text_color=("#002960","#00ff00"),font=("Roboto Medium",70),fg_color="transparent",bg_color="transparent",border_color=("#002960","#00ff00"),border_width=3,corner_radius=40,width=420,height=100,hover_color=("#002960","#00ff00"),command=lambda x="k_drama": self.search_menu(x))
		self.kdm_but.place(relx=0.1,rely=0.6)
		#for text color change when hover
		self.kdm_but.bind("<Enter>",lambda event: self.on_enter_but(event, self.kdm_but))
		self.kdm_but.bind("<Leave>",lambda event: self.on_leave_but(event, self.kdm_but))
		
		
		
		
		#anime button 
		self.anime_but=CTkButton(self.menu_frm,text="Anime",text_color=("#002960","#00ff00"),font=("Roboto Medium",70),fg_color="transparent",bg_color="transparent",border_color=("#002960","#00ff00"),border_width=3,corner_radius=40,width=420,height=100,hover_color=("#002960","#00ff00"),command=lambda x="anime": self.search_menu(x))
		self.anime_but.place(relx=0.55,rely=0.6)
		#for text color change when hover
		self.anime_but.bind("<Enter>",lambda event: self.on_enter_but(event, self.anime_but))
		self.anime_but.bind("<Leave>",lambda event: self.on_leave_but(event, self.anime_but))
		
		
		#home page button
		self.hm_page_but=CTkButton(self.menu_frm,text="Go to Homepage",text_color=("#002960","#00ff00"),font=("Roboto Medium",70),fg_color="transparent",bg_color="transparent",border_color=("#002960","#00ff00"),border_width=3,corner_radius=40,width=600,height=100,hover_color=("#002960","#00ff00"),command=self.go_to_homepage)
		self.hm_page_but.place(relx=0.25,rely=0.75)
		#for text color change when hover
		self.hm_page_but.bind("<Enter>",lambda event: self.on_enter_but(event, self.hm_page_but))
		self.hm_page_but.bind("<Leave>",lambda event: self.on_leave_but(event, self.hm_page_but))
		
		#to place menu_frm
		self.go_next_pg(self.menu_frm)
		
		#option menu end______________________
		
	def search_menu(self,srh_w):
		#for ensure to Only once
		try:
			if self.start_start:
				self.start_start=False
			else:
				return
		except:
			pass
		
		match srh_w:
			case "movies":
				self.search_head="Movie"
			case "webseries":
				self.search_head="Webseries"
			case "k_drama":
				self.search_head="K Drama"
			case "anime":
				self.search_head="Anime"
			case _:
				return
				
				
		#frm of search menu
		self.search_frm=CTkFrame(self.main,width=self.main.winfo_screenwidth(),height=self.main.winfo_screenheight())
		
		
		#moive heading 
		self.search_head_label=CTkLabel(self.search_frm,text="\n"+self.search_head,font=("Noto Serif",70,"bold"),fg_color="#002960",text_color="#fdc500",corner_radius=80)
		self.search_head_label.place(relx=0,rely=-0.1,relwidth=1,relheight=0.3)
		
		#back button
		self.back_but=CTkButton(self.search_frm,text="Back",font=("Roboto Medium", 60,"bold"),text_color="#002960",fg_color="brown",command=lambda x=self.search_frm: self.go_back_pg(x),corner_radius=60,hover_color="black",bg_color="#002960")
		self.back_but.place(relx=0.87,rely=0.01,relheight=0.1,relwidth=0.1)
		
		#options for optionmenu
		self.search_option=["Name","Genre"]
		
		#seach optionmenu
		self.search_opt_menu=CTkOptionMenu(self.search_frm,values=self.search_option,height=150,font=("Roboto Medium",70,"bold"),corner_radius=50,fg_color="#002960",text_color="#fdc500",button_color="#002960",dropdown_font=("Roboto Medium",55,"bold"),button_hover_color="#002960",dropdown_text_color="#fdc500",dropdown_fg_color="#002960",command=self.search_opt)
		self.search_opt_menu.place(relx=0.06,rely=0.25)
		#for set the value
		self.search_opt_menu.set("Search by")

		
		#for seach by name option 
		self.search_name=CTkEntry(self.search_frm,placeholder_text="Enter "+self.search_head+" Name",font=("Roboto", 40),corner_radius=70,height=100,text_color=("blue","#00ff00"),placeholder_text_color=("blue","#00ff00"),fg_color=("white","#1c1c1c"))
		
		
		#for find of search
		self.find_name_but=CTkButton(self.search_frm,text="Find",font=("Roboto Medium",70,"bold"),text_color=("#002960","#00ff00"),fg_color="transparent",bg_color="transparent",border_color=("#002960","#00ff00"),border_width=3,corner_radius=40,height=100,hover_color=("#002960","#00ff00"),command=lambda x=self.search_name.get: self.find_name(x().replace(" ","+")))
		
		#for text color change when hover
		self.find_name_but.bind("<Enter>",lambda event: self.on_enter_but(event, self.find_name_but))
		self.find_name_but.bind("<Leave>",lambda event: self.on_leave_but(event, self.find_name_but))
		
		
		
		#for Genre search 
		self.search_genre=CTkEntry(self.search_frm,placeholder_text="Enter "+self.search_head+" Genre",font=("Roboto", 40),corner_radius=70,height=100,text_color=("blue","#00ff00"),placeholder_text_color=("blue","#00ff00"),fg_color=("white","#1c1c1c"))
		
		#for show list in list box
		self.search_genre.bind("<KeyRelease>",self.change_list)
		
		#list box of Genre 
		self.genre_list_box=CTkListbox(self.search_frm,orientation="vertical",border_width=3,fg_color="transparent", bg_color="transparent", scrollbar_button_color=("#002960","#00ff00"),scrollbar_fg_color="transparent",scrollbar_button_hover_color=("red","orange"),corner_radius=60,command=self.clk_list_box)
		
		#for find of genre
		self.find_genre_but=CTkButton(self.search_frm,text="Find",font=("Roboto Medium",70,"bold"),text_color=("#002960","#00ff00"),fg_color="transparent",bg_color="transparent",border_color=("#002960","#00ff00"),border_width=3,corner_radius=40,height=100,hover_color=("#002960","#00ff00"),command=self.show_result_list)
		
		
		#for text color change when hover
		self.find_genre_but.bind("<Enter>",lambda event: self.on_enter_but(event, self.find_genre_but))
		self.find_genre_but.bind("<Leave>",lambda event: self.on_leave_but(event, self.find_genre_but))
		
		
		
		self.go_next_pg(self.search_frm)
	#Search menu end_______________________
	
	
	# Search menu functions _________
	#Genre list change
	def change_list(self,event):
		self.genre_list_box.clear_items()
		ch=self.search_head
		match ch:
			case "Movie":
				self.gen_list=['biography', 'crime', 'sci-fi', 'romance', 'sport', 'comedy', 'history', 'adventure', 'superhero', 'horror', 'animation', 'action', 'western', 'mystery', 'music', 'musical', 'family', 'drama', 'thriller', 'war', 'fantasy']
				
			case "Webseries":
				self.gen_list=['short', 'action', 'mystery', 'musical', 'music', 'dystopian', 'fantasy', 'biography', 'family', 'history', 'sports', 'talk-show', 'drama', 'war', 'spy', 'thriller', 'horror', 'superhero', 'western', 'food', 'comedy', 'reality-tv', 'animation', 'sci-fi', 'political', 'romance', 'historical', 'medical', 'sport', 'game-show', 'netflix', 'crime', 'documentary', 'adventure']
				
			case "K Drama":
				self.gen_list=['education', 'animation', 'supernatural', 'satire', 'psychological', 'brotherhood', 'business', 'healing', 'crime', 'thriller', 'medical', 'fantasy', 'mystery', 'sci-fi', 'spy', 'friendship', 'musical', 'school', 'romance', 'family', 'survival', 'youth', 'horror', 'sports', 'melodrama', 'political', 'adventure', 'military', 'legal', 'food', 'comedy', 'mockumentary', 'war', 'drama', 'action', 'historical', 'slice-of-life']
				
			case "Anime":
				self.gen_list=['cyberpunk', 'super power', 'suspense', 'horror', 'superhero', 'shounen', 'samurai', 'parody', 'slice of life', 'drama', 'harem', 'supernatural', 'anthology', 'martial arts', 'thriller', 'mecha', 'romance', 'team sports', 'vampire', 'gourmet', 'ecchi', 'military', 'adventure', 'police', 'sports', 'action', 'steampunk', 'music', 'surrealism', 'comedy', 'seinen', 'game', 'historical', 'space', 'school', 'dementia', 'mystery', 'fantasy', 'strategy', 'psychological', 'documentary', 'sci-fi']
			case _:
				return
		ent=self.search_genre.get().lower()
		if ent=="":
			return
		for i in self.gen_list:
			if ent in i:
				self.genre_list_box.add_item(i)
	
	
	#click on list box items
	def clk_list_box(self,x):
		self.search_genre.delete(0,"end")
		self.search_genre.insert(0,x)
		self.main.update()	
	
	
	
	#for show list from selected genre
	def show_result_list(self):
		
		#for ensure to Only once
		try:
			if self.start_start:
				self.start_start=False
			else:
				return
		except:
			pass
		
		ent=self.search_genre.get().lower()
		#for chk_value
		if ent=="":
			mb.showinfo(title="Empty Input",message="Plz,Input something.")
			return
		elif ent not in self.gen_list:
			mb.showinfo(title="Wrong Input",message="Plz,input the correct genre.")
			return
		
		
		#for getting items from local
		sort_data_list=[]
		match self.search_head:
			case "Movie":
				with open(r"Movies.csv",encoding="utf-8")as f:
					read=csv.reader(f)
					next(read)
					list_of_data=list(read)
				for i in list_of_data:
					if i==[]:
						continue
					if ent in i[2].lower():
						sort_data_list.append(i[0])
				
			case "Webseries":
				with open(r"Webseries.csv",encoding="utf-8")as f:
					read=csv.reader(f)
					next(read)
					list_of_data=list(read)
				for i in list_of_data:
					if i==[]:
						continue
					if ent in i[3].lower():
						sort_data_list.append(i[0])
					
			case "K Drama":
				with open(r"K_drama.csv",encoding="utf-8")as f:
					read=csv.reader(f)
					next(read)
					list_of_data=list(read)
				for i in list_of_data:
					if i==[]:
						continue
					if ent in i[3].lower():
						sort_data_list.append(i[0])
						
						
			case "Anime":
				with open(r"Anime.csv",encoding="utf-8")as f:
					read=csv.reader(f)
					next(read)
					list_of_data=list(read)
				for i in list_of_data:
					if i==[]:
						continue
					if ent in i[1].lower():
						sort_data_list.append(i[0])
		#for shuffling
		rd.shuffle(sort_data_list)
		
		
		#frame
		self.result_list_frm=CTkFrame(self.main,width=self.main.winfo_screenwidth(),height=self.main.winfo_screenheight())
		
		
		
		#back button
		self.back_but=CTkButton(self.result_list_frm,text="Back",font=("Roboto Medium", 60,"bold"),text_color="#002960",fg_color="brown",bg_color="transparent",command=lambda x=self.result_list_frm: self.go_back_pg(x),hover_color="black")
		self.back_but.place(relx=0.87,rely=0.01,relheight=0.1,relwidth=0.1)
		
		
		#listbox
		self.result_list_box=CTkListbox(self.result_list_frm,label_text=self.search_head,label_font=("Roboto Medium", 100,"bold"),label_text_color="#fdc500",label_fg_color="#002960",corner_radius=40,items=sort_data_list[:50],scrollbar_button_color=("#002960","#00ff00"),scrollbar_fg_color="transparent",scrollbar_button_hover_color=("red","orange"),command=self.con_tor)
		self.result_list_box.place(relx=0.05,rely=0.12,relwidth=0.9,relheight=0.8)
		
		self.go_next_pg(self.result_list_frm)
		
	#genre result list end_____________________
	
	#for connecting find_name
	def con_tor(self,x):
		x=x.replace(" ","+")
		self.find_name(x)
	
	
	#for select the option
	def search_opt(self,opt):
		self.search_opt_menu.set("Search by\n  "+opt+" ➡️")

		

		if opt=="Name":
			#for removal
			self.search_genre.place_forget()
			self.genre_list_box.place_forget()
			self.find_genre_but.place_forget()
			
			#for add item
			self.search_name.place(relx=0.5,rely=0.4,relwidth=0.45)
			self.find_name_but.place(relx=0.6,rely=0.6,relwidth=0.2)
			
		elif opt=="Genre":
			#for removal 
			self.search_name.place_forget()
			self.find_name_but.place_forget()
			
			#for add item
			self.search_genre.place(relx=0.5,rely=0.3,relwidth=0.45)
			self.genre_list_box.place(relx=0.5,rely=0.42,relwidth=0.4,relheight=0.3)
			self.find_genre_but.place(relx=0.6,rely=0.75,relwidth=0.2)
		self.main.update()
		
			
	#find from name
	def find_name(self,name):
		#for ensure to Only once
		try:
			if self.start_start:
				self.start_start=False
			else:
				return
		except:
			pass
		
		self.url = f"http://www.omdbapi.com/?t=\"{name}\"&apikey={self.api_key}"
		
		try:
			if name=="":
				mb.showinfo(title="Empty",message="Plz,input the name.")
				self.start_start=True
				return
			with urllib.request.urlopen(self.url) as response:
				self.data = json.loads(response.read())
			if self.data["imdbRating"]=="N/A":
				mb.showinfo(title="not found",message="plz,check your input\nNo such moive found.")
				self.start_start=True
				return 
			
				
			self.show_from_name(self.data)
			self.chk_locol(self.data)
		except:
			mb.showinfo(title="No Internet",message="Plz,Check Your Internet\n and Your input.")
			self.start_start=True
	
	#result from name
	def show_from_name(self,data):
		
		#create the result frm
		self.result=CTkFrame(self.main,width=self.main.winfo_screenwidth(),height=self.main.winfo_screenheight())
		
		#heading
		self.result_heading=CTkLabel(self.result,text="\n"+self.search_head,font=("Noto Serif",90,"bold"),fg_color="#002960",text_color="#fdc500",corner_radius=80)
		self.result_heading.place(relx=0,rely=-0.1,relwidth=1,relheight=0.3)
		
		#back button
		self.back_but=CTkButton(self.result,text="Back",font=("Roboto Medium", 60,"bold"),text_color="#002960",fg_color="brown",command=lambda x=self.result: self.go_back_pg(x),hover_color="black",bg_color="#002960")
		self.back_but.place(relx=0.87,rely=0.01,relheight=0.1,relwidth=0.1)
		
		#movie name as subtitle
		self.result_title=CTkLabel(self.result,text=data["Title"],font=("Roboto Medium",75,"bold"),text_color=("blue","#00ff11"),fg_color="transparent", bg_color="transparent",anchor="center",wraplength=self.main.winfo_screenwidth()-50)
		self.result_title.place(relx=0,rely=0.2, relwidth=1)
	
		# load Poster url
		if data["Poster"]:
			with urllib.request.urlopen(data["Poster"])as u:
				raw_data = u.read()
			#load img
			img = Image.open(BytesIO(raw_data))
			
			#make it compatible for ctk
			img=CTkImage(light_image=img,dark_image=img,size=(300,450))
			
			#display img
			if len(data["Title"])>25:
				yy=0.4
			else:
				yy=0.32
			self.result_img=CTkLabel(self.result, text="",image=img)
			self.result_img.place(relx=0.05,rely=yy)
		
		#display data
		
		if (data["Type"]).lower()=="movie":
			txt="Year="+data["Year"]+"\nImdb-Rating="+data["imdbRating"]+"/10 \nBoxOffice-Collection="+data["BoxOffice"]+"\nType="+data["Type"]+"\nDirector="+data["Director"]+"\nRunTime="+data["Runtime"]+"\nActors="+data["Actors"]
		else:
			txt="Year="+data["Year"][:4]+"\nImdb-Rating="+data["imdbRating"]+"/10\nType="+data["Type"]+"\nSeasons="+data["totalSeasons"]+"\nAge-Rating="+data["Rated"]+"\nActors="+data["Actors"]
		
		
		self.result_side_panel=CTkLabel(self.result,text=txt,font=("Roboto",25),wraplength=self.main.winfo_screenwidth()*0.38,anchor="w")
		self.result_side_panel.place(relx=0.5,rely=yy)
		
		#plot_heading
		self.result_plot_head=CTkLabel(self.result, text="Plot:-",font=("Roboto",55,"bold"),text_color=("blue","#00ff11"))
		self.result_plot_head.place(relx=0.4,rely=0.6)
		
		#plot_data
		self.result_plot=CTkLabel(self.result, text=data["Plot"],wraplength=self.main.winfo_screenwidth()*0.5,font=("Roboto",25))
		self.result_plot.place(relx=0.4,rely=0.68)
		
		
		
		#for check Type is correct or not
		if data["Type"]!="movie" and self.search_head=="Movie":
			if mb.askyesno(title="Wrong Type",message="You searched for a movie\nBut We have a series\nWould You like to see it?"):
				pass
			else:
				return
		elif data["Type"]=="movie" and self.search_head!="Movie":
			if mb.askyesno(title="Wrong Type",message=f"You searched for a {self.search_head}\nBut We have a Movie\nWould You like to see it?"):
				pass
			else:
				return
		
		#display pg
		self.go_next_pg(self.result)
		
	
	
	#check available in local data or not
	def chk_locol(self,data):
		
		if data["Type"]=="movie":
			with open(r"Movies.csv",encoding="utf-8") as f:
				movie_reader=csv.reader(f)
				next(movie_reader)
				m_list=list(movie_reader)
			go=True 
			
			for i in m_list:
				if i==[]:
					continue
				if data["Title"].lower().strip() == i[0].lower().strip():
					go=False 
					break
			if go:
				n_e=[data["Title"],data["Year"],data["Genre"],data["imdbRating"],data["Language"],data["Director"],data["Country"]]
				with open(r"Movies.csv","a",encoding="utf-8") as f:
					writer=csv.writer(f)	
					writer.writerow(n_e)
		elif data["Type"]=="series":
			mx_list=[]
			#anime
			with open(r"Anime.csv",encoding="utf-8")as f:
				read=csv.reader(f)
				next(read)
				mx_list.extend(list(read))
				
			#ott
			with open(r"Webseries.csv",encoding="utf-8")as f:
				read=csv.reader(f)
				next(read)
				mx_list.extend(list(read))
				
			#k drama 
			with open(r"K_drama.csv",encoding="utf-8")as f:
				read=csv.reader(f)
				next(read)
				mx_list.extend(list(read))
				
			n="Netflix"
			go=True
			
			for i in mx_list:
				if i==[]:
					continue
				if data["Title"].lower().strip() == i[0].lower().strip():
					go=False
					break
			if go:	
				n_e=[data["Title"],data["Year"],n,data["Genre"],data["Language"],data["imdbRating"],data["Country"]]
				
				with open(r"Webseries.csv","a",encoding="utf-8")as f:
					writer=csv.writer(f)		
					writer.writerow(n_e)
			
		
		




if __name__=="__main__":
	Recommendation_App=App()
	
	
