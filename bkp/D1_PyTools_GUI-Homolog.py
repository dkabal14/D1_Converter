import tkinter as tk
from tkinter import messagebox, filedialog
import tkinter.ttk as ttk
from tkinter.constants import END
import os
import subprocess


HB_TO_PY = 1
HB_TO_IPYNB = 2
IPYNB_TO_HB = 3
DEBUG_MODE = False
root_dir = os.path.dirname(os.path.abspath(__file__))
default_title = "Quality Digital - Ferramentas de Conversão para o Diligent One - Versão de Homologação"

def to_path_linux(path):
    """
    Converte o caminho do arquivo para o formato Linux.
    """
    return path.replace("\\", "/")

def to_path_windows(path):
    """
    Converte o caminho do arquivo para o formato Windows.
    """
    return path.replace("/", "\\")

def choose_file_1():
    try:
        if root.rdbtn.get() == 1:
            file_type = [('Arquivo de um Robô', '*.json')]
        elif root.rdbtn.get() == 2:
            file_type = [('Arquivo de um Robô', '*.json')]
        elif root.rdbtn.get() == 3:
            file_type = [('IPython Jupyter Notebook', '*.ipynb')]
        else:
            raise Exception('É necessário escolher um tipo de conversão!')
        # TODO: Adicionar checagem se o json escolhido é de fato um arquivo válido para a conversão
        file_name = filedialog.askopenfilename(filetypes=file_type, initialdir=os.environ['USERPROFILE'], defaultextension=file_type[0][1])
        if file_name != '':
            root.Entry1.delete(0, END)
            root.Entry1.insert(0, to_path_windows(file_name))

    except Exception as e:
        messagebox.showwarning("Atenção!", f"{e}")

def choose_file_2():
    try:
        if root.rdbtn.get() == 1:
            file_type = [('Script Python', '*.py')]
        elif root.rdbtn.get() == 2:
            file_type = [('IPython Jupyter Notebook', '*.ipynb')]
        elif root.rdbtn.get() == 3:
            file_type = [('Robô Highbond', '*.json')]
        else:
            raise Exception('É necessário escolher um tipo de conversão!')
        if root.Entry1.get() != '':
            initd = os.path.dirname(root.Entry1.get())
            initf = f'{".".join(os.path.basename(root.Entry1.get()).split(".")[:-1])}'
            file_name = filedialog.asksaveasfilename(filetypes=file_type, initialdir=initd, defaultextension=file_type[0][1], initialfile=initf)
        else:
            file_name = filedialog.asksaveasfilename(filetypes=file_type, initialdir=os.environ['USERPROFILE'], defaultextension=file_type[0][1])
        # TODO: Adicionar checagem se o json escolhido é de fato um arquivo válido para a conversão
        if file_name != '':
            root.Entry2.delete(0, END)
            root.Entry2.insert(0, to_path_windows(file_name))
        
    except Exception as e:
        messagebox.showwarning("Atenção!", f"{e}")

def clear_entries():
    root.Entry1.delete(0, END)
    root.Entry2.delete(0, END)

def runMainVoid():
    try:
        i_file = to_path_linux(root.Entry1.get())
        o_file = to_path_linux(root.Entry2.get())

        if not bool(i_file) and not bool(o_file):
            raise Exception("Os arquivos de origem e destino precisam estar preenchidos!")
        elif not bool(i_file):
            raise Exception("O arquivo de origem precisa estar preenchido!")
        elif not bool(o_file):
            raise Exception("O arquivo de destino precisa estar preenchido!")
        
        if root.rdbtn.get() == 1:
            run1 = subprocess.run(['python.exe', f"{root_dir}/src/hb-json_to_py.py", i_file, o_file], capture_output=True, check=False)
            if run1.returncode != 0:
                raise Exception(f"Falha na execução com o código {run1.returncode}: {run1.stderr}")
            else:
                messagebox.showinfo(default_title, f"Arquivo {o_file} criado com sucesso!")
        elif root.rdbtn.get() == 2:
            run2 = subprocess.run(['python.exe', f"{root_dir}/src/hb-json_to_ipynb.py", i_file, o_file], capture_output=True, check=False)
            if run2.returncode != 0:
                raise Exception(default_title, f"Falha na execução com o código {run2.returncode}: {run2.stderr}")
            else:
                messagebox.showinfo(f"Arquivo {o_file} criado com sucesso!")
        elif root.rdbtn.get() == 3:
            run3 = subprocess.run(['python.exe', f"{root_dir}/src/ipynb_to_hb-json.py", i_file, o_file], capture_output=True, check=False)
            if run3.returncode != 0:
                raise Exception(f"Falha na execução com o código {run3.returncode}: {run3.stderr}")
            else:
                messagebox.showinfo(default_title, f"Arquivo {o_file} criado com sucesso!")
        else:
            raise Exception("É necessário escolher um tipo de conversão!")

    except Exception as e:
        messagebox.showwarning("Atenção", e)

