from PresentationLayer.Shell import Shell as Shell
from PresentationLayer.Menu import Menu as Menu
from PresentationLayer.Pages.MainPage import MainPage as MainPage


menu = Menu()
menu.add_navigation_item("Hlavní stránka", MainPage)

Shell.init("Aplikace", 600, 200, menu, MainPage)