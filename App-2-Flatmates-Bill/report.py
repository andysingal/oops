from fpdf import FPDF
import webbrowser,os
class PdfReport:
    """
    Creates a Pdf file that contains data about the flatmates
    such as their names, their due amount and the period of the
    bill
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self,flatmate1, flatmate2,bill):
        flatmat1_pay = str(round(flatmate1.pays(bill,flatmate2),2))
        flatmat2_pay = str (round (flatmate2.pays (bill, flatmate1), 2))

        pdf = FPDF (orientation='P', unit='pt', format='A4')
        pdf.add_page ()

        #Add Image
        pdf.image("files/house.png", w=30,h=30)

        # Add some text
        pdf.set_font (family='Times', size=24, style='B')
        pdf.cell (w=0, h=80, txt="Flatesmate Bill", border=0, align="C", ln=1)

        #Insert Period label and Value
        pdf.set_font (family='Times', size=14, style='B')
        pdf.cell (w=100, h=40, txt="Period:", border=0)
        pdf.cell (w=150, h=40, txt=bill.period, border=0,ln=1)

        #Insert name and due amount
        pdf.set_font (family='Times', size=12)
        pdf.cell (w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell (w=200, h=25, txt=flatmat1_pay, border=0,ln=1)


        pdf.cell (w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell (w=200, h=25, txt=flatmat2_pay, border=0, ln=1)

        pdf.output(self.filename)

        os.chdir("files")
        webbrowser.open('file://'+os.path.realpath(self.filename))