root = tk.Tk()
root.protocol('WM_DELETE_WINDOW' , root.destroy)

root.geometry("602x190+307+125")
root.minsize(120, 1)
root.maxsize(1370, 749)
root.resizable(1,  1)
root.title(default_title)
root.configure(background="#d9d9d9")
root.configure(highlightbackground="#d9d9d9")
root.configure(highlightcolor="#000000")
root.iconbitmap(f"{root_dir}/img/quality.ico")

root.rdbtn = tk.IntVar()



root.Label1 = tk.Label(root)
root.Label1.place(relx=0.017, rely=0.105, height=21, width=191)
root.Label1.configure(activebackground="#d9d9d9")
root.Label1.configure(activeforeground="black")
root.Label1.configure(anchor='w')
root.Label1.configure(background="#d9d9d9")
root.Label1.configure(compound='left')
root.Label1.configure(disabledforeground="#a3a3a3")
root.Label1.configure(font="-family {Segoe UI} -size 9")
root.Label1.configure(foreground="#000000")
root.Label1.configure(highlightbackground="#d9d9d9")
root.Label1.configure(highlightcolor="#000000")
root.Label1.configure(text='''Selecione o Método de Conversão:''')

root.Entry1 = tk.Entry(root)
root.Entry1.place(relx=0.432, rely=0.211, height=20, relwidth=0.488)
root.Entry1.configure(background="white")
root.Entry1.configure(disabledforeground="#a3a3a3")
root.Entry1.configure(font="-family {Courier New} -size 10")
root.Entry1.configure(foreground="#000000")
root.Entry1.configure(highlightbackground="#d9d9d9")
root.Entry1.configure(highlightcolor="#000000")
root.Entry1.configure(insertbackground="#000000")
root.Entry1.configure(selectbackground="#d9d9d9")
root.Entry1.configure(selectforeground="black")

root.Entry2 = tk.Entry(root)
root.Entry2.place(relx=0.432, rely=0.474, height=20, relwidth=0.488)
root.Entry2.configure(background="white")
root.Entry2.configure(disabledforeground="#a3a3a3")
root.Entry2.configure(font="-family {Courier New} -size 10")
root.Entry2.configure(foreground="#000000")
root.Entry2.configure(highlightbackground="#d9d9d9")
root.Entry2.configure(highlightcolor="#000000")
root.Entry2.configure(insertbackground="#000000")
root.Entry2.configure(selectbackground="#d9d9d9")
root.Entry2.configure(selectforeground="black")

root.Button1 = tk.Button(root)
root.Button1.place(relx=0.93, rely=0.211, height=26, width=27)
root.Button1.configure(activebackground="#d9d9d9")
root.Button1.configure(activeforeground="black")
root.Button1.configure(background="#d9d9d9")
root.Button1.configure(disabledforeground="#a3a3a3")
root.Button1.configure(foreground="#000000")
root.Button1.configure(highlightbackground="#d9d9d9")
root.Button1.configure(highlightcolor="#000000")
root.Button1.configure(text='''...''')
root.Button1.configure(command=choose_file_1)

root.Button2 = tk.Button(root)
root.Button2.place(relx=0.93, rely=0.474, height=26, width=27)
root.Button2.configure(activebackground="#d9d9d9")
root.Button2.configure(activeforeground="black")
root.Button2.configure(background="#d9d9d9")
root.Button2.configure(cursor="fleur")
root.Button2.configure(disabledforeground="#a3a3a3")
root.Button2.configure(font="-family {Segoe UI} -size 9")
root.Button2.configure(foreground="#000000")
root.Button2.configure(highlightbackground="#d9d9d9")
root.Button2.configure(highlightcolor="#000000")
root.Button2.configure(text='''...''')
root.Button2.configure(command=choose_file_2)

root.Radiobutton1 = tk.Radiobutton(root)
root.Radiobutton1.place(relx=0.017, rely=0.211, relheight=0.132, relwidth=0.256)
root.Radiobutton1.configure(activebackground="#d9d9d9")
root.Radiobutton1.configure(activeforeground="black")
root.Radiobutton1.configure(anchor='w')
root.Radiobutton1.configure(background="#d9d9d9")
root.Radiobutton1.configure(compound='left')
root.Radiobutton1.configure(disabledforeground="#a3a3a3")
root.Radiobutton1.configure(font="-family {Segoe UI} -size 9")
root.Radiobutton1.configure(foreground="#000000")
root.Radiobutton1.configure(highlightbackground="#d9d9d9")
root.Radiobutton1.configure(highlightcolor="#000000")
root.Radiobutton1.configure(justify='left')
root.Radiobutton1.configure(overrelief="groove")
root.Radiobutton1.configure(text='''HB-JSON -> Python''')
root.Radiobutton1.configure(underline="-100")
root.Radiobutton1.configure(variable=root.rdbtn)
root.Radiobutton1.configure(value=HB_TO_PY)
root.Radiobutton1.configure(command=clear_entries)

