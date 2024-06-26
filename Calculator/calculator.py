from tkinter import *
from math import *
import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox
import re


def plot_graph(y_function, x_min=-100, x_max=100, body_1cm=100, skip=False):
    body = (abs(x_min) + abs(x_max) * body_1cm)
    x = np.linspace(x_min, x_max, body)
    y = []

    for val in x:
        try:
            y_value = zaklady_pocitania(y_function.replace('x', f'({val})'))

            if skip and abs(y_value) > 50:
                y.append(np.nan)
            else:
                y.append(y_value)
        except Exception:
            y.append(np.nan)

    y = np.array(y)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f"y = {y_function}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.ylim(-10, 10)
    plt.xlim(-10, 10)
    plt.legend()
    plt.show()
    for top in his_top:
        top.destroy()
    with open("historia.txt", "a",encoding='utf-8') as file:
        try:
            file.write(y_function + "\n")
            file.write(f"graf : {y_function}" + "\n")
        except Exception:
            y_function = filter_2(y_function, "str")
            file.write(y_function + "\n")
            file.write(f"graf : {y_function}" + "\n")


def graf_prenos():
    try:
        y_function = y_equals.get()  #
        skip = skip_b.get()
        x_min = int(sb_min.get())
        x_max = int(sb_max.get())
        body_1cm = int(pocet_bodov_sb.get())
        plot_graph(y_function, x_min, x_max, body_1cm, skip=skip)
    except Exception:
        pass


def graf_root():
    global y_equals, skip_b, sb_min, sb_max, pocet_bodov_sb
    top = Toplevel(root)
    top.title("Grafer")
    top.configure(bg="#282c34")
    top.geometry("+%d+%d" % (1000, 20))

    y_equals = Entry(top, font="Arial 25", width=14, borderwidth=5, relief="flat", justify="right", bg="#abb2bf",
                     fg="#282c34")
    y_equals.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

    Label(top, text="x_min:", font=('Arial', 20), bg="#282c34", fg="white").grid(row=1, column=0, padx=5, pady=5,
                                                                                 sticky="w")

    sb_min = Spinbox(top, from_=-1000, to=1000, font=('Arial', 20), width=3, justify="center")
    sb_min.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
    sb_min.delete(0, END)
    sb_min.insert(0, "-10")

    Label(top, text="x_max:", font=('Arial', 20), bg="#282c34", fg="white").grid(row=2, column=0, padx=5, pady=5,
                                                                                 sticky="w")

    sb_max = Spinbox(top, from_=-1000, to=1000, font=('Arial', 20), width=3, justify="center")
    sb_max.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
    sb_max.delete(0, END)
    sb_max.insert(0, "10")

    Label(top, text="Body v 1cm:", font=('Arial', 20), bg="#282c34", fg="white").grid(row=3, column=0, padx=5, pady=5,
                                                                                      sticky="w")

    pocet_bodov_sb = Spinbox(top, from_=-10000, to=10000, font=('Arial', 20), width=3, justify="center")
    pocet_bodov_sb.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
    pocet_bodov_sb.delete(0, END)
    pocet_bodov_sb.insert(0, "100")

    skip_b = BooleanVar()
    skip_check = Checkbutton(top, text="preskoč velke hodnoty ", variable=skip_b, font="Arial 15", bg="#282c34",
                             fg="#61afef", selectcolor="#282c34")
    skip_check.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

    btn = Button(top, text="Graf", font=('Arial', 20), bg="#61afef", fg="white", bd=0, relief="raised",
                 command=graf_prenos)
    btn.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

    top.grid_columnconfigure(0, weight=1)
    top.grid_columnconfigure(1, weight=1)


def cot(x):
    return 1 / tan(x)


def sec(x):
    return 1 / cos(x)


def csc(x):
    return 1 / sin(x)


def convert(value):
    try:
        return float(value)
    except ValueError:
        try:
            return complex(value)
        except ValueError:
            raise ValueError(f"nemožem premeniť '{value}' ani na float ani na complexne čislo .")


def spocitaj(x, y):
    return x + y


def nasob(x, y):
    return x * y


def deg(x):
    return x * 180 / pi


