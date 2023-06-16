import joblib
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import font

model = joblib.load("seg")  # initialize model variable

def load_model():
    global model
    filepath = filedialog.askopenfilename()  # open file dialog to select the file
    model = joblib.load("seg")  # load the selected model file
    print("Model loaded successfully!")

def customer_segmentation(Gender, Ever_Married, Age, Graduated, Profession, Work_Experience, Spending_score, Family_size, Var_1):
    y_pred = model.predict([[Gender, Ever_Married, Age, Graduated, Profession, Work_Experience, Spending_score, Family_size, Var_1]])
    if y_pred == 0:
        return "A : The automobiles which is suitable is BIKE."
    elif y_pred == 1:
        return "B : The automobile which is suitable is CAR."
    elif y_pred == 2:
        return "C : The automobile which is suitable is MINI VAN."
    else:
        return "D : The automobile which is suitable is MINI BUS."

# Create the Tkinter window and widgets
window = tk.Tk()
window.title("Customer segmentation for automobile")

#  creating title to the window
window.geometry("400x400")
window.configure(bg='lavender')
window.geometry("400x300")
window.resizable(True, True)


img = ImageTk.PhotoImage(Image.open("147.png"))
bg_label = tk.Label(window, image=img)
bg_label.place(x= 0, y= 0, relwidth= 1, relheight=1)

label_gender = tk.Label(window, text="Gender\n Male - 1 \n Female - 0\n")
label_gender.grid(row=1, column=0, padx=10, pady=10)
entry_gender = tk.Entry(window)
entry_gender.grid(row=1, column=1, padx=10, pady=10)

label_married = tk.Label(window, text="Ever Married\n Yes - 1\n No - 0\n")
label_married.grid(row=2, column=0, padx=10, pady=10)
entry_married = tk.Entry(window)
entry_married.grid(row=2, column=1, padx=10, pady=10)

label_age = tk.Label(window, text="Age")
label_age.grid(row=3, column=0, padx=10, pady=10)
entry_age = tk.Entry(window)
entry_age.grid(row=3, column=1, padx=10, pady=10)

label_graduated = tk.Label(window, text="Graduated\n Yes - 1\n No - 0\n")
label_graduated.grid(row=4, column=0, padx=10, pady=10)
entry_graduated = tk.Entry(window)
entry_graduated.grid(row=4, column=1, padx=10, pady=10)

label_profession = tk.Label(window, text="Profession\n  Artist-0\n Doctor-1\n   Engineer-2\n Entertainment-3\n Executive-4\n Healthcare-5\n  Lawyer-7\n Marketing-8\n Homemaker-9\n")
label_profession.grid(row=5, column=0, padx=10, pady=10)
entry_profession = tk.Entry(window)
entry_profession.grid(row=5, column=1, padx=10, pady=10)

label_experience = tk.Label(window, text="Work Experience")
label_experience.grid(row=6, column=0, padx=10, pady=10)
entry_experience = tk.Entry(window)
entry_experience.grid(row=6, column=1, padx=10, pady=10)

label_spending = tk.Label(window, text="Spending Score\n "
                                       "Low - 2\n Average - 1\n High - 0\n")
label_spending.grid(row=7, column=0, padx=10, pady=10)
entry_spending = tk.Entry(window)
entry_spending.grid(row=7, column=1, padx=10, pady=10)


label_family = tk.Label(window, text="Family Size")
label_family.grid(row=8, column=0, padx=10, pady=10)
entry_family = tk.Entry(window)
entry_family.grid(row=8, column=1, padx=10, pady=10)

label_var = tk.Label(window, text="Category")
label_var.grid(row=9, column=0, padx=10, pady=10)
entry_var = tk.Entry(window)
entry_var.grid(row=9, column=1, padx=10, pady=10)

def predict_segmentation():
    gender = (entry_gender.get())
    married = (entry_married.get())
    age = int(entry_age.get())
    graduated = (entry_graduated.get())
    profession = (entry_profession.get())
    experience = int(entry_experience.get())
    spending = (entry_spending.get())
    family = int(entry_family.get())
    var = (entry_var.get())

    prediction = customer_segmentation(gender, married, age, graduated, profession, experience, spending, family, var)
    output_label.config(text=prediction)

button = tk.Button(window, text="Predict", command = predict_segmentation)
button.grid(row=10, column=1)

output_label = tk.Label(window, text="")
output_label.grid(row=11, column=0)

font_style = font.Font(size=10)
output_label.config(font=font_style)

window.mainloop()
