
import flet
from flet import Dropdown, ElevatedButton, dropdown, Text, TextField

def main(page):
    page.title ='percentil'
    page.theme_mode = flet.ThemeMode.LIGHT
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.padding = 100
    page.spacing = 15
    page.navigation_bar = flet.NavigationBar(
        destinations=[
            flet.NavigationDestination(icon=flet.icons.EXPLORE, label="Explore"),
            flet.NavigationDestination(icon=flet.icons.COMMUTE, label="Commute"),
            flet.NavigationDestination(icon=flet.icons.BOOKMARK_BORDER, selected_icon=flet.icons.BOOKMARK, label="Explore"),
            flet.NavigationDestination(icon=flet.icons.AUDIOTRACK, label = "Music")
        ]
    )
    page.update()
    
    def theme_changed(e):
        page.theme_mode = (flet.ThemeMode.DARK if page.theme_mode == flet.ThemeMode.LIGHT else flet.ThemeMode.LIGHT)
        page.update()
    
    def calcular(e):
        if casilla.value == 'peso':
            texto.value = f'El peso en libras es {int(int(campo_de_peso.value)*2.2)}'
        else:
            texto.value = f'La talla en metros es {float(int(campo_de_talla.value)/100)}'
        page.update()
   
                
    campo_de_peso = TextField(label ='ingrese el peso en kg: ', width = 350)
    campo_de_talla = TextField(label ='ingrese la talla en cm: ', width = 350)
    
    boton = ElevatedButton(text = 'calcular', on_click=calcular)
    
    texto = Text(value='', width=300, size=20)
            
    casilla = Dropdown(width=100, options= 
                       [dropdown.Option("peso"),
                        dropdown.Option("talla")] )
    c = flet.Switch(label="Light theme", on_change = theme_changed)
    
    
    page.add(casilla, 
             campo_de_peso, 
             campo_de_talla, 
             boton, 
             texto,
             c
    )

flet.app(target=main)
