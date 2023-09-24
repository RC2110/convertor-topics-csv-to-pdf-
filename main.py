from fpdf import FPDF
import pandas as pd

data = pd.read_csv("topics.csv")

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

for index, rows in data.iterrows():
        pdf.set_text_color(100,100,100)
        # set the header
        pdf.add_page()
        pdf.set_font(family="Times", style='B', size=24)
        pdf.cell(w=0, h=10, txt= rows['Topic'], align='L',ln=1)
        pdf.line(10,19,190,19)

        for i in range(19,271,7):
                pdf.line(10, i, 190, i)

        # Set the Footer
        pdf.ln(271)
        pdf.set_text_color(180, 180, 180)
        pdf.set_font(family="Times", style='I', size=12)
        pdf.cell(w=0, h=0, txt=rows['Topic'], align='R', ln=1)

        for i in range(rows['Pages']-1):
                pdf.add_page()
                pdf.ln(278)
                pdf.set_font(family="Times", style='I', size=12)
                pdf.cell(w=0, h=0, txt=rows['Topic'], align='R',ln=1)
                for i in range(19, 278, 7):
                        pdf.line(10, i, 190, i)

pdf.output("Output.pdf")
