import tkinter as tk
from tkinter import font

from PresentationLayer.Pages.Page import Page as Page
from PresentationLayer.Menu import Menu as Menu

class Shell:
    PAGE_HISTORY_STACK = []
    
    @classmethod
    def init(cls, title: str, width: int, height: int, defined_menu: Menu, main_page = None):
       
        cls.WINDOW = cls.__create_window(title, width, height)
        
        if(defined_menu != None):
            cls.MENU = defined_menu.get_frame(cls.WINDOW)
            cls.MENU.grid(column=0, row=0, sticky="ew") 
         
        cls.NAVIGATION = cls.__create_navigation(cls.WINDOW)
        
        cls.CONTENT = None       
        if main_page != None:
            page = main_page(cls.WINDOW)
            cls.__change_content(page)
            
        cls.WINDOW.mainloop()
    
    @classmethod
    def __create_window(cls, title, width, height):
        root = tk.Tk()
        root.title(title)
        root.geometry(f"{width}x{height}")
        root.configure(bg="lightblue")
        root.columnconfigure(0, weight=1) 
        root.rowconfigure(2, weight=1)                                 
        return root
    
    @classmethod
    def __create_navigation(cls, root):
        cls.navigation_frame = tk.Frame(root, bg="purple")
        
        cls.back_button = tk.Button(cls.navigation_frame, text="←", 
                                     command=cls.go_back, 
                                     font=font.Font(size=15, weight="bold"), 
                                     fg="white", 
                                     bg="purple",
                                     borderwidth=0, 
                                     relief=tk.FLAT)     
        cls.back_button.pack(side="left", padx=10)
    
    @classmethod
    def __render_navigation(cls):
        if len(cls.PAGE_HISTORY_STACK) > 0:
            cls.navigation_frame.grid(row=1, column=0, sticky="ew")
        else:
            cls.navigation_frame.grid_forget()
    
    @classmethod
    def __change_content(cls, new_page: Page):
        if cls.CONTENT != None:
            old_page = cls.CONTENT  
            old_page.grid_forget()
        
        new_page.grid(row=2, column=0, sticky="nsew")
        cls.CONTENT = new_page 
        cls.__render_navigation()      
    
    
    @classmethod
    def go_to(cls, page_class, params: dict = None):
        old_page = cls.CONTENT
        cls.PAGE_HISTORY_STACK.append(old_page)
        new_page = page_class(cls.WINDOW, params)
        cls.__change_content(new_page)
        
    @classmethod
    def push(cls, page_class, params: dict = None):
        cls.PAGE_HISTORY_STACK = []
        new_page = page_class(cls.WINDOW, params)
        cls.__change_content(new_page)
    
    @classmethod
    def go_back(cls):     
        page = cls.PAGE_HISTORY_STACK.pop()
        cls.__change_content(page)
    
    
    @classmethod
    def go_home(cls):
        pass 