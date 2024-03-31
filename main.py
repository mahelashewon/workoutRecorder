import tkinter
from tkinter import ttk
import mysql.connector

import sv_ttk



root = tkinter.Tk()
root.geometry("450x800")


connection = mysql.connector.connect(host='localhost', user='root', password = '', port='3306', database='workout')
c = connection.cursor()
    


burpeesLabel = ttk.Label(root, text = 'Burpees Count: ')
burpeesLabel.grid(row=1, column=0 , padx= 10, pady=10)
burpeesEntry = ttk.Entry(root, width = 30)
burpeesEntry.grid(row=1, column=1, padx=10, pady=10)


pushUpsLabel = ttk.Label(root, text= 'Pushups Count: ')
pushUpsLabel.grid(row=2, column=0, padx= 10, pady = 10)
pushUpsEntry = ttk.Entry(root, width=30)
pushUpsEntry.grid(row=2, column=1, padx=10, pady=10)

bicepCurlLabel = ttk.Label(root, text='Bicep Curl: ')
bicepCurlLabel.grid(row=3, column=0, padx=10, pady=10)
bicepCurlEntry = ttk.Entry(root, width=30)
bicepCurlEntry.grid(row=3, column=1, padx= 10, pady=10)

pullUpBarsLabel = ttk.Label(root, text='Pull Up Bar: ')
pullUpBarsLabel.grid(row=4, column=0, padx= 10, pady=10)
pullUpBarsEntry = ttk.Entry(root, width=30)
pullUpBarsEntry.grid(row=4, column=1, padx=10, pady=10)

frontRaisesLabel = ttk.Label(root, text='Front Raises: ')
frontRaisesLabel.grid(row=5, column=0, padx=10, pady=10)
frontRaisesEntry = ttk.Entry(root, width=30)
frontRaisesEntry.grid(row=5, column=1, padx=10, pady=10)

inclinedPushUpsLabel = ttk.Label(root, text='Inclined Pushups: ')
inclinedPushUpsLabel.grid(row=6, column=0, padx=10, pady=10)
inclinedPushUpsEntry = ttk.Entry(root, width=30)
inclinedPushUpsEntry.grid(row=6, column=1, padx=10, pady=10)

declinedPushUpsLabel = ttk.Label(root, text='Declined Pushups: ')
declinedPushUpsLabel.grid(row=7, column=0, padx=10, pady=10)
declinedPushUpsEntry = ttk.Entry(root, width=30)
declinedPushUpsEntry.grid(row=7, column=1, padx=10, pady=10)

CurlLabel = ttk.Label(root, text="Curl: ")
CurlLabel.grid(row=8, column=0, padx=10, pady=10)
CurlEntry = ttk.Entry(root, width=30)
CurlEntry.grid(row=8, column=1, padx=10, pady=10)

LateralRaisesLabel = ttk.Label(root,text="Lateral Raises: ")
LateralRaisesLabel.grid(row=9, column=0, padx=10, pady=10)
LateralRaisesEntry = ttk.Entry(root, width=30)
LateralRaisesEntry.grid(row=9, column=1, padx=10, pady=10)

HammerCurlLabel = ttk.Label(root, text="Hammer Curl: ")
HammerCurlLabel.grid(row=10, column=0, padx=10, pady=10)
HammerCurlEntry = ttk.Entry(root, width=30)
HammerCurlEntry.grid(row=10, column=1, padx=10, pady=10)

ShoulderPressLabel = ttk.Label(root, text="Shoulder Press: ")
ShoulderPressLabel.grid(row=11, column=0, padx=10, pady=10)
ShoulderPressEntry = ttk.Entry(root, width=30)
ShoulderPressEntry.grid(row=11, column=1, padx=10, pady=10)

ConcentrationCurlLabel = ttk.Label(root, text="Concentration Curl: ")
ConcentrationCurlLabel.grid(row=12, column=0, padx=10, pady=10)
ConcentrationCurlEntry = ttk.Entry(root, width=30)
ConcentrationCurlEntry.grid(row=12, column=1, padx=10, pady=10)


def submitData():

    burpees = burpeesEntry.get()
    pushups = pushUpsEntry.get()
    bicepcurl = bicepCurlEntry.get()
    pullUpBars = pullUpBarsEntry.get()
    frontRaises = frontRaisesEntry.get()
    inclinedPushUps = inclinedPushUpsEntry.get()
    declinedPushUps = declinedPushUpsEntry.get()
    Curl = CurlEntry.get()
    LateralRaises = LateralRaisesEntry.get()
    HammerCurl = HammerCurlEntry.get()
    ShoulderPress = ShoulderPressEntry.get()
    ConcentrationCurl = ConcentrationCurlEntry.get()

    insertInto = "INSERT INTO `upperbody`(`Burpees`, `Pushups`, `Bicep Curl`, `Pull Up Bars`, `Front Raises`, `Incline Pushups`, `Decline Pushups`, `Curl`, `Lateral Raises`, `Hammer Curl`, `Shoulder Press`, `Concentration Curl`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    vals = (burpees, pushups, bicepcurl, pullUpBars, frontRaises, inclinedPushUps, declinedPushUps, Curl, LateralRaises, HammerCurl, ShoulderPress, ConcentrationCurl)
    c.execute(insertInto, vals)
    connection.commit()

    connection.close()




    



submit_button = ttk.Button(root,text = "Submit", command=submitData)
submit_button.grid(row=13, column=1, padx=10, pady=10)

sv_ttk.set_theme("dark")

root.mainloop()




