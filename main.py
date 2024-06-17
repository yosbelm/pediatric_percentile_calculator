import flet
from flet import Text, TextField, Page, Dropdown, dropdown, ControlEvent, CupertinoAlertDialog, CupertinoDialogAction, KeyboardType, TextStyle, TextThemeStyle, CupertinoFilledButton, Row, Container
from tabla import tabla_peso_edad_boys, tabla_peso_edad_girls, tabla_talla_edad_boys, tabla_talla_edad_girls, tabla_talla_peso_boys, tabla_talla_peso_girls, tabla_peso_edad_boys_years, tabla_peso_edad_girls_years, tabla_talla_edad_boys_years, tabla_talla_edad_girls_years
    
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

class PercentileFindertallapeso:
    def __init__(self, tabla_talla_peso):
        self.tabla_talla_peso = tabla_talla_peso
        self.percentiles = [3, 10, 25, 50, 75, 90, 97]
        self.talla = ["[50.0-51.9]", "[52.0-53.9]", "[54.0-55.9]", "[56.0-57.9]", "[58.0-59.9]", "[60.0-61.9]", "[62.0-63.9]", "[64.0-65.9]", "[66.0-67.9]", "[68.0-69.9]", "[70.0-71.9]", "[72.0-73.9]", "[74.0-75.9]", "[76.0-77.9]", "[78.0-79.9]", "[80.0-81.9]", "[82.0-83.9]", "[84.0-85.9]", "[86.0-87.9]", "[88.0-89.9]", "[90.0-91.9]", "[92.0-93.9]", "[94.0-95.9]","[96.0-97.9]", "[98.0-99.9]", "[100.0-101.9]", "[102.0-103.9]", "[104.0-105.9]", "[106.0-107.9]", "[108.0-109.9]", "[110.0-111.9]", "[112.0-113.9]", "[114.0-115.9]","[116.0-117.9]", "[118.0-119.9]","[120.0-121.9]", "[122.0-123.9]", "[124.0-125.9]", "[126.0-127.9]", "[128.0-129.9]", "[130.0-131.9]", "[132.0-133.9]", "[134.0-135.9]", "[136.0-137.9]", "[138.0-139.9]", "[140.0-141.9]", "[142.0-143.9]", "[144.0-145.9]", "[146.0-147.9]", "[148.0-149.9]", "[150.0-151.9]", "[152.0-153.9]", "[154.0-155.9]", "[156.0-157.9]", "[158.0-159.9]", "[160.0-161.9]", "[162.0-163.9]", "[164.0-165.9]", "[166.0-167.9]", "[168.0-169.9]", "[170.0-171.9]", "[172.0-173.9]", "[174.0-175.9]", "[176.0-177.9]", "[178.0-179.9]"]   
    
    def parse_range(self, range_peso):
        lower, upper = map(float, range_peso.strip('[]').split('-'))
        return lower, upper 
         
    def buscar(self, peso, talla):
        for i, fila in enumerate(self.talla):
            if self.parse_range(fila)[0] <= talla < self.parse_range(fila)[1]:
                
                for p in self.percentiles:
                    if peso <= self.tabla_talla_peso.loc[i, p]:
                        return p     
                return 97
            
