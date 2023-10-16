import tkinter as tk

class Page(tk.Frame):
    def __init__(self, parent: tk.Frame, params: dict = None):     
        super().__init__(parent)
        self.params = params
        self._create()
        
    def show(self):
        self.content.grid(row=2, column=0, sticky="nsew")
        
    def hide(self):
        self.content.grid_forget()
        
    def _create(self, root):
        raise NotImplementedError("This method is abstract and must be override in child.")
    
    def _go_to(self, page_class, params: dict = None):
        from PresentationLayer.Shell import Shell
        Shell.go_to(page_class, params)
        
    def _push(self, page_class, params: dict = None):
        from PresentationLayer.Shell import Shell
        Shell.push(page_class, params)
        
    def _go_back(self):
        from PresentationLayer.Shell import Shell
        Shell.go_back()
        
    def _go_home(self):
        from PresentationLayer.Shell import Shell
        Shell.go_home()