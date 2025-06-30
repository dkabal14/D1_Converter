import tkinter as tk
from tkinter import messagebox, filedialog
import tkinter.ttk as ttk
from tkinter.constants import END
import os
import subprocess
from typing import Literal
import uuid

class D1Converter:
    def __init__(self, title, experimental=False):
        # HB_TO_PY = 1
        # HB_TO_IPYNB = 2
        # IPYNB_TO_HB = 3
        # DEBUG_MODE = False

        self.HB_TO_PY = 1
        self.HB_TO_IPYNB = 2
        self.IPYNB_TO_HB = 3
        self.DEV_MODE = experimental
        self.default_title = title
        self.root_dir = os.path.dirname(os.path.abspath(__file__))
        # self.main_window()

    def to_path_linux(self, path):
        """
        Converte o caminho do arquivo para o formato Linux.
        """
        return path.replace("\\", "/")

    def to_path_windows(self, path):
        """
        Converte o caminho do arquivo para o formato Windows.
        """
        return path.replace("/", "\\")
    
    def choose_file_1(self):
        try:
            if self.main_window.rdbtn.get() == 1:
                file_type = [('Arquivo de um Robô', '*.json')]
            elif self.main_window.rdbtn.get() == 2:
                file_type = [('Arquivo de um Robô', '*.json')]
            elif self.main_window.rdbtn.get() == 3:
                file_type = [('IPython Jupyter Notebook', '*.ipynb')]
            else:
                raise Exception('É necessário escolher um tipo de conversão!')
            # TODO: Adicionar checagem se o json escolhido é de fato um arquivo válido para a conversão
            if self.main_window.Entry1.get() != '':
                initd = os.path.dirname(self.main_window.Entry1.get())
                initf = f'{".".join(os.path.basename(self.main_window.Entry1.get()).split(".")[:-1])}'
                self.file_name = filedialog.askopenfilename(filetypes=file_type, initialdir=initd, defaultextension=file_type[0][1], initialfile=initf)
            else:
                self.file_name = filedialog.askopenfilename(filetypes=file_type, initialdir=os.environ['USERPROFILE'], defaultextension=file_type[0][1])
            if self.file_name != '':
                self.main_window.Entry1.delete(0, END)
                self.main_window.Entry1.insert(0, self.to_path_windows(self.file_name))

        except Exception as e:
            messagebox.showwarning("Atenção!", f"{e}")

    def choose_file_2(self):
        try:
            if self.main_window.rdbtn.get() == 1:
                file_type = [('Script Python', '*.py')]
            elif self.main_window.rdbtn.get() == 2:
                file_type = [('IPython Jupyter Notebook', '*.ipynb')]
            elif self.main_window.rdbtn.get() == 3:
                file_type = [('Robô Highbond', '*.json')]
            else:
                raise Exception('É necessário escolher um tipo de conversão!')
            if self.main_window.Entry1.get() != '':
                initd = os.path.dirname(self.main_window.Entry1.get())
                initf = f'{".".join(os.path.basename(self.main_window.Entry1.get()).split(".")[:-1])}'
                self.file_name = filedialog.asksaveasfilename(filetypes=file_type, initialdir=initd, defaultextension=file_type[0][1], initialfile=initf)
            else:
                self.file_name = filedialog.asksaveasfilename(filetypes=file_type, initialdir=os.environ['USERPROFILE'], defaultextension=file_type[0][1])
            # TODO: Adicionar checagem se o json escolhido é de fato um arquivo válido para a conversão
            if self.file_name != '':
                self.main_window.Entry2.delete(0, END)
                self.main_window.Entry2.insert(0, self.to_path_windows(self.file_name))

        except Exception as e:
            messagebox.showwarning("Atenção!", f"{e}")
    
    def clear_entries(self):
        self.main_window.Entry1.delete(0, END)
        self.main_window.Entry2.delete(0, END)
    
    def run_conversion(self):
        try:
            i_file = self.to_path_linux(self.main_window.Entry1.get())
            o_file = self.to_path_linux(self.main_window.Entry2.get())

            if not bool(i_file) and not bool(o_file):
                raise Exception("Os arquivos de origem e destino precisam estar preenchidos!")
            elif not bool(i_file):
                raise Exception("O arquivo de origem precisa estar preenchido!")
            elif not bool(o_file):
                raise Exception("O arquivo de destino precisa estar preenchido!")
            
            if self.main_window.rdbtn.get() == 1:
                run1 = subprocess.run(['python.exe', f"{self.root_dir}/src/hb-json_to_py.py", i_file, o_file], capture_output=True, check=False)
                if run1.returncode != 0:
                    raise Exception(f"Falha na execução com o código {run1.returncode}: {run1.stderr}")
                else:
                    messagebox.showinfo(self.default_title, f'Arquivo "{o_file}" criado com sucesso!')

            elif self.main_window.rdbtn.get() == 2:
                run2 = subprocess.run(['python.exe', f"{self.root_dir}/src/hb-json_to_ipynb.py", i_file, o_file], capture_output=True, check=False)
                if run2.returncode != 0:
                    raise Exception(f"Falha na execução com o código {run2.returncode}: {run2.stderr}")
                else:
                    messagebox.showinfo(self.default_title, f'Arquivo "{o_file}" criado com sucesso!')

            elif self.main_window.rdbtn.get() == 3:
                run3 = subprocess.run(['python.exe', f"{self.root_dir}/src/ipynb_to_hb-json.py", i_file, o_file], capture_output=True, check=False)
                if run3.returncode != 0:
                    raise Exception(f"Falha na execução com o código {run3.returncode}: {run3.stderr}")
                else:
                    messagebox.showinfo(self.default_title, f'Arquivo "{o_file}" criado com sucesso!')
            else:
                raise Exception("É necessário escolher um tipo de conversão!")

        except Exception as e:
            messagebox.showwarning("Atenção", e)

    def main_window(self):
        self.main_window = tk.Tk()

        # Configurações Principais
        self.main_window.geometry("600x170+300+150")
        self.main_window.minsize(120, 1)
        self.main_window.maxsize(1370, 749)
        self.main_window.resizable(1,  1)
        self.main_window.title(self.default_title)
        self.main_window.configure(background="#d9d9d9")
        self.main_window.configure(highlightbackground="#d9d9d9")
        self.main_window.configure(highlightcolor="#000000")
        self.main_window.iconbitmap(f"{self.root_dir}/img/quality.ico")
        self.main_window.TSizegrip1 = ttk.Sizegrip(self.main_window)
        self.main_window.TSizegrip1.place(anchor='se', relx=1.0, rely=1.0)

        # Label dos Radio Buttons
        self.main_window.Label1 = tk.Label(self.main_window)
        self.main_window.Label1.place(relx=0.017, rely=0.105, height=21, width=191)
        self.main_window.Label1.configure(activebackground="#d9d9d9")
        self.main_window.Label1.configure(activeforeground="black")
        self.main_window.Label1.configure(anchor='w')
        self.main_window.Label1.configure(background="#d9d9d9")
        self.main_window.Label1.configure(compound='left')
        self.main_window.Label1.configure(disabledforeground="#a3a3a3")
        self.main_window.Label1.configure(font="-family {Segoe UI} -size 9")
        self.main_window.Label1.configure(foreground="#000000")
        self.main_window.Label1.configure(highlightbackground="#d9d9d9")
        self.main_window.Label1.configure(highlightcolor="#000000")
        self.main_window.Label1.configure(text='''Selecione o Método de Conversão:''')

        # Configuração da Entrada de Texto 1
        self.main_window.Entry1 = tk.Entry(self.main_window)
        self.main_window.Entry1.place(relx=0.432, rely=0.211, height=20, relwidth=0.488)
        self.main_window.Entry1.configure(background="white")
        self.main_window.Entry1.configure(disabledforeground="#a3a3a3")
        self.main_window.Entry1.configure(font="-family {Courier New} -size 10")
        self.main_window.Entry1.configure(foreground="#000000")
        self.main_window.Entry1.configure(highlightbackground="#d9d9d9")
        self.main_window.Entry1.configure(highlightcolor="#000000")
        self.main_window.Entry1.configure(insertbackground="#000000")
        self.main_window.Entry1.configure(selectbackground="#d9d9d9")
        self.main_window.Entry1.configure(selectforeground="black")

        # Configuração da Entrada de Texto 2
        self.main_window.Entry2 = tk.Entry(self.main_window)
        self.main_window.Entry2.place(relx=0.432, rely=0.474, height=20, relwidth=0.488)
        self.main_window.Entry2.configure(background="white")
        self.main_window.Entry2.configure(disabledforeground="#a3a3a3")
        self.main_window.Entry2.configure(font="-family {Courier New} -size 10")
        self.main_window.Entry2.configure(foreground="#000000")
        self.main_window.Entry2.configure(highlightbackground="#d9d9d9")
        self.main_window.Entry2.configure(highlightcolor="#000000")
        self.main_window.Entry2.configure(insertbackground="#000000")
        self.main_window.Entry2.configure(selectbackground="#d9d9d9")
        self.main_window.Entry2.configure(selectforeground="black")

        # Configuração do Botão de Escolha do Arquivo 1
        self.main_window.Button1 = tk.Button(self.main_window)
        self.main_window.Button1.place(relx=0.93, rely=0.211, height=26, width=27)
        self.main_window.Button1.configure(activebackground="#d9d9d9")
        self.main_window.Button1.configure(activeforeground="black")
        self.main_window.Button1.configure(background="#d9d9d9")
        self.main_window.Button1.configure(disabledforeground="#a3a3a3")
        self.main_window.Button1.configure(foreground="#000000")
        self.main_window.Button1.configure(highlightbackground="#d9d9d9")
        self.main_window.Button1.configure(highlightcolor="#000000")
        self.main_window.Button1.configure(text='''...''')
        self.main_window.Button1.configure(command=self.choose_file_1)

        # Configuração do Botão de Escolha do Arquivo 2
        self.main_window.Button2 = tk.Button(self.main_window)
        self.main_window.Button2.place(relx=0.93, rely=0.474, height=26, width=27)
        self.main_window.Button2.configure(activebackground="#d9d9d9")
        self.main_window.Button2.configure(activeforeground="black")
        self.main_window.Button2.configure(background="#d9d9d9")
        self.main_window.Button2.configure(cursor="fleur")
        self.main_window.Button2.configure(disabledforeground="#a3a3a3")
        self.main_window.Button2.configure(font="-family {Segoe UI} -size 9")
        self.main_window.Button2.configure(foreground="#000000")
        self.main_window.Button2.configure(highlightbackground="#d9d9d9")
        self.main_window.Button2.configure(highlightcolor="#000000")
        self.main_window.Button2.configure(text='''...''')
        self.main_window.Button2.configure(command=self.choose_file_2)

        # Configuração Geral dos Radio Buttons
        self.main_window.rdbtn = tk.IntVar()

        # Configuração do Radio Button 1
        self.main_window.Radiobutton1 = tk.Radiobutton(self.main_window)
        self.main_window.Radiobutton1.place(relx=0.017, rely=0.211, relheight=0.132, relwidth=0.256)
        self.main_window.Radiobutton1.configure(activebackground="#d9d9d9")
        self.main_window.Radiobutton1.configure(activeforeground="black")
        self.main_window.Radiobutton1.configure(anchor='w')
        self.main_window.Radiobutton1.configure(background="#d9d9d9")
        self.main_window.Radiobutton1.configure(compound='left')
        self.main_window.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.main_window.Radiobutton1.configure(font="-family {Segoe UI} -size 9")
        self.main_window.Radiobutton1.configure(foreground="#000000")
        self.main_window.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.main_window.Radiobutton1.configure(highlightcolor="#000000")
        self.main_window.Radiobutton1.configure(justify='left')
        self.main_window.Radiobutton1.configure(overrelief="groove")
        self.main_window.Radiobutton1.configure(text='''HB-JSON -> Python''')
        self.main_window.Radiobutton1.configure(underline="-100")
        self.main_window.Radiobutton1.configure(variable=self.main_window.rdbtn)
        self.main_window.Radiobutton1.configure(value=self.HB_TO_PY)
        self.main_window.Radiobutton1.configure(command=self.clear_entries)

        # Configuração do Radio Button 2
        self.main_window.Radiobutton2 = tk.Radiobutton(self.main_window)
        self.main_window.Radiobutton2.place(relx=0.017, rely=0.368, relheight=0.132, relwidth=0.322)
        self.main_window.Radiobutton2.configure(activebackground="#d9d9d9")
        self.main_window.Radiobutton2.configure(activeforeground="black")
        self.main_window.Radiobutton2.configure(anchor='w')
        self.main_window.Radiobutton2.configure(background="#d9d9d9")
        self.main_window.Radiobutton2.configure(compound='left')
        self.main_window.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.main_window.Radiobutton2.configure(font="-family {Segoe UI} -size 9")
        self.main_window.Radiobutton2.configure(foreground="#000000")
        self.main_window.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.main_window.Radiobutton2.configure(highlightcolor="#000000")
        self.main_window.Radiobutton2.configure(justify='left')
        self.main_window.Radiobutton2.configure(overrelief="groove")
        self.main_window.Radiobutton2.configure(text='''HB-JSON -> Jupyter Notebook''')
        self.main_window.Radiobutton2.configure(underline="-100")
        self.main_window.Radiobutton2.configure(variable=self.main_window.rdbtn)
        self.main_window.Radiobutton2.configure(value=self.HB_TO_IPYNB)
        self.main_window.Radiobutton2.configure(command=self.clear_entries)

        # Configuração do Radio Button 3
        self.main_window.Radiobutton3 = tk.Radiobutton(self.main_window)
        self.main_window.Radiobutton3.place(relx=0.017, rely=0.526, relheight=0.132, relwidth=0.322)
        self.main_window.Radiobutton3.configure(activebackground="#d9d9d9")
        self.main_window.Radiobutton3.configure(activeforeground="black")
        self.main_window.Radiobutton3.configure(anchor='w')
        self.main_window.Radiobutton3.configure(background="#d9d9d9")
        self.main_window.Radiobutton3.configure(compound='left')
        self.main_window.Radiobutton3.configure(disabledforeground="#a3a3a3")
        self.main_window.Radiobutton3.configure(font="-family {Segoe UI} -size 9")
        self.main_window.Radiobutton3.configure(foreground="#000000")
        self.main_window.Radiobutton3.configure(highlightbackground="#d9d9d9")
        self.main_window.Radiobutton3.configure(highlightcolor="#000000")
        self.main_window.Radiobutton3.configure(justify='left')
        self.main_window.Radiobutton3.configure(overrelief="groove")
        self.main_window.Radiobutton3.configure(text='''Jupyter Notebook -> HB-JSON''')
        self.main_window.Radiobutton3.configure(underline="-100")
        self.main_window.Radiobutton3.configure(variable=self.main_window.rdbtn)
        self.main_window.Radiobutton3.configure(value=self.IPYNB_TO_HB)
        self.main_window.Radiobutton3.configure(command=self.clear_entries)

        # Configuração da Label de Escolha do Arquivo 1
        self.main_window.TLabel1 = ttk.Label(self.main_window)
        self.main_window.TLabel1.place(relx=0.432, rely=0.105, height=17, width=158)
        self.main_window.TLabel1.configure(font="-family {Segoe UI} -size 9")
        self.main_window.TLabel1.configure(relief="flat")
        self.main_window.TLabel1.configure(anchor='w')
        self.main_window.TLabel1.configure(justify='left')
        self.main_window.TLabel1.configure(text='''Defina o arquivo de Origem''')
        self.main_window.TLabel1.configure(compound='left')

        # Configuração da Label de Escolha do Arquivo 2
        self.main_window.TLabel2 = ttk.Label(self.main_window)
        self.main_window.TLabel2.place(relx=0.432, rely=0.368, height=17, width=158)
        self.main_window.TLabel2.configure(font="-family {Segoe UI} -size 9")
        self.main_window.TLabel2.configure(relief="flat")
        self.main_window.TLabel2.configure(anchor='w')
        self.main_window.TLabel2.configure(justify='left')
        self.main_window.TLabel2.configure(text='''Defina o arquivo de Destino''')
        self.main_window.TLabel2.configure(compound='left')

        # Configuração do Botão Executar!
        self.Button3 = tk.Button(self.main_window)
        self.Button3.place(relx=0.332, rely=0.737, height=26, width=187)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="black")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="#000000")
        self.Button3.configure(text='''Executar!''')
        self.Button3.configure(command=self.run_conversion)

        # INDEV:  
        if self.DEV_MODE:
            self.main_window.Button4 = tk.Button(self.main_window)
            self.main_window.Button4.place(relx=0.020, rely=0.737, height=26, width=120)
            self.main_window.Button4.configure(activebackground="#d9d9d9")
            self.main_window.Button4.configure(activeforeground="black")
            self.main_window.Button4.configure(background="#d9d9d9")
            self.main_window.Button4.configure(disabledforeground="#a3a3a3")
            self.main_window.Button4.configure(foreground="#000000")
            self.main_window.Button4.configure(highlightbackground="#d9d9d9")
            self.main_window.Button4.configure(highlightcolor="#000000")
            self.main_window.Button4.configure(text='''Variáveis''')
            self.main_window.Button4.configure(command=self.vars_window)

        self.main_window.mainloop()

    def vars_window(self):
        self.vars_window = tk.Tk()

        # Configurações Principais
        self.vars_window.geometry("800x300")
        self.vars_window.minsize(120, 1)
        self.vars_window.maxsize(1370, 749)
        self.vars_window.resizable(1,  1)
        self.vars_window.title("Variáveis do D1")
        self.vars_window.configure(background="#d9d9d9")
        self.vars_window.configure(highlightbackground="#d9d9d9")
        self.vars_window.configure(highlightcolor="#000000")
        self.vars_window.iconbitmap(f"{self.root_dir}/img/quality.ico")
        self.vars_window.TSizegrip1 = ttk.Sizegrip(self.vars_window)
        self.vars_window.TSizegrip1.place(anchor='se', relx=1.0, rely=1.0)
        
        # Configurações do Frame
        self.vars_window.list_frame = tk.Frame(self.vars_window)
        self.vars_window.list_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Configurações da Tabela treeview
        self.vars_window.tree = ttk.Treeview(self.vars_window.list_frame, columns=('name', 'type', 'taskInputLabel', 'value'), show='headings')
        self.vars_window.tree.heading('name', text='Nome')
        self.vars_window.tree.column('name', anchor='w', width=50)
        self.vars_window.tree.heading('type', text='Tipo')
        self.vars_window.tree.column('type', anchor='w', width=50)
        self.vars_window.tree.heading('taskInputLabel', text='Label')
        self.vars_window.tree.column('taskInputLabel', anchor='w', width=50)
        self.vars_window.tree.heading('value', text='Valor')
        self.vars_window.tree.column('value', anchor='w', width=50)
        
        self.vars_window.tree.pack(fill=tk.BOTH, expand=True)

        # Configurações dos painel de botões
        self.vars_window.buttons_frame = tk.Frame(self.vars_window)
        self.vars_window.buttons_frame.pack(fill=tk.X, padx=5, pady=5)

        # Configurações do botão de criar
        self.vars_window.create_button = tk.Button(self.vars_window.buttons_frame, text='Criar JSON')
        self.vars_window.create_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Configurações do botão de carregar
        self.vars_window.load_button = tk.Button(self.vars_window.buttons_frame, text='Carregar JSON')
        self.vars_window.load_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Configurações do botão de salvar
        self.vars_window.save_button = tk.Button(self.vars_window.buttons_frame, text='Salvar JSON')
        self.vars_window.save_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Configurações do botão de adicionar
        self.vars_window.add_button = tk.Button(self.vars_window.buttons_frame, text='Adicionar Variável')
        self.vars_window.add_button.pack(side=tk.RIGHT, padx=5, pady=5)
        self.vars_window.add_button.configure(command=self.add_var_form)

        # Configurações do botão de editar
        self.vars_window.edit_button = tk.Button(self.vars_window.buttons_frame, text='Editar Variável')
        self.vars_window.edit_button.pack(side=tk.RIGHT, padx=5, pady=5)

        # Configurações do botão de remover
        self.vars_window.remove_button = tk.Button(self.vars_window.buttons_frame, text='Remover Variável')
        self.vars_window.remove_button.pack(side=tk.RIGHT, padx=5, pady=5)

    def add_var_form(self):
        self.add_var_window = tk.Tk()
            # variáveis
            # {
            #    "id": "b60eee3e-523b-42c8-87a7-cd81a3cad55f",
            #    "name": "v_hb_token",
            #    "type": "password",
            #    "value": "",
            #    "isReadOnly": false,
            #    "isTaskInput": true,
            #    "taskInputLabel": "Insira seu Token do Diligent One",
            #    "taskInputDescription": "",
            #    "isTaskInputValueOptional": false
            # }
        # Configurações Principais
        window_width = 450
        window_height = 350
        self.add_var_window.geometry(f"{window_width}x{window_height}")
        self.add_var_window.minsize(120, 1)
        self.add_var_window.maxsize(1370, 749)
        self.add_var_window.resizable(1,  1)
        self.add_var_window.title("Variáveis do D1")
        self.add_var_window.configure(background="#d9d9d9")
        self.add_var_window.configure(highlightbackground="#d9d9d9")
        self.add_var_window.configure(highlightcolor="#000000")
        self.add_var_window.iconbitmap(f"{self.root_dir}/img/quality.ico")
        self.add_var_window.TSizegrip1 = ttk.Sizegrip(self.add_var_window)
        self.add_var_window.TSizegrip1.place(anchor='se', relx=1.0, rely=1.0)

        fixed_label_widths = 160
        fixed_entry_widths = 200
        fixed_x_position_labels = 20/window_width
        fixed_x_position_entries = 200/window_width

        curr_y_position = 0.060
        y_position_iteration = 0.100

        self.add_var_window.Label1 = tk.Label(self.add_var_window)
        self.add_var_window.Label1.place(relx=fixed_x_position_labels, rely=curr_y_position, height=30, width=fixed_label_widths)
        self.add_var_window.Label1.configure(activebackground="#d9d9d9")
        self.add_var_window.Label1.configure(activeforeground="black")
        self.add_var_window.Label1.configure(anchor='e')
        self.add_var_window.Label1.configure(background="#d9d9d9")
        self.add_var_window.Label1.configure(compound='left')
        self.add_var_window.Label1.configure(disabledforeground="#a3a3a3")
        self.add_var_window.Label1.configure(font="-family {Segoe UI} -size 9")
        self.add_var_window.Label1.configure(foreground="#000000")
        self.add_var_window.Label1.configure(highlightbackground="#d9d9d9")
        self.add_var_window.Label1.configure(highlightcolor="#000000")
        self.add_var_window.Label1.configure(justify='right')
        self.add_var_window.Label1.configure(text='Nome da Variável:')

        self.add_var_window.Entry1 = tk.Entry(self.add_var_window)
        self.add_var_window.Entry1.place(relx=fixed_x_position_entries, rely=curr_y_position, height=30, width=fixed_entry_widths)
        self.add_var_window.Entry1.configure(background="white")
        self.add_var_window.Entry1.configure(disabledforeground="#a3a3a3")
        self.add_var_window.Entry1.configure(font="-family {Courier New} -size 10")
        self.add_var_window.Entry1.configure(foreground="#000000")
        self.add_var_window.Entry1.configure(highlightbackground="#d9d9d9")
        self.add_var_window.Entry1.configure(highlightcolor="#000000")
        self.add_var_window.Entry1.configure(insertbackground="#000000")
        self.add_var_window.Entry1.configure(selectbackground="#d9d9d9")
        self.add_var_window.Entry1.configure(selectforeground="black")
        
        curr_y_position += y_position_iteration
        self.add_var_window.Label2 = tk.Label(self.add_var_window)
        self.add_var_window.Label2.place(relx=fixed_x_position_labels, rely=curr_y_position, height=30, width=fixed_label_widths)
        self.add_var_window.Label2.configure(activebackground="#d9d9d9")
        self.add_var_window.Label2.configure(activeforeground="black")
        self.add_var_window.Label2.configure(anchor='e')
        self.add_var_window.Label2.configure(background="#d9d9d9")
        self.add_var_window.Label2.configure(compound='left')
        self.add_var_window.Label2.configure(disabledforeground="#a3a3a3")
        self.add_var_window.Label2.configure(font="-family {Segoe UI} -size 9")
        self.add_var_window.Label2.configure(foreground="#000000")
        self.add_var_window.Label2.configure(highlightbackground="#d9d9d9")
        self.add_var_window.Label2.configure(highlightcolor="#000000")
        self.add_var_window.Label2.configure(text='Tipo da Variável:')

        self.add_var_window.Combo2 = ttk.Combobox(self.add_var_window, state="readonly")
        self.add_var_window.Combo2.place(relx=fixed_x_position_entries, rely=curr_y_position, height=30, width=180)
        self.add_var_window.Combo2.configure(font="-family {Segoe UI} -size 9")
        self.add_var_window.Combo2['values'] = ("Texto", "Senha")
        self.add_var_window.Combo2.current(0)

        curr_y_position += y_position_iteration
        self.add_var_window.Label3 = tk.Label(self.add_var_window)
        self.add_var_window.Label3.place(relx=fixed_x_position_labels, rely=curr_y_position, height=30, width=fixed_label_widths)
        self.add_var_window.Label3.configure(activebackground="#d9d9d9")
        self.add_var_window.Label3.configure(activeforeground="black")
        self.add_var_window.Label3.configure(anchor='e')
        self.add_var_window.Label3.configure(background="#d9d9d9")
        self.add_var_window.Label3.configure(compound='left')
        self.add_var_window.Label3.configure(disabledforeground="#a3a3a3")
        self.add_var_window.Label3.configure(font="-family {Segoe UI} -size 9")
        self.add_var_window.Label3.configure(foreground="#000000")
        self.add_var_window.Label3.configure(highlightbackground="#d9d9d9")
        self.add_var_window.Label3.configure(highlightcolor="#000000")
        self.add_var_window.Label3.configure(text='Valor da Variável:')

        self.add_var_window.Entry3 = tk.Entry(self.add_var_window)
        self.add_var_window.Entry3.place(relx=fixed_x_position_entries, rely=curr_y_position, height=30, width=fixed_entry_widths)
        self.add_var_window.Entry3.configure(background="white")
        self.add_var_window.Entry3.configure(disabledforeground="#a3a3a3")
        self.add_var_window.Entry3.configure(font="-family {Courier New} -size 10")
        self.add_var_window.Entry3.configure(foreground="#000000")
        self.add_var_window.Entry3.configure(highlightbackground="#d9d9d9")
        self.add_var_window.Entry3.configure(highlightcolor="#000000")
        self.add_var_window.Entry3.configure(insertbackground="#000000")
        self.add_var_window.Entry3.configure(selectbackground="#d9d9d9")
        self.add_var_window.Entry3.configure(selectforeground="black")

        curr_y_position += y_position_iteration
        self.add_var_window.Label4 = tk.Label(self.add_var_window)
        self.add_var_window.Label4.place(relx=fixed_x_position_labels, rely=curr_y_position, height=30, width=fixed_label_widths)
        self.add_var_window.Label4.configure(activebackground="#d9d9d9")
        self.add_var_window.Label4.configure(activeforeground="black")
        self.add_var_window.Label4.configure(anchor='e')
        self.add_var_window.Label4.configure(background="#d9d9d9")
        self.add_var_window.Label4.configure(compound='left')
        self.add_var_window.Label4.configure(disabledforeground="#a3a3a3")
        self.add_var_window.Label4.configure(font="-family {Segoe UI} -size 9")
        self.add_var_window.Label4.configure(foreground="#000000")
        self.add_var_window.Label4.configure(highlightbackground="#d9d9d9")
        self.add_var_window.Label4.configure(highlightcolor="#000000")
        self.add_var_window.Label4.configure(text='Somente Leitura?')

        self.add_var_window.CheckButton4 = tk.Checkbutton(self.add_var_window)
        self.add_var_window.CheckButton4.place(relx=fixed_x_position_entries, rely=curr_y_position, height=30, width=20)
        self.add_var_window.CheckButton4.configure(background="#d9d9d9")
        self.add_var_window.CheckButton4.configure(disabledforeground="#a3a3a3")
        self.add_var_window.CheckButton4.configure(font="-family {Courier New} -size 10")
        self.add_var_window.CheckButton4.configure(foreground="#000000")
        self.add_var_window.CheckButton4.configure(highlightbackground="#d9d9d9")
        self.add_var_window.CheckButton4.configure(highlightcolor="#000000")

        curr_y_position += y_position_iteration
        self.add_var_window.Label5 = tk.Label(self.add_var_window)
        self.add_var_window.Label5.place(relx=fixed_x_position_labels, rely=curr_y_position, height=30, width=fixed_label_widths)
        self.add_var_window.Label5.configure(activebackground="#d9d9d9")
        self.add_var_window.Label5.configure(activeforeground="black")
        self.add_var_window.Label5.configure(anchor='e')
        self.add_var_window.Label5.configure(background="#d9d9d9")
        self.add_var_window.Label5.configure(compound='left')
        self.add_var_window.Label5.configure(disabledforeground="#a3a3a3")
        self.add_var_window.Label5.configure(font="-family {Segoe UI} -size 9")
        self.add_var_window.Label5.configure(foreground="#000000")
        self.add_var_window.Label5.configure(highlightbackground="#d9d9d9")
        self.add_var_window.Label5.configure(highlightcolor="#000000")
        self.add_var_window.Label5.configure(text='É um Parâmetro do Robô?')

        self.add_var_window.is_task_input_var = tk.BooleanVar()
        self.add_var_window.CheckButton5 = tk.Checkbutton(self.add_var_window)
        self.add_var_window.CheckButton5.place(relx=fixed_x_position_entries, rely=curr_y_position, height=30, width=20)
        self.add_var_window.CheckButton5.configure(background="#d9d9d9")
        self.add_var_window.CheckButton5.configure(disabledforeground="#a3a3a3")
        self.add_var_window.CheckButton5.configure(font="-family {Courier New} -size 10")
        self.add_var_window.CheckButton5.configure(foreground="#000000")
        self.add_var_window.CheckButton5.configure(highlightbackground="#d9d9d9")
        self.add_var_window.CheckButton5.configure(highlightcolor="#000000")
        self.add_var_window.CheckButton5.configure(variable=self.add_var_window.is_task_input_var)

        curr_y_position += y_position_iteration
        self.add_var_window.Label6 = tk.Label(self.add_var_window)
        self.add_var_window.Label6.place(relx=fixed_x_position_labels, rely=curr_y_position, height=30, width=fixed_label_widths)
        self.add_var_window.Label6.configure(activebackground="#d9d9d9")
        self.add_var_window.Label6.configure(activeforeground="black")
        self.add_var_window.Label6.configure(anchor='e')
        self.add_var_window.Label6.configure(background="#d9d9d9")
        self.add_var_window.Label6.configure(compound='left')
        self.add_var_window.Label6.configure(disabledforeground="#a3a3a3")
        self.add_var_window.Label6.configure(font="-family {Segoe UI} -size 9")
        self.add_var_window.Label6.configure(foreground="#000000")
        self.add_var_window.Label6.configure(highlightbackground="#d9d9d9")
        self.add_var_window.Label6.configure(highlightcolor="#000000")
        self.add_var_window.Label6.configure(text='Nome do Parâmetro:')

        self.add_var_window.Entry6 = tk.Entry(self.add_var_window)
        self.add_var_window.Entry6.place(relx=fixed_x_position_entries, rely=curr_y_position, height=30, width=fixed_entry_widths)
        self.add_var_window.Entry6.configure(background="white")
        self.add_var_window.Entry6.configure(disabledforeground="#a3a3a3")
        self.add_var_window.Entry6.configure(font="-family {Courier New} -size 10")
        self.add_var_window.Entry6.configure(foreground="#000000")
        self.add_var_window.Entry6.configure(highlightbackground="#d9d9d9")
        self.add_var_window.Entry6.configure(highlightcolor="#000000")
        self.add_var_window.Entry6.configure(insertbackground="#000000")
        self.add_var_window.Entry6.configure(selectbackground="#d9d9d9")
        self.add_var_window.Entry6.configure(selectforeground="black")
        self.add_var_window.Entry6.configure(state="disabled")

        curr_y_position += y_position_iteration
        self.add_var_window.Label7 = tk.Label(self.add_var_window)
        self.add_var_window.Label7.place(relx=fixed_x_position_labels, rely=curr_y_position, height=30, width=fixed_label_widths)
        self.add_var_window.Label7.configure(activebackground="#d9d9d9")
        self.add_var_window.Label7.configure(activeforeground="black")
        self.add_var_window.Label7.configure(anchor='e')
        self.add_var_window.Label7.configure(background="#d9d9d9")
        self.add_var_window.Label7.configure(compound='left')
        self.add_var_window.Label7.configure(disabledforeground="#a3a3a3")
        self.add_var_window.Label7.configure(font="-family {Segoe UI} -size 9")
        self.add_var_window.Label7.configure(foreground="#000000")
        self.add_var_window.Label7.configure(highlightbackground="#d9d9d9")
        self.add_var_window.Label7.configure(highlightcolor="#000000")
        self.add_var_window.Label7.configure(text='Descrição do Parâmetro:')

        self.add_var_window.Entry7 = tk.Entry(self.add_var_window)
        self.add_var_window.Entry7.place(relx=fixed_x_position_entries, rely=curr_y_position, height=30, width=fixed_entry_widths)
        self.add_var_window.Entry7.configure(background="white")
        self.add_var_window.Entry7.configure(disabledforeground="#706f6f")
        self.add_var_window.Entry7.configure(font="-family {Courier New} -size 10")
        self.add_var_window.Entry7.configure(foreground="#000000")
        self.add_var_window.Entry7.configure(highlightbackground="#d9d9d9")
        self.add_var_window.Entry7.configure(highlightcolor="#000000")
        self.add_var_window.Entry7.configure(insertbackground="#000000")
        self.add_var_window.Entry7.configure(selectbackground="#d9d9d9")
        self.add_var_window.Entry7.configure(selectforeground="black")
        self.add_var_window.Entry7.configure(state="disabled")


        curr_y_position += y_position_iteration
        self.add_var_window.Label8 = tk.Label(self.add_var_window)
        self.add_var_window.Label8.place(relx=fixed_x_position_labels, rely=curr_y_position, height=30, width=fixed_label_widths)
        self.add_var_window.Label8.configure(activebackground="#d9d9d9")
        self.add_var_window.Label8.configure(activeforeground="black")
        self.add_var_window.Label8.configure(anchor='e')
        self.add_var_window.Label8.configure(background="#d9d9d9")
        self.add_var_window.Label8.configure(compound='left')
        self.add_var_window.Label8.configure(disabledforeground="#a3a3a3")
        self.add_var_window.Label8.configure(font="-family {Segoe UI} -size 9")
        self.add_var_window.Label8.configure(foreground="#000000")
        self.add_var_window.Label8.configure(highlightbackground="#d9d9d9")
        self.add_var_window.Label8.configure(highlightcolor="#000000")
        self.add_var_window.Label8.configure(text='Parâmetro Opcional?')

        self.add_var_window.CheckButton8 = tk.Checkbutton(self.add_var_window)
        self.add_var_window.CheckButton8.place(relx=fixed_x_position_entries, rely=curr_y_position, height=30, width=20)
        self.add_var_window.CheckButton8.configure(background="#d9d9d9")
        self.add_var_window.CheckButton8.configure(disabledforeground="#706f6f")
        self.add_var_window.CheckButton8.configure(font="-family {Courier New} -size 10")
        self.add_var_window.CheckButton8.configure(foreground="#000000")
        self.add_var_window.CheckButton8.configure(highlightbackground="#d9d9d9")
        self.add_var_window.CheckButton8.configure(highlightcolor="#000000")
        self.add_var_window.CheckButton8.configure(state="disabled")

        curr_y_position += y_position_iteration
        self.add_var_window.Button1 = tk.Button(self.add_var_window)
        self.add_var_window.Button1.place(relx=120/window_width, rely=curr_y_position, height=30, width=100)
        self.add_var_window.Button1.configure(activebackground="#d9d9d9")
        self.add_var_window.Button1.configure(activeforeground="black")
        self.add_var_window.Button1.configure(background="#d9d9d9")
        self.add_var_window.Button1.configure(disabledforeground="#a3a3a3")
        self.add_var_window.Button1.configure(foreground="#000000")
        self.add_var_window.Button1.configure(highlightbackground="#d9d9d9")
        self.add_var_window.Button1.configure(highlightcolor="#000000")
        self.add_var_window.Button1.configure(text='Salvar')

        self.add_var_window.Button1 = tk.Button(self.add_var_window)
        self.add_var_window.Button1.place(relx=230/window_width, rely=curr_y_position, height=30, width=100)
        self.add_var_window.Button1.configure(activebackground="#d9d9d9")
        self.add_var_window.Button1.configure(activeforeground="black")
        self.add_var_window.Button1.configure(background="#d9d9d9")
        self.add_var_window.Button1.configure(disabledforeground="#a3a3a3")
        self.add_var_window.Button1.configure(foreground="#000000")
        self.add_var_window.Button1.configure(highlightbackground="#d9d9d9")
        self.add_var_window.Button1.configure(highlightcolor="#000000")
        self.add_var_window.Button1.configure(text='Cancelar')

if __name__ == "__main__":
    d1c = D1Converter(title="Ferramenta de Conversão do D1 - v0.0.4", experimental=True)
    d1c.main_window()