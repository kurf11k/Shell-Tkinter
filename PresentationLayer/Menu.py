import tkinter as tk
from PresentationLayer.Pages.Page import Page

class MenuItem:
    def __init__(self, title: str, page: Page):
        self.title = title
        self.page = page
        
    def create_component(self, parent):
        menu_button = tk.Button(parent, text=self.title, command=self.push_new_page_command)
        menu_button.pack(side="left")
        
    def push_new_page_command(self):
        from PresentationLayer.Shell import Shell
        Shell.push(self.page)

class Menu:
    def __init__(self, position = "top"):
        self.position = position
        self.items = []
    
    def add_navigation_item(self, title: str, page: Page):
        self.items.append(MenuItem(title, page))
        return self
        
    def get_frame(self, parent):
        root = tk.Frame(parent)
        for item in self.items:
            item.create_component(root)
            
        return root
    