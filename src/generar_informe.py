from fpdf import FPDF
import datetime
import src.create_image as create_image

class PDFWithBackground(FPDF):
    def __init__(self):
        super().__init__()
        self.background = None

    def set_background(self, image_path):
        self.background = image_path

    def add_page(self, orientation=''):
        super().add_page(orientation)
        if self.background:
            self.image(self.background, 0, 0, self.w, self.h)

    def footer(self):
        # Posición a 1.5 cm desde el fondo
        self.set_y(-15)
        # Configurar la fuente para el pie de página
        self.set_font('Arial', 'I', 8)
        # Número de página
        self.cell(0, 10, 'Página ' + str(self.page_no()), 0, 0, 'C')
    

def informe():
    pdf = PDFWithBackground()
    today = str(datetime.date.today())

    pdf.add_font('Ablation','', "fuente_FPDF/ablation.ttf", uni=True)
    pdf.set_background('imagenes/background.png')
    meses = create_image.consutar_deuda()
    
    ancho_pagina = 210
    margen = 30
    ancho = ancho_pagina - (2*margen)

    for i in range(0,len(meses),4):
        pdf.add_page()
        pdf.set_y(46)
        pdf.set_x(40)
        pdf.set_font('Courier',size=14)
        pdf.cell(0,0,f': {today}',0,1)
        
        pdf.image(f'imagenes/img_deuda_{meses[i]}.png', x=margen-6, y = 65, w = ancho/2 + 5)
        pdf.image(f'imagenes/img_deuda_{meses[i+1]}.png', x=ancho_pagina-margen-(ancho/2)+2, y = 65, w = ancho/2 + 5)
        pdf.image(f'imagenes/img_deuda_{meses[i+2]}.png', x=margen-6, y = 135, w = ancho/2 + 5)
        pdf.image(f'imagenes/img_deuda_{meses[i+3]}.png', x=ancho_pagina-margen-(ancho/2)+2, y = 135, w = ancho/2 +5)

    pdf.output('informes_pdf/reporte_mensual.pdf')
        
