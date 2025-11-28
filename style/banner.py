from rich import print
from rich.console import Console
from rich.text import Text
from rich.theme import Theme

def display_banner():
    custom_theme = Theme({
        "link": "dark_orange3"
    })
    console1 = Console(theme=custom_theme)
    console = Console()

    banner = """
       .d8888b.                                    
      d88P  Y88b                                   
      Y88b.                                        
       "Y888b.    .d88b.   .d8888b 888d888 8888b.  
          "Y88b. d8P  Y8b d88P"    888P"      "88b 
            "888 88888888 888      888    .d888888 
      Y88b  d88P Y8b.     Y88b.    888    888  888 
       "Y8888P"   "Y8888   "Y8888P 888    "Y888888 
                                           """
    
    banner3 = "[+] Developed by i1zco"


    banner_text1 = Text(banner, style="orange3")
   # banner_text2 = Text(banner4, style="red3")
    banner_text3 = Text(banner3, style="dark_orange3")


    centered_text1 = "{:^60}".format(banner_text1.plain)
    #centered_text2 = "{:^60}".format(banner_text2.plain)
    centered_text3 = "{:^70}".format(banner_text3.plain)


    console.print(Text(centered_text1, style="red1"))
    #console.print(Text(centered_text2, style="red1"))
    console1.print(Text(centered_text3, style="dark_orange3"))

