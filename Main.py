import csv
import PySimpleGUI as sg

sg.theme('Light Green 4')

def StartMenu():
    layout = [[sg.Image("gradientLogo.png", subsample = 2, pad = (0,20))], [sg.Button("Today's outfit", size=(15, 1))], 
              [sg.Button("Add clothes", size=(15, 1))], [sg.Button("Change location", size=(15, 1))], 
              [sg.Button("Credits", pad = (0,20)), sg.Push(), sg.Text("Version 1.0.0")]]

    window = sg.Window("ChromaCloset Outfit Generator", layout, element_justification = 'c', font = "Cambria", 
                       icon = "shirtIcon.ico")

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Today's outfit":
            window.close()
            TodaysOutfitScreen()
            window.close()
        elif event == "Credits":
            window.close()
            CreditsScreen()
            window.close()
        elif event == "Add clothes":
            window.close()
            AddClothesScreen()
            window.close()
        elif event == "Change location":
            window.close()
            ChangeLocScreen()
            window.close()
        window.close()


def TodaysOutfitScreen():
    layout = [[sg.Text("Your outfit for today is:", pad = (0,30))], [sg.Text("RandomTop")], [sg.Text("RandomBottoms")], 
              [sg.Text("RandomOuter")], [sg.Button("Get a different outfit!", pad = (0,30)), sg.Push(), 
                                         sg.Button("Back to main menu")]]

    window = sg.Window("ChromaCloset Outfit Generator", layout, element_justification = 'c', font = "Cambria", 
                       icon = "shirtIcon.ico")

    while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Get a different outfit!":
                window.close()
                TodaysOutfitScreen()
                window.close()
            else:
                window.close()
                StartMenu()
                window.close()
            window.close()


def AddClothesScreen():
    layout = [[sg.Image("gradientLogo.png", subsample = 8), 
               sg.Text("Tip: Use a label you will be able to identify your item with!", font = ("Cambria", 12, "italic"))], 
              [sg.Text("Label"), sg.Input()], [sg.Text("Type"), sg.Combo(["Short Sleeve Top", "Long Sleeve Top", "Tank Top", 
                                                                 "Sweater", "Hoodie", "Zip-Up Jacket", "Coat", "Cardigan", 
                                                                 "Short Sleeve Dress", "Long Sleeve Dress", 
                                                                 "Jumpsuit", "Jeans", "Dress Pants", "Leggings", 
                                                                 "Sweatpants", "Short Shorts", "Mid Length Shorts",
                                                                 "Knee Length Shorts", "Miniskirt", "Knee Length Skirt", 
                                                                 "Maxi Skirt"])],
    [sg.Text("Color"), sg.Combo(["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Brown", "Gray", "Beige", 
                                 "Black", "White"])], [sg.Text("Tone"), sg.Radio('Light', group_id = 1, default = True), 
                                                       sg.Radio('Dark', group_id = 1)], [sg.Button("Back to main menu")]]
    
    window = sg.Window("ChromaCloset Outfit Generator", layout, font = ("Cambria"), icon = "shirtIcon.ico")

    while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            else:
                window.close()
                StartMenu()
                window.close()
            window.close()


def ChangeLocScreen():
    layout = [[sg.Text("Please enter your ZIP code:"), sg.Input()], [sg.Button("Back to main menu"), sg.Push(), sg.Button("Enter")]]

    window = sg.Window("ChromaCloset Outfit Generator", layout, font = ("Cambria"), icon = "shirtIcon.ico")
    
    while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Back to main menu":
                window.close()
                StartMenu()
                window.close()
            else:
                sg.popup_ok("Success! Your ZIP code has been changed to " + values[0] + ".", title = "ChromaCloset Outfit Generator", font = ("Cambria"), icon = "shirtIcon.ico")
                window.close()
                StartMenu()
            window.close()


def CreditsScreen():
    layout = [[sg.Text("Credits", font = ("Cambria", 16, "bold"))], [sg.Text("Code and GUI: Alison Mueller")], 
              [sg.Text("Branding, graphics, research, CSV file: Ellora Majumdar")], 
              [sg.Text("Made exclusively for &hacks 10.", pad = (0,20))], [sg.Button("Back to main menu")]]
    
    window = sg.Window("ChromaCloset Outfit Generator", layout, element_justification = 'c', font = "Cambria", 
                       icon = "shirtIcon.ico")

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        else:
            window.close()
            StartMenu()
            window.close()
        window.close()


StartMenu()