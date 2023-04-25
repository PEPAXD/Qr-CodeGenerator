import os
import tkinter
import customtkinter
import qrcode
from PIL import Image

def generate_qrcode(link):

    #CREATE QR-CODE
    qr = qrcode.QRCode(version=1, box_size=30, border=2)

    #ADD DATA
    qr.add_data(link)

    #GENERATE QR CODE
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    #SAVE IMAGE-QR
    img.save("QRLink.png")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window appearance
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("dark-blue")

        # configure window title
        self.title("Qr-CodeGenerator by-MauroPepa.py")

        # configure window size
        self.geometry(f"{400}x{450}")
        self.resizable(False, False)

        # create canvas
        self.frame = customtkinter.CTkFrame(master=self, corner_radius=30)
        self.frame.pack(fill="both", expand=True)
        self.frame.place(relx=0.07, rely=0.07, relwidth=0.87, relheight=0.87)

        # load image qr ---> GITHUB/PEPAXD
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "GITHUBLINK.png")),size=(250, 250))
        self.home_frame_large_image_label = customtkinter.CTkLabel(master=self, text="", image=self.large_test_image)
        self.home_frame_large_image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # TEXT-LABEL
        self.label = customtkinter.CTkLabel(master=self.frame, text="QR-CODEGENERATOR", font=("Arial Black", 24, "underline"))
        self.label.place(relx=0.5, rely=0.08, anchor=tkinter.CENTER)

        # create entry link-qr
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Add link and press the button", width=220)
        self.entry.place(relx=0.63, rely=0.87, anchor=tkinter.CENTER)

        def click_button():

            #INPUT LINK-USER
            Link = self.entry.get()

            #GENERATE QR
            generate_qrcode(Link)

            #PRINT NEW QR.PNG
            self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "QRLink.png")), size=(250, 250))
            self.home_frame_large_image_label = customtkinter.CTkLabel(master=self, text="", image=self.large_test_image)
            self.home_frame_large_image_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # create button QR-GENERATOR
        self.main_button = customtkinter.CTkButton(master=self, command=click_button, fg_color="transparent", text="GENERATE QR", width=50, border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button.place(relx=0.23, rely=0.87, anchor=tkinter.CENTER)

if __name__ == "__main__":
    app = App()
    app.mainloop()