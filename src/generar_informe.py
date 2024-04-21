from fpdf import FPDF

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
    import datetime
    today = str(datetime.date.today())
    pdf.add_font('Ablation','', "fuente_FPDF/ablation.ttf", uni=True)
    pdf.set_background('imagenes/background.png')

    pdf.add_page()

    pdf.set_y(46.1)
    pdf.set_font('Courier',size=25)
    pdf.cell(0,0,today,0,1,'C')

    pdf.set_y(180)
    pdf.set_font('Ablation',size=100)
    pdf.cell(0,0,'TEST',0,1,'C')

    pdf.image('imagenes/img_deuda_total.png', x=(210 - 160)/2, y = 65, w = 160)

    pdf.output('informes_pdf/reporte_mensual.pdf')
        