root.Radiobutton2 = tk.Radiobutton(root)
root.Radiobutton2.place(relx=0.017, rely=0.368, relheight=0.132, relwidth=0.322)
root.Radiobutton2.configure(activebackground="#d9d9d9")
root.Radiobutton2.configure(activeforeground="black")
root.Radiobutton2.configure(anchor='w')
root.Radiobutton2.configure(background="#d9d9d9")
root.Radiobutton2.configure(compound='left')
root.Radiobutton2.configure(disabledforeground="#a3a3a3")
root.Radiobutton2.configure(font="-family {Segoe UI} -size 9")
root.Radiobutton2.configure(foreground="#000000")
root.Radiobutton2.configure(highlightbackground="#d9d9d9")
root.Radiobutton2.configure(highlightcolor="#000000")
root.Radiobutton2.configure(justify='left')
root.Radiobutton2.configure(overrelief="groove")
root.Radiobutton2.configure(text='''HB-JSON -> Jupyter Notebook''')
root.Radiobutton2.configure(underline="-100")
root.Radiobutton2.configure(variable=root.rdbtn)
root.Radiobutton2.configure(value=HB_TO_IPYNB)
root.Radiobutton2.configure(command=clear_entries)

root.Radiobutton3 = tk.Radiobutton(root)
root.Radiobutton3.place(relx=0.017, rely=0.526, relheight=0.132, relwidth=0.322)
root.Radiobutton3.configure(activebackground="#d9d9d9")
root.Radiobutton3.configure(activeforeground="black")
root.Radiobutton3.configure(anchor='w')
root.Radiobutton3.configure(background="#d9d9d9")
root.Radiobutton3.configure(compound='left')
root.Radiobutton3.configure(disabledforeground="#a3a3a3")
root.Radiobutton3.configure(font="-family {Segoe UI} -size 9")
root.Radiobutton3.configure(foreground="#000000")
root.Radiobutton3.configure(highlightbackground="#d9d9d9")
root.Radiobutton3.configure(highlightcolor="#000000")
root.Radiobutton3.configure(justify='left')
root.Radiobutton3.configure(overrelief="groove")
root.Radiobutton3.configure(text='''Jupyter Notebook -> HB-JSON''')
root.Radiobutton3.configure(underline="-100")
root.Radiobutton3.configure(variable=root.rdbtn)
root.Radiobutton3.configure(value=IPYNB_TO_HB)
root.Radiobutton3.configure(command=clear_entries)

root.TLabel1 = ttk.Label(root)
root.TLabel1.place(relx=0.432, rely=0.105, height=17, width=158)
root.TLabel1.configure(font="-family {Segoe UI} -size 9")
root.TLabel1.configure(relief="flat")
root.TLabel1.configure(anchor='w')
root.TLabel1.configure(justify='left')
root.TLabel1.configure(text='''Defina o arquivo de Origem''')
root.TLabel1.configure(compound='left')

root.TLabel2 = ttk.Label(root)
root.TLabel2.place(relx=0.432, rely=0.368, height=17, width=158)
root.TLabel2.configure(font="-family {Segoe UI} -size 9")
root.TLabel2.configure(relief="flat")
root.TLabel2.configure(anchor='w')
root.TLabel2.configure(justify='left')
root.TLabel2.configure(text='''Defina o arquivo de Destino''')
root.TLabel2.configure(compound='left')

root.Button3 = tk.Button(root)
root.Button3.place(relx=0.332, rely=0.737, height=26, width=187)
root.Button3.configure(activebackground="#d9d9d9")
root.Button3.configure(activeforeground="black")
root.Button3.configure(background="#d9d9d9")
root.Button3.configure(disabledforeground="#a3a3a3")
root.Button3.configure(foreground="#000000")
root.Button3.configure(highlightbackground="#d9d9d9")
root.Button3.configure(highlightcolor="#000000")
root.Button3.configure(text='''Executar!''')
root.Button3.configure(command=runMainVoid)

if DEBUG_MODE:
    root.Button4 = tk.Button(root)
    root.Button4.place(relx=0.020, rely=0.737, height=26, width=120)
    root.Button4.configure(activebackground="#d9d9d9")
    root.Button4.configure(activeforeground="black")
    root.Button4.configure(background="#d9d9d9")
    root.Button4.configure(disabledforeground="#a3a3a3")
    root.Button4.configure(foreground="#000000")
    root.Button4.configure(highlightbackground="#d9d9d9")
    root.Button4.configure(highlightcolor="#000000")
    root.Button4.configure(text='''Variáveis''')
    # root.Button4.configure(command=runMainVoid)

root.mainloop()