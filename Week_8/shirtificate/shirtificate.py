from fpdf import FPDF

def main():
    name = input("Name: ")

    # create a new PDF object
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=48)
    pdf.cell(200, 80, txt="CS50 Shirtificate", align="C")
    pdf.image('shirtificate.png', x=15, y=90, w=180, h=180)
    pdf.set_font("helvetica", size=28)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x=60, y=160, txt="{} took CS50".format(name))
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()