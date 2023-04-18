from linkedin_api import Linkedin
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

dimensions = (612, 792)
def get_details():
    logininfo = []
    file = open('login-info.txt', "r")
    for line in file:
        logininfo.append(line.split()[1])
    return logininfo

logindetails = get_details()
print(logindetails)
# Authenticate using any Linkedin account credentials
api = Linkedin(logindetails[0], logindetails[1])
profile = api.get_profile("willwhitehead122")

NAME = profile["firstName"] + " " +profile["lastName"]
experience = profile["experience"]
print(profile)
    
def form(path):
    my_canvas = canvas.Canvas(path, pagesize=letter)
    my_canvas.setLineWidth(.3)
    my_canvas.setFont('Helvetica', 12)
    my_canvas.drawString(30, 750, 'OFFICIAL COMMUNIQUE')
    my_canvas.drawString(30, 735, 'OF ACME INDUSTRIES')
    my_canvas.drawString(500, 750, "12/12/2010")
    my_canvas.line(480, 747, 580, 747)
    my_canvas.drawString(250, 760, NAME)
    my_canvas.drawString(500, 725, "$1,000.00")
    my_canvas.line(378, 723, 580, 723)
    my_canvas.drawString(30, 703, 'RECEIVED BY:')
    my_canvas.line(120, 700, 580, 700)
    my_canvas.drawString(120, 703, "JOHN DOE")
    my_canvas.save()
if __name__ == '__main__':
    form('canvas_form.pdf')