def rad(x):
    return x * pi / 180


def faktorial(n):

    if n <= 0:
        return 1
    else:
        return n * faktorial(n - 1)



def vydel(x, y):
    if y != 0:
        return x / y
    else:
        return ZeroDivisionError("Nuh uh , nemôžeš deliť nulov ")


def mocnina(x, y):
    return x ** y


def odmocnenie(x, y):
    return y ** (1 / x)


def ln(x):
    return log(x)
def exp10(x):
    return 10**x

def logaritmus(x, y):
    return log(y, x)


def value_insert(value):
    pozicia = entry.index(INSERT)
    entry.insert(pozicia, value)
    if value in funkcie.keys():
        value_insert("(")


def dozadu():
    entry.delete(entry.index("end") - 1)


def clear():
    global postup
    postup = []
    entry.delete(0, END)


def start():
    global postup_bool, postup
    try:
        postup = []
        priklad = entry.get()
        postup.append(priklad)
        decimals = int(spinbox.get())
        try:
            result = str(round(zaklady_pocitania(priklad), decimals))
        except Exception:
            result = np.array(zaklady_pocitania(priklad))
            real_part = round(float(result.real) , decimals)
            imaginary_part = round(float(result.imag) , decimals)
            if real_part == 0 and imaginary_part == 0 :
                result = 0
            elif real_part == 0  :
                result = str(imaginary_part) + "j"
            elif imaginary_part == 0:
                result = str(real_part)
            else :
                result = f"{str(real_part)} + {str(imaginary_part)}j "
        result = re.sub(r'e', '* exp', str(result))

        try:
            if result[0] == "-" and result[1] == "0":
                result = result[1:]
        except Exception:
            pass
        for top in his_top:
            top.destroy()
        with open("historia.txt", "a",encoding='utf-8') as file:
            try:
                file.write(str(priklad) + "\n")
                file.write(str(result) + "\n")
            except Exception:
                priklad = filter_2(priklad, "str")
                file.write(str(priklad) + "\n")
                file.write(str(result) + "\n")

        if postup_bool:
            postup.append(result)
            postup_root()
        clear()
        entry.insert(END, result)
    except Exception as e:
        messagebox.showerror("Error", f"{e}")


def formatovanie_zatvorky(casti):
    od = 0
    skip = 0
    pozicia = 0
    while pozicia < len(casti):
        if casti[pozicia] == "(":
            if skip == 0:
                od = pozicia
            skip += 1
        if casti[pozicia] == ")":
            if skip == 1:
                do = pozicia
                stred = pocitaj(casti[od + 1:do])
                casti = casti[:od] + [str(stred)] + casti[do + 1:]
                pozicia = -1
            skip -= 1
        pozicia += 1
    return casti


def pocitaj(casti):
    global postup

    casti = formatovanie_zatvorky(casti)
    casti = plus_minus(casti)
    casti = mazanie_znakov(casti)

    for funckcia in funkcie.keys():
        while funckcia in casti:
            postup.append(casti)
            znak = casti.index(funckcia)

            x = convert(casti[znak + 1])

            result = funkcie[funckcia](x)
            casti = casti[:znak] + [str(result)] + casti[znak + 2:]
    j = 0
    while j < len(one):
        i = 1
        while i < len(casti) - 1:
            znak = casti[i]
            if znak in one[j]:
                postup.append(casti)
                x = convert(casti[i - 1])
                y = convert(casti[i + 1])
                result = znaky[znak](x, y)
                casti = casti[:i - 1] + [str(result)] + casti[i + 2:]
            else:
                i += 2
        j += 1
    if len(casti) == 1:
        return casti[0]
    return SyntaxError("je problem v priklade , možno si tam omilom vložil nepočitatelne znaky alebo pismena ")


def filter_2(priklad, mode="list"):
    pred = sorted(premena.keys(), key=len, reverse=True)
    pattern = re.compile(r'(' + '|'.join(re.escape(key) for key in pred) + r'|[()]|\d+\.\d+|\d+|j)')

    def replacer(match):
        znak = match.group(0)
        if znak in premena:
            return " " + premena[znak] + " "
        elif znak.isdigit() or znak == 'j':
            return " " + znak + " "
        return znak

    priklad = pattern.sub(replacer, priklad)
    priklad = re.sub(r'(\d|j)\s+(\d|j)', r'\1 * \2', priklad)

    if mode == "str":
        return priklad
    casti = priklad.lower().split()
    return casti


