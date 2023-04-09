import DeveloperCredits
import qrcode
import PySimpleGUI as sg

def inputDataQR():

    # Define the layout of the window
    layout = [
        [sg.Text("INGRESE LINK DE ACCESO: "), sg.InputText(key="-input-")],
        [sg.Button("Ok"), sg.Exit()],
    ]

    # Create the window
    window = sg.Window("QR-GENERATOR", layout, element_justification="right")

    # Event loop window
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == "Ok":
            link = values["-input-"]
            if link != "":
                sg.popup("EL QR SE HA GENERADO!!!")
                return link
                break

    # Close the window
    window.close()



def generate_qrcode(link):

    #CREATE QR-CODE
    qr = qrcode.QRCode(version=1, box_size=30, border=2)

    #ADD DATA
    qr.add_data(link)

    #GENERATE QR CODE
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    #SAVE IMAGE-QR
    img.save("MyQRLink.png")

def main():
    DeveloperCredits.printCredits()
    link = inputDataQR()
    generate_qrcode(link)

#EJECUTAR SCRIPT
if __name__ == '__main__':
    main()
