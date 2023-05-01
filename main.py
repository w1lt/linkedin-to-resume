from linkedin_api import Linkedin
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph

from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib import colors

styles = getSampleStyleSheet()

styles.add(ParagraphStyle(name='right',
                          alignment=TA_RIGHT,
                          fontName='Times-Roman',
                          fontSize=12,
                          textColor=colors.black,
                          leading=8,
                          wordWrap='LTR',
                          splitLongWords=True,
                          ))

pagex = 612
pagey = 792
def get_details():
    logininfo = []
    file = open('login-info.txt', "r")
    for line in file:
        logininfo.append(line.split()[1])
    return logininfo

logindetails = get_details()

api = Linkedin(logindetails[0], logindetails[1])
profile = api.get_profile("willwhitehead122")

def add_text(canvas, text, style="right"):
    p = Paragraph(text, styles[style])
    p.wrapOn(canvas, 300, 50)
    p.drawOn(canvas, 50, 400)

NAME = "Will Whitehead"#profile["firstName"] + " " +profile["lastName"]
def get_eduction(num):
    eduction =  profile["education"][num]
    edprops = {
    "degree": eduction["degreeName"],
    "field_of_study": eduction["fieldOfStudy"],
    "activities": eduction["activities"].split("\n"),
    "school_name": eduction["schoolName"],
    "time_period": eduction["timePeriod"],
    }
    return edprops
FONT_NAME = 'Times-Roman'
FONT_SIZE = 12
def centertext(canvas, yvalue, text):
    text_width = stringWidth(text, FONT_NAME, FONT_SIZE)
    pdf_text_object = canvas.beginText((pagex - text_width) / 2.0, yvalue)
    pdf_text_object.textOut(text) # or: pdf_text_object.textLine(text) etc.
    canvas.drawString((pagex - text_width) / 2.0, yvalue, text)

p1 = Paragraph('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Suspendisse sed nisi lacus sed viverra tellus in. Dictumst vestibulum rhoncus est pellentesque elit ullamcorper dignissim cras. Morbi tincidunt ornare massa eget egestas purus viverra accumsan in. Bibendum enim facilisis gravida neque convallis a cras semper auctor. Magna etiam tempor orci eu lobortis elementum nibh tellus. Scelerisque eu ultrices vitae auctor eu augue. Massa tincidunt dui ut ornare lectus sit amet. Mauris pharetra et ultrices neque ornare aenean euismod. Hac habitasse platea dictumst vestibulum. Morbi tempus iaculis urna id volutpat lacus laoreet non. Tortor vitae purus faucibus ornare suspendisse sed nisi lacus. Velit ut tortor pretium viverra suspendisse potenti.')

def form(path):
    
    c = canvas.Canvas(path, pagesize=letter)
    c.setLineWidth(.3)
    # c.setFont(FONT_NAME, FONT_SIZE)
    c.setFont('Times-Bold', 12)
    centertext(c, 740, NAME )
    c.line(50, 735, 562, 735)
    centertext(c, 680, "Education" )
    
    add_text(c, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua")
    # centertext(my_canvas, 700, "test123" )
    # p1.wrapOn(my_canvas, 300, 50)
    # p1.drawOn(my_canvas, 50, 600)
    c.save()
if __name__ == '__main__':
    form('canvas_form.pdf')