def plus_minus(casti):
    index = 0
    while index < len(casti) - 1:
        if casti[index] == '-' and casti[index + 1] == '+':
            del casti[index + 1]
        elif casti[index] == '+' and casti[index + 1] == '-':
            del casti[index]
        elif casti[index] == '+' and casti[index + 1] == '+':
            del casti[index]
        elif casti[index] == '-' and casti[index + 1] == '-':
            casti[index] = "+"
            del casti[index + 1]
        elif casti[index] == '-' and casti[index + 1] not in znaky_vsetky:
            if casti[index - 1] in list(znaky.keys()) + ["("]:
                if float(casti[index + 1]) > 0:
                    del casti[index]
                    casti[index] = float(casti[index]) * -1
                elif casti[index + 1] < 0:
                    casti[index] = "+"
                    del casti[index + 1][0]
            else:
                casti[index] = "+"
                casti[index + 1] = float(casti[index + 1]) * -1
            index += 1
        else:
            index += 1
    return casti


def mazanie_znakov(casti):
    dalej = True
    while dalej:
        if casti[0] in list(znaky.keys()) + [")", "."]:
            del casti[0]
        else:
            dalej = False
    return casti


def pravidla():
    prav = (
        "Pravidlá:\n"
        "+ = sčítanie (napr. 5 + 2 = 7)\n"
        "- = odčítanie (napr. 5 - 2 = 3)\n"
        "* = násobenie (napr. 5 * 2 = 10)\n"
        "/ = delenie (napr. 5 / 2 = 2.5)\n"
        "** = mocnina (napr. 5 ** 2 = 25)\n"
        "√ = odmocnina (napr. 3 √ 8 = 2)\n"
        "log = logaritmus s lubovolným base  , (base)log(x) , 2log8 = 3 \n"  # 2**3 = 8, j log -1 = 2
        "( ) = zátvorky pre zoskupenie operácií\n"
        "sin(x) = sinus uhla x (v rad)\n"
        "cos(x) = kosinus uhla x (v rad)\n"
        "tan(x) = tangens uhla x (v rad)\n"
        "cot(x) = cotangens uhla x (v rad)\n"
        "sec(x) = secant uhla x (v rad)\n"
        "csc(x) = cosecant uhla x (v rad)\n"
        "ln(x) = prirodzený logaritmus čísla x , base je e\n"
        "log10(x) = dekadický logaritmus čísla x , base je 10\n"
        "rad(x) = premení deg na rad (x*pi/180)\n"
        "deg(x) = premení rad na deg (x*180/pi)\n"
        "abs(x) = absolutna hodnota aka |-5| = 5 (nepouživať || , iba abs)\n"
        "floor (x) =  zaokruhlenie na zem\n"
        "exp(x)= 10**x ,exp(2) = 100 \n"
        "!(x) = faktorial čisla x ,( x musi biť pozitivny integer aka cele čislo, abs(floor(x)) )\n"
        "π = hodnota matematickej konštanty Pi , funguje aj ked napišeš pi\n"
        "e = hodnota matematickej konštanty e\n"
        "j = hodota ktora je vyjadrená rovnicou j**2 = -1 , je to imaginare \n"
        "dm = desatine miesta , dm = 2 π = 3.14 , dm = 3 π = 3.142n\n"
        "graf = Vo Graf_makery (grafery) moužete použivať X (Škálu x si môžte\n"
        "definovať od kadial do kadial)\n"
    )
    top = Toplevel(root)
    top.title("Pravidlá")
    top.configure(bg="#282c34")
    top.geometry("+%d+%d" % (425, 20))
    lbl = Label(top, text=prav, font=('Arial', 12), bg="#282c34", fg="white", justify="left")
    lbl.pack(pady=10, padx=10)


