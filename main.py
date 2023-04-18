from linkedin_api import Linkedin
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph

pagex = 612
pagey = 792
def get_details():
    logininfo = []
    file = open('login-info.txt', "r")
    for line in file:
        logininfo.append(line.split()[1])
    return logininfo

logindetails = get_details()
# Authenticate using any Linkedin account credentials
api = Linkedin(logindetails[0], logindetails[1])
profile = api.get_profile("willwhitehead122")

NAME = profile["firstName"] + " " +profile["lastName"]
# experience = profile["experience"]
FONT_NAME = 'Times-Roman'
FONT_SIZE = 12
def centertext(canvas, yvalue, text):
    text_width = stringWidth(text, FONT_NAME, FONT_SIZE)
    pdf_text_object = canvas.beginText((pagex - text_width) / 2.0, yvalue)
    pdf_text_object.textOut(text) # or: pdf_text_object.textLine(text) etc.
    canvas.drawString((pagex - text_width) / 2.0, yvalue, text)

p1 = Paragraph('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Suspendisse sed nisi lacus sed viverra tellus in. Dictumst vestibulum rhoncus est pellentesque elit ullamcorper dignissim cras. Morbi tincidunt ornare massa eget egestas purus viverra accumsan in. Bibendum enim facilisis gravida neque convallis a cras semper auctor. Magna etiam tempor orci eu lobortis elementum nibh tellus. Scelerisque eu ultrices vitae auctor eu augue. Massa tincidunt dui ut ornare lectus sit amet. Mauris pharetra et ultrices neque ornare aenean euismod. Hac habitasse platea dictumst vestibulum. Morbi tempus iaculis urna id volutpat lacus laoreet non. Tortor vitae purus faucibus ornare suspendisse sed nisi lacus. Velit ut tortor pretium viverra suspendisse potenti.')

def form(path):
    my_canvas = canvas.Canvas(path, pagesize=letter)
    my_canvas.setLineWidth(.3)
    my_canvas.setFont(FONT_NAME, FONT_SIZE)
    centertext(my_canvas, 760, NAME )
    my_canvas.line(30, 750, 582, 750)
    centertext(my_canvas, 700, "test123" )
    p1.wrapOn(my_canvas, 300, 50)
    p1.drawOn(my_canvas, 50, 600)

    # my_canvas.drawString(30, 750, 'OFFICIAL COMMUNIQUE')
    # my_canvas.drawString(30, 735, 'OF ACME INDUSTRIES')
    # my_canvas.drawString(500, 750, "12/12/2010")
    # my_canvas.line(480, 747, 580, 747)
    # my_canvas.drawString(500, 725, "$1,000.00")
    # my_canvas.line(378, 723, 580, 723)
    # my_canvas.drawString(30, 703, 'RECEIVED BY:')
    # my_canvas.line(120, 700, 580, 700)
    # my_canvas.drawString(120, 703, "JOHN DOE")
    my_canvas.save()
if __name__ == '__main__':
    form('canvas_form.pdf')