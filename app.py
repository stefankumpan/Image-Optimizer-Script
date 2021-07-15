import eel
import tkinter
import tkinter.filedialog as filedialog

Input_Folder = 'None'
Output_Folder = 'None'

def RuntThis():
    print(f"Input( {Input_Folder} ) - Output( {Output_Folder} )")

@eel.expose
def Select_Folder(folder):
    root = tkinter.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    directory_path = filedialog.askdirectory()
    print(directory_path)
    if folder == 'input': 
        Input_Folder = directory_path
        print(f"Input Folder: {Input_Folder}")
    if folder == "output":
        Output_Folder = directory_path
        print(f"Output Folder: {Output_Folder}")

    RuntThis()

    return directory_path


import generate_images






eel.init('webapp') # or the name of your directory
eel.start('index.html', size=(820, 420), Port="8686")   