def zaklady_pocitania(priklad):
    global postup
    try:
        priklad = priklad.lower()
        postup = []
        casti = filter_2(priklad)

        result = convert(pocitaj(casti))
        return result
    except ZeroDivisionError as e:
        return(f"nemôžeš deliť nulou : {e}")
    except IndexError as e:
        return(f"Dával si znaky bez hodnôt , asi : {e}")


def toggle_postup():
    global postup_bool
    postup_bool = not postup_bool


def postup_root():
    global postup
    i = 0
    top = Toplevel(root)
    top.title("postup")
    top.configure(bg="#282c34")
    for step in postup:
        Label(top, text=f"{i}. step: {step}", font=('Arial', 12), bg="#282c34", fg="white", anchor="w",
              justify="left").pack(pady=2, fill="x")
        i += 1
    postup = []


def history_root():
    global his_top, page
    try:
        with open("historia.txt", "r",encoding='utf-8') as file:
            historia = [line.rstrip() for line in file]
    except FileNotFoundError:
        historia = []

    his_top.append(Toplevel(root))
    his_top[-1].title("historia")
    his_top[-1].configure(bg="#282c34")
    his_top[-1].geometry("+%d+%d" % (475, 20))


    max_entires = 32
    total_pages = (len(historia) + max_entires - 1) // max_entires
    label_page = Label(his_top[-1], text=f"Page {page + 1}/{total_pages}", font=('Arial', 10), bg="#282c34", fg="white")
    label_page.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

    def show_entries():
        global page
        for widget in his_top[-1].grid_slaves():
            if int(widget.grid_info()["row"]) > 0:
                widget.grid_forget()

        start_index = page * max_entires
        end_index = start_index + max_entires
        page_entries = historia[start_index:end_index]

        row_val = 1
        col_val = 0
        for priklad in page_entries:
            if col_val == 1:
                lb = Label(his_top[-1], text="=", font=('Arial', 12), bg="#282c34", fg="white", anchor="w",
                           justify="left")
                lb.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
                col_val = 2
            entry = Entry(his_top[-1])
            entry.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
            entry.insert(END, priklad)
            if col_val > 1:
                col_val = 0
                row_val += 1
            else:
                col_val = 1

        label_page.config(text=f"Page {page + 1}/{total_pages}")

    # Navigation buttons
    def prev_page():
        global page
        if page > 0:
            page -= 1
            show_entries()

    def next_page():
        global page
        if page < total_pages - 1:
            page += 1
            show_entries()

    def clear_history():
        try:
            with open("historia.txt", "w",encoding='utf-8') as file:
                file.write("")
            for top in his_top:
                top.destroy()
            history_root()
        except Exception:
            pass

    btn_prev = Button(his_top[-1], text="<", command=prev_page, font=('Arial', 10), bg="#61afef", fg="white", bd=0,
                      relief="raised")
    btn_prev.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    btn_next = Button(his_top[-1], text=">", command=next_page, font=('Arial', 10), bg="#61afef", fg="white", bd=0,
                      relief="raised")
    btn_next.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

    Button(his_top[-1], text="vymaž historiu ;)", command=clear_history, font=('Arial', 10), bg="#e06c75", fg="white",
           bd=0, relief="raised").grid(row=0, column=3, padx=5, pady=5, sticky="nsew")

    show_entries()

    his_top[-1].grid_columnconfigure(0, weight=1)
    his_top[-1].grid_columnconfigure(2, weight=1)


