import csv
import random
import PySimpleGUI as sg
import Matches

sg.theme('Light Green 4')

def StartMenu():
    layout = [[sg.Image("gradientLogo.png", subsample = 2, pad = (0,20))], [sg.Button("Today's outfit", size=(15, 1))], 
              [sg.Button("Add clothes", size=(15, 1))], 
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
        window.close()


def TodaysOutfitScreen():

    temp = sg.popup_yes_no("Is it 70 degrees Fahrenheit or warmer today?", title = "ChromaCloset Outfit Generator", font = "Cambria", 
                        icon = "shirtIcon.ico")
    
    # Outfit generation
    if temp == "Yes":
        randomRowO = [""]
        while True:
            with open("AllClothing.csv") as csvfile:
                reader = csv.reader(csvfile)

                randomT = random.choice(Matches.warmT)
                randomRowT = random.choice(list(reader))
                
                if randomT == randomRowT[1]:
                    with open("AllClothing.csv") as csvfile:
                        reader = csv.reader(csvfile)
                        
                        randomB = random.choice(Matches.warmB)
                        randomRowB = random.choice(list(reader))

                        if randomB == randomRowB[1]:
                            colorVar1 = randomRowT[2] + ", " + randomRowB[2]
                            colorVar2 = randomRowB[2] + ", " + randomRowT[2]

                            if colorVar1 in Matches.colorCombos or colorVar2 in Matches.colorCombos:
                                break
    
    else:
        while True:
            with open("AllClothing.csv") as csvfile:
                reader = csv.reader(csvfile)

                randomT = random.choice(Matches.coldT)
                randomRowT = random.choice(list(reader))
                
                if randomT == randomRowT[1]:
                    with open("AllClothing.csv") as csvfile:
                        reader = csv.reader(csvfile)
                        
                        randomB = random.choice(Matches.coldB)
                        randomRowB = random.choice(list(reader))

                        if randomB == randomRowB[1]:
                            with open("AllClothing.csv") as csvfile:
                                reader = csv.reader(csvfile)
                            
                                randomO = random.choice(Matches.outerwear)
                                randomRowO = random.choice(list(reader))

                                if randomO == randomRowO[1]:
                                    colorVar1 = randomRowT[2] + ", " + randomRowB[2]
                                    colorVar2 = randomRowB[2] + ", " + randomRowT[2]

                                    if colorVar1 in Matches.colorCombos or colorVar2 in Matches.colorCombos:
                                        colorVarExtra1 = randomRowT[2] + ", " + randomRowO[2]
                                        colorVarExtra2 = randomRowB[2] + ", " + randomRowO[2]
                                        colorVarExtra3 = randomRowO[2] + ", " + randomRowT[2]
                                        colorVarExtra4 = randomRowO[2] + ", " + randomRowB[2]

                                        if colorVarExtra1 in Matches.colorCombos or colorVarExtra2 in Matches.colorCombos or colorVarExtra3 in Matches.colorCombos or colorVarExtra4 in Matches.colorCombos:
                                            break


    # End outfit generation
    
    layout = [[sg.Text("Your outfit for today is:", pad = (0,30))], [sg.Text(randomRowT[0])], [sg.Text(randomRowB[0])], 
              [sg.Text(randomRowO[0])], [sg.Button("Get a different outfit!", pad = (0,30)), sg.Push(), 
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
              [sg.Text("Label"), sg.Input(key = '-LABEL-')], [sg.Text("Type"), sg.Combo(["Short Sleeve Top", "Long Sleeve Top", "Tank Top", 
                                                                 "Sweater", "Hoodie", "Zip-Up Jacket", "Coat", "Cardigan", 
                                                                 "Jeans", "Dress Pants", "Leggings", 
                                                                 "Sweatpants", "Short Shorts", "Mid Length Shorts",
                                                                 "Knee Length Shorts", "Miniskirt", "Knee Length Skirt", 
                                                                 "Maxi Skirt"])],
    [sg.Text("Color"), sg.Combo(["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Brown", "Gray", "Beige", 
                                 "Black", "White"])], [sg.Text("Tone"), sg.Radio('Light', group_id = 1, default = True), 
                                                       sg.Radio('Dark', group_id = 1)], [sg.Button("Back to main menu"), 
                                                                                         sg.Push(), sg.Button("Submit")]]
    
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
                itemData = [values['-LABEL-'], values[1], str(values[3])+values[2]]
                with open("AllClothing.csv", 'a') as csvfile:
                    writer = csv.writer(csvfile, lineterminator = '\n')
                    writer.writerow(itemData)
                    window.close()
                    AddClothesScreen()
                    window.close()
            window.close()


def CreditsScreen():
    layout = [[sg.Text("Credits", font = ("Cambria", 16, "bold"))], [sg.Text("Code and GUI: Alison Mueller")], 
              [sg.Text("Branding, graphics, research, CSV file: Ellora Majumdar")], 
              [sg.Text("Made for &hacks 10.", pad = (0,20))], [sg.Button("Back to main menu")]]
    
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