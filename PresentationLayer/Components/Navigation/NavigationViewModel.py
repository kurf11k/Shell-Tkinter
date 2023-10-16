from PresentationLayer.ViewModel import ViewModel
from PresentationLayer.Shell import Shell

class NavigationViewModel(ViewModel):
    def __init__(self):
        self.title = ""
        
    def go_back_command(self):
        Shell.go_back()
        
        if Shell.can_go_back():
            self.back_button.grid(column=0, row=0)
        else:
            self.back_button.ungrid()