if __name__ == '__main__':
    page = 0
    his_top = []
    root = Tk()
    root.title("Calculator")
    root.configure(bg="#282c34")
    root.geometry("+%d+%d" % (0, 20))
    entry = Entry(root, font="Arial 25", width=14, borderwidth=5, relief="flat", justify="right", bg="#abb2bf",
                  fg="#282c34")
    entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")
    postup = []

    znaky_vsetky = ["+", "**", "-", "*", "/", "root", "(", ")", "sin", "tan", "cos", "cot", "log10", "ln", "sec", "csc",
                    "rad", "deg", "abs", "!", "exp","floor","ceil","log"]

    premena = {
        "ceil": "ceil",
        "abs": "abs",
        "round": "round",
        "!": "!",
        'sin': 'sin',
        'cos': 'cos',
        'tan': 'tan',
        'cot': 'cot',
        'log10': 'log10',
        'ln': 'ln',
        'sec': 'sec',
        'csc': 'csc',
        'rad': 'rad',
        'deg': 'deg',
        '+': '+',
        '**': '**',
        '-': '-',
        '*': '*',
        '/': '/',
        '√': 'root',
        "log": "log",
        "root": 'root',
        '(': '(',
        ')': ')',
        'π': str(pi),
        'e': str(e),
        "exp":"exp",
        'pi': str(pi),
        "i": "j",
        "floor": "floor"
    }

    znaky = {"+": spocitaj, "*": nasob, "/": vydel, "**": mocnina, "root": odmocnenie, "log": logaritmus}
    one = [["**", "root", "log"], ["*", "/"], ["+"]]

    funkcie = {"sin": sin, "cos": cos, "tan": tan, "cot": cot,
               "ln": log, "log10": log10,
               "sec": sec, "csc": csc,
               "rad": rad, "deg": deg,
               "abs": abs, "!": faktorial,
               "floor": floor, "ceil": ceil,
               "round": round , "exp":exp10
               }

    buttons = [
        'C', '(', ')', '⌫', 'sin',
        'cos', 'tan', 'cot', 'sec', 'csc',
        'log10', 'ln', "abs", "rad", "deg",
        "!", "floor", "log", "π", "e",
        '7', '8', '9', '**', '√',
        '4', '5', '6', '*', '/',
        '1', '2', '3', "+", '-',
        'ceil', '0', '.', '=', 'round',
        "j","exp", "pra", "gra", "hist"
    ]

    row_val = 1
    col_val = 0
    for button in buttons:
        if button == "=":
            btn = Button(root, text=button, font=('Arial', 20), command=start, bg="#61afef", fg="white", bd=0,
                         relief="raised")
        elif button == 'C':
            btn = Button(root, text=button, font=('Arial', 20), command=clear, bg="#e06c75", fg="white", bd=0,
                         relief="raised")
        elif button == "⌫":
            btn = Button(root, text=button, font=('Arial', 20), command=dozadu, bg="#e06c75", fg="white", bd=0,
                         relief="raised")
        elif button == "pra":
            btn = Button(root, text=button, font=('Arial', 20), command=pravidla, bg="#e06c75", fg="white", bd=0,
                         relief="raised")
        elif button == "gra":
            btn = Button(root, text=button, font=('Arial', 20), command=graf_root, bg="#e06c75", fg="white", bd=0,
                         relief="raised")
        elif button == "hist":
            btn = Button(root, text=button, font=('Arial', 20), command=history_root, bg="#e06c75", fg="white", bd=0,
                         relief="raised")
        else:
            btn = Button(root, text=button, font=('Arial', 20), command=lambda b=button: value_insert(b), bg="#98c379",
                         fg="white", bd=0, relief="raised")
        btn.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
        col_val += 1
        if col_val > 4:
            col_val = 0
            row_val += 1

    root.grid_rowconfigure(0, weight=1)
    for i in range(1, row_val + 1):
        root.grid_rowconfigure(i, weight=1)
    for j in range(5):
        root.grid_columnconfigure(j, weight=1)

    postup_bool = True
    checkvar = IntVar(value=1)
    chk_postup_bool = Checkbutton(root, text="postup", font=('Arial', 20), command=toggle_postup, bg="#282c34",
                                  fg="white", selectcolor="#61afef", variable=checkvar)
    chk_postup_bool.grid(row=row_val + 1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    Label(root, text="Dm:", font=('Arial', 20), bg="#282c34", fg="white").grid(row=row_val + 1, column=2, padx=5,
                                                                               pady=5, sticky="nsew")

    spinbox = Spinbox(root, from_=0, to=20, font=('Arial', 20), width=3, justify="center")
    spinbox.grid(row=row_val + 1, column=3, padx=5, pady=5, sticky="nsew")
    spinbox.delete(0, END)
    spinbox.insert(0, "2")

    pravidla()
    graf_root()
    root.mainloop()
