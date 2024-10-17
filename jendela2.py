import PySimpleGUI as sg
sg.theme("DarkRed1")
sg.theme_text_color("#007fff")

window = sg.Window(title="Profile",layout=[[sg.Text("NPM : 2210010362")],
                                                   [sg.Text("NAMA : YERRI NUR RAHMAN")],
                                                   [sg.Text("KELAS : 5-O REGULER PAGI BANJARMASIN")],
                                                   [sg.Text("MATKUL : PEMROGRAMAN VISUAL 3")]],size=(400,200))
window()
window.close()