from PresentationLayer.Pages.Page import Page as Page
import tkinter as tk

class ExamplePage(Page):
        
    def _create(self):
        id = self.params["id"]
        text = tk.Label(self, text=f"Detail {id}")
        text.pack()
        
        button = tk.Button(self, text="Další stránka", command=self.go_to_example)
        button.pack()
        
        button = tk.Button(self, text="Nové okno", command=self.push_example)
        button.pack()
        
        
    def go_to_example(self):
        self.params["id"] += 1
        self._go_to(ExamplePage, self.params)
        
    def push_example(self):
        self.params["id"] = 1
        self._push(ExamplePage, self.params)