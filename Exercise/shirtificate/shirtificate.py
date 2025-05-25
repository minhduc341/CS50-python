from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 36)
        self.cell(0, 20, "CS50 Shirtificate", align="C")

    def generate_shirtificate(self, name, output_file):
        # New page
        self.add_page()

        # Shirt's size and position
        shirt_width = 175
        shirt_height = 215
        x = (210 - shirt_width) / 2
        y = (297 - shirt_height) / 2

        # Add shirt
        self.image("shirtificate.png", x, y, shirt_width, shirt_height)

        # Name's size and position
        name_width = self.get_string_width(name)
        name_height = 24
        x = x + (shirt_width - name_width) / 2
        y = y + shirt_height / 3

        # Name's font, size and color
        self.set_font("Helvetica", size=name_height)
        self.set_text_color(255, 255, 255)

        # Add the name
        self.text(x, y, name)

        # Output the PDF to the specified file
        self.output(output_file)

def main():
    name = input("Name: ")
    shirtificate = Shirtificate()
    shirtificate.generate_shirtificate(name+' took Cs50', "shirtificate.pdf")

if __name__ == "__main__":
    main()