import flet
from flet import Text, TextField, ElevatedButton, Page, Dropdown, dropdown, ControlEvent
from tabla import tabla_peso_edad_boys, tabla_peso_edad_girls, tabla_talla_edad_boys, tabla_talla_edad_girls
    
class PercentileFinder:
    def __init__(self, tabla_percentiles):
        self.tabla_percentiles = tabla_percentiles
        self.percentiles = [3, 10, 25, 50, 75, 90, 97]

    def find_percentile_edad_peso(self, edad, peso):
        fila = min(edad-1, len(self.tabla_percentiles) - 1)

        for p in self.percentiles:
            if peso <= self.tabla_percentiles.loc[fila, p]:
                return p
        return 97

class PercentileFindertalla:
    def __init__(self, tabla_percentiles_talla):
        self.tabla_percentiles_talla = tabla_percentiles_talla
        self.percentiles = [3, 10, 25, 50, 75, 90, 97]
            
    def find_percentile_edad_talla(self, edad, talla):
        fila = min(edad-1, len(self.tabla_percentiles_talla) - 1)

        for p in self.percentiles:
            if talla <= self.tabla_percentiles_talla.loc[fila, p]:
                return p
        return 97
    
def main(page: Page):
    page.title = "Cálculo de percentiles pediátricos"
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.window_width = 390
    page.window_height = 644
    
    
    def sexo(e: ControlEvent):
        if lista.value == "Boy":
            pf.tabla_percentiles = tabla_peso_edad_boys
            pt.tabla_percentiles_talla = tabla_talla_edad_boys
        elif lista.value == "Girl":
            pf.tabla_percentiles = tabla_peso_edad_girls
            pt.tabla_percentiles_talla = tabla_talla_edad_girls
        page.update()
    
    pf = PercentileFinder(sexo)
    pt = PercentileFindertalla(sexo)
    
    def on_find_percentile_edad_peso_click(e):
        edad = int(edad_input.value)
        peso = float(peso_input.value)
        percentil = pf.find_percentile_edad_peso(edad, peso)
        percentil_anterior = pf.percentiles[pf.percentiles.index(percentil) - 1] if percentil!= 3 else None

        if percentil_anterior != '':
            result_text.value = f'El bebé se encuentra entre el percentil {percentil_anterior}-{percentil} de peso para su edad.'
        else:
            result_text.value = f'El bebé se encuentra en el percentil 3 de peso para su edad.'
        page.update()
    
    def on_find_percentile_edad_talla_click(e):
        edad = int(edad_input.value)
        talla = float(talla_input.value)
        percentil = pt.find_percentile_edad_talla(edad, talla)
        percentil_anterior = pt.percentiles[pt.percentiles.index(percentil) - 1] if percentil!= 3 else None

        if percentil_anterior != '':
            texto_2.value = f'El bebé se encuentra entre el percentil {percentil_anterior}-{percentil} de talla para su edad.'
        else:
            texto_2.value = f'El bebé se encuentra en el percentil 3 de talla para su edad.'
        page.update()
    
    def on_button_click(e):
        on_find_percentile_edad_peso_click(e)
        on_find_percentile_edad_talla_click(e)
    
    edad_input = TextField(label="Edad (meses):", width=290)
    peso_input = TextField(label="Peso (kg):", width=290)
    talla_input = TextField(label="Talla (cm):", width=290)
    
    lista = Dropdown(hint_text="¿Cual es el sexo?",
        width= 200, on_change=sexo, options=[
        dropdown.Option('Girl'),
        dropdown.Option('Boy'),])    
    boton = ElevatedButton(text="Encontrar percentil", on_click=(on_button_click))
    result_text = Text(value="")
    texto_2 = Text(value="")
    
    page.add(lista,
        edad_input, 
        peso_input,
        talla_input, 
        boton, 
        result_text,
        texto_2)

flet.app(target= main)