from PresentationLayer.Pages.Page import Page as Page
import tkinter as tk

class MainPage(Page):
    
    def _create(self):
        main_label = tk.Label(self, text="Hlavní stránka")
        main_label.pack(padx=10, pady=10)
        
        next_page_button = tk.Button(self, text="Detail", command=self.go_to_example)
        next_page_button.pack(padx=10, pady=10)
        
    def go_to_example(self):
        from PresentationLayer.Pages.ExamplePage import ExamplePage
        params = {"id": 1}
        self._go_to(ExamplePage, params)