def main(page: Page):
    page.title = "Pediatric percentile calculator"
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.window_width = 390
    page.window_height = 644
    
    def edad(e: ControlEvent):
        if edad_dropdown.value == "Months":
            pf.tabla_percentiles = tabla_peso_edad_boys
            pf.tabla_percentiles = tabla_peso_edad_girls
            pt.tabla_percentiles_talla = tabla_talla_edad_boys  
            pt.tabla_percentiles_talla = tabla_talla_edad_girls    
        elif edad_dropdown.value == "Years":
            pf.tabla_percentiles = tabla_peso_edad_boys_years
            pf.tabla_percentiles = tabla_peso_edad_girls_years
            pt.tabla_percentiles_talla = tabla_talla_edad_boys_years
            pt.tabla_percentiles_talla = tabla_talla_edad_girls_years           
        page.update()
        
    def sexo(e: ControlEvent):
        if lista.value == "Boy":
            pf.tabla_percentiles = tabla_peso_edad_boys
            pt.tabla_percentiles_talla = tabla_talla_edad_boys
            ptp.tabla_talla_peso = tabla_talla_peso_boys
        elif lista.value == "Girl":
            pf.tabla_percentiles = tabla_peso_edad_girls
            pt.tabla_percentiles_talla = tabla_talla_edad_girls
            ptp.tabla_talla_peso = tabla_talla_peso_girls
        page.update()
            
    pf = PercentileFinder(sexo)
    pt = PercentileFindertalla(sexo)
    ptp = PercentileFindertallapeso(sexo)
    
    def on_find_percentile_edad_peso_click(e):
        edad = int(edad_input.value)
        peso = float(peso_input.value)
        percentil = pf.find_percentile_edad_peso(edad, peso)
        percentil_anterior = pf.percentiles[pf.percentiles.index(percentil) - 1] if percentil!= 3 else None

        if percentil_anterior == None:
            if lista.value == "Girl" and edad_dropdown.value == "Months":
                result_text.value = f'W/A: The baby is in the 3rd percentile for weight for her age.'
            elif lista.value == "Girl" and edad_dropdown.value == "Years":
                result_text.value = f'W/A: The girl is in the 3rd percentile for weight for her age.'
              
            elif  lista.value == "Boy" and edad_dropdown.value == "Months":
                result_text.value = f'W/A: The baby is in the 3rd percentile for weight for her age.'
            elif  lista.value == "Boy" and edad_dropdown.value == "Years":
                result_text.value = f'W/A: The boy is in the 3rd percentile for weight for her age.'
        elif percentil_anterior != '':
            result_text.value = f'W/A: {percentil_anterior}-{percentil}'
        page.update()
    
    def on_find_percentile_edad_talla_click(e):
        edad = int(edad_input.value)
        talla = float(talla_input.value)
        percentil = pt.find_percentile_edad_talla(edad, talla)
        percentil_anterior = pt.percentiles[pt.percentiles.index(percentil) - 1] if percentil!= 3 else None

        if percentil_anterior == None:
            if lista.value == "Girl" and edad_dropdown.value == "Meses":
                texto_2.value = f'H/A The baby is in the 3rd percentile for height for her age.'
            elif lista.value =="Girl" and edad_dropdown.value == "Years":
                texto_2.value = f'H/A: The girl is in the 3rd percentile for height for her age.' 
            
            elif  lista.value == "Boy" and edad_dropdown.value == "Meses":
                texto_2.value = f'H/A: The baby is in the 3rd percentile for height for her age.'
            elif lista.value =="Boy" and edad_dropdown.value == "Years":
                texto_2.value = f'H/A: The boy is in the 3rd percentile for height for her age.'
        elif percentil_anterior != '':
            texto_2.value = f'H/A: {percentil_anterior}-{percentil}'
        page.update()
    
    def on_find_percentile_talla_peso_click(e):
        talla = float(talla_input.value)
        peso = float(peso_input.value)
        percentil = ptp.buscar(peso, talla)
        percentil_anterior = pf.percentiles[ptp.percentiles.index(percentil) - 1] if percentil!= 3 else None

        if percentil_anterior == None:
            if lista.value == "Girl" and edad_dropdown.value == "Months":
                texto_3.value = f'W/H: The baby is in the 3rd percentile for weight for her height.'
            elif lista.value =="Girl" and edad_dropdown.value == "Years":
                texto_3.value = f'W/H: The girl is in the 3rd percentile for weight for her height.'
                
            elif  lista.value == "Boy" and edad_dropdown.value == "Months":
                texto_3.value = f'W/H: The baby is in the 3rd percentile for weight for her height.'
            elif lista.value =="Boy" and edad_dropdown.value == "Years":
                texto_3.value = f'W/H: The boy is in the 3rd percentile for weight for her height.'
        elif percentil_anterior != '':
            texto_3.value = f'W/H: {percentil_anterior}-{percentil}'
        page.update()
    
    def on_button_click(e):
        on_find_percentile_edad_peso_click(e)
        on_find_percentile_edad_talla_click(e)
        on_find_percentile_talla_peso_click(e)
        open_cupertino_dialog(e)
    
    def close_cupertino_dialog(e):
        cupertino_alert_dialog.open = False
        page.update()
    
    def open_cupertino_dialog(e):
        cupertino_alert_dialog.content.value = f'{result_text.value}\n{texto_2.value}\n{texto_3.value}'
        page.dialog = cupertino_alert_dialog
        cupertino_alert_dialog.open = True
        page.update()
    
    cupertino_alert_dialog = CupertinoAlertDialog(
        title=Text("Results", text_align='center'),
        content=Text(value="", style=TextThemeStyle.BODY_MEDIUM),
        actions=[
            CupertinoDialogAction(
                "OK",
                text_style=TextStyle(italic=True),
                on_click=close_cupertino_dialog
            ),
        ]
    )
    edad_input = TextField(label="Age (month or years):", width=290, keyboard_type= KeyboardType.NUMBER)
    peso_input = TextField(label="Weight (kg):", width=290, keyboard_type= KeyboardType.NUMBER)
    talla_input = TextField(label="Height (cm):", width=290, keyboard_type= KeyboardType.NUMBER)
    
    lista = Dropdown(hint_text="What is the gender?",
        width= 200, on_change=sexo, options=[
        dropdown.Option('Girl'),
        dropdown.Option('Boy'),]) 
    edad_dropdown = Dropdown(hint_text="Choose",
        width= 100, on_change=edad, options=[
        dropdown.Option('Months'),
        dropdown.Option('Years'),]
    )   
    boton = CupertinoFilledButton(
            content=Text("Calculate"),
            opacity_on_click=0.3,
            on_click=on_button_click,
            width=200
        )
    result_text = Text(value="")
    texto_2 = Text(value="")
    texto_3 = Text(value="")
    
    page.add(
        lista,
        Row(controls=[
                Container(
                    expand=2,
                    content=edad_input,),
                Container(
                    expand=1, 
                    content=edad_dropdown)
                ]
            ), 
        peso_input,
        talla_input, 
        boton, 
        )

flet.app(target= main)