import tkinter as tk
from tkinter import messagebox, filedialog
import tkinter.ttk as ttk
from tkinter.constants import END
import os
import subprocess

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
            if self.root.rdbtn.get() == 1:
                file_type = [('Arquivo de um Robô', '*.json')]
            elif self.root.rdbtn.get() == 2:
                file_type = [('Arquivo de um Robô', '*.json')]
            elif self.root.rdbtn.get() == 3:
                file_type = [('IPython Jupyter Notebook', '*.ipynb')]
            else:
                raise Exception('É necessário escolher um tipo de conversão!')
            # TODO: Adicionar checagem se o json escolhido é de fato um arquivo válido para a conversão
            if self.root.Entry1.get() != '':
                initd = os.path.dirname(self.root.Entry1.get())
                initf = f'{".".join(os.path.basename(self.root.Entry1.get()).split(".")[:-1])}'
                self.file_name = filedialog.askopenfilename(filetypes=file_type, initialdir=initd, defaultextension=file_type[0][1], initialfile=initf)
            else:
                self.file_name = filedialog.askopenfilename(filetypes=file_type, initialdir=os.environ['USERPROFILE'], defaultextension=file_type[0][1])
            if self.file_name != '':
                self.root.Entry1.delete(0, END)
                self.root.Entry1.insert(0, self.to_path_windows(self.file_name))

        except Exception as e:
            messagebox.showwarning("Atenção!", f"{e}")

    def choose_file_2(self):
        try:
            if self.root.rdbtn.get() == 1:
                file_type = [('Script Python', '*.py')]
            elif self.root.rdbtn.get() == 2:
                file_type = [('IPython Jupyter Notebook', '*.ipynb')]
            elif self.root.rdbtn.get() == 3:
                file_type = [('Robô Highbond', '*.json')]
            else:
                raise Exception('É necessário escolher um tipo de conversão!')
            if self.root.Entry1.get() != '':
                initd = os.path.dirname(self.root.Entry1.get())
                initf = f'{".".join(os.path.basename(self.root.Entry1.get()).split(".")[:-1])}'
                self.file_name = filedialog.asksaveasfilename(filetypes=file_type, initialdir=initd, defaultextension=file_type[0][1], initialfile=initf)
            else:
                self.file_name = filedialog.asksaveasfilename(filetypes=file_type, initialdir=os.environ['USERPROFILE'], defaultextension=file_type[0][1])
            # TODO: Adicionar checagem se o json escolhido é de fato um arquivo válido para a conversão
            if self.file_name != '':
                self.root.Entry2.delete(0, END)
                self.root.Entry2.insert(0, self.to_path_windows(self.file_name))

        except Exception as e:
            messagebox.showwarning("Atenção!", f"{e}")
    
    def clear_entries(self):
        self.root.Entry1.delete(0, END)
        self.root.Entry2.delete(0, END)
    
    def run_conversion(self):
        try:
            i_file = self.to_path_linux(self.root.Entry1.get())
            o_file = self.to_path_linux(self.root.Entry2.get())

            if not bool(i_file) and not bool(o_file):
                raise Exception("Os arquivos de origem e destino precisam estar preenchidos!")
            elif not bool(i_file):
                raise Exception("O arquivo de origem precisa estar preenchido!")
            elif not bool(o_file):
                raise Exception("O arquivo de destino precisa estar preenchido!")
            
            if self.root.rdbtn.get() == 1:
                run1 = subprocess.run(['python.exe', f"{self.root_dir}/src/hb-json_to_py.py", i_file, o_file], capture_output=True, check=False)
                if run1.returncode != 0:
                    raise Exception(f"Falha na execução com o código {run1.returncode}: {run1.stderr}")
                else:
                    messagebox.showinfo(self.default_title, f"Arquivo {o_file} criado com sucesso!")
            elif self.root.rdbtn.get() == 2:
                run2 = subprocess.run(['python.exe', f"{self.root_dir}/src/hb-json_to_ipynb.py", i_file, o_file], capture_output=True, check=False)
                if run2.returncode != 0:
                    raise Exception(self.default_title, f"Falha na execução com o código {run2.returncode}: {run2.stderr}")
                else:
                    messagebox.showinfo(f"Arquivo {o_file} criado com sucesso!")
            elif self.root.rdbtn.get() == 3:
                run3 = subprocess.run(['python.exe', f"{self.root_dir}/src/ipynb_to_hb-json.py", i_file, o_file], capture_output=True, check=False)
                if run3.returncode != 0:
                    raise Exception(f"Falha na execução com o código {run3.returncode}: {run3.stderr}")
                else:
                    messagebox.showinfo(self.default_title, f"Arquivo {o_file} criado com sucesso!")
            else:
                raise Exception("É necessário escolher um tipo de conversão!")

        except Exception as e:
            messagebox.showwarning("Atenção", e)

    def main_window(self):
        self.root = tk.Tk()

        # Configurações Principais
        self.root.geometry("600x170+300+150")
        self.root.minsize(120, 1)
        self.root.maxsize(1370, 749)
        self.root.resizable(1,  0)
        self.root.title(self.default_title)
        self.root.configure(background="#d9d9d9")
        self.root.configure(highlightbackground="#d9d9d9")
        self.root.configure(highlightcolor="#000000")
        self.root.iconbitmap(f"{self.root_dir}/img/quality.ico")
        self.root.TSizegrip1 = ttk.Sizegrip(self.root)
        self.root.TSizegrip1.place(anchor='se', relx=1.0, rely=1.0)

        # Label dos Radio Buttons
        self.root.Label1 = tk.Label(self.root)
        self.root.Label1.place(relx=0.017, rely=0.105, height=21, width=191)
        self.root.Label1.configure(activebackground="#d9d9d9")
        self.root.Label1.configure(activeforeground="black")
        self.root.Label1.configure(anchor='w')
        self.root.Label1.configure(background="#d9d9d9")
        self.root.Label1.configure(compound='left')
        self.root.Label1.configure(disabledforeground="#a3a3a3")
        self.root.Label1.configure(font="-family {Segoe UI} -size 9")
        self.root.Label1.configure(foreground="#000000")
        self.root.Label1.configure(highlightbackground="#d9d9d9")
        self.root.Label1.configure(highlightcolor="#000000")
        self.root.Label1.configure(text='''Selecione o Método de Conversão:''')

        # Configuração da Entrada de Texto 1
        self.root.Entry1 = tk.Entry(self.root)
        self.root.Entry1.place(relx=0.432, rely=0.211, height=20, relwidth=0.488)
        self.root.Entry1.configure(background="white")
        self.root.Entry1.configure(disabledforeground="#a3a3a3")
        self.root.Entry1.configure(font="-family {Courier New} -size 10")
        self.root.Entry1.configure(foreground="#000000")
        self.root.Entry1.configure(highlightbackground="#d9d9d9")
        self.root.Entry1.configure(highlightcolor="#000000")
        self.root.Entry1.configure(insertbackground="#000000")
        self.root.Entry1.configure(selectbackground="#d9d9d9")
        self.root.Entry1.configure(selectforeground="black")

        # Configuração da Entrada de Texto 2
        self.root.Entry2 = tk.Entry(self.root)
        self.root.Entry2.place(relx=0.432, rely=0.474, height=20, relwidth=0.488)
        self.root.Entry2.configure(background="white")
        self.root.Entry2.configure(disabledforeground="#a3a3a3")
        self.root.Entry2.configure(font="-family {Courier New} -size 10")
        self.root.Entry2.configure(foreground="#000000")
        self.root.Entry2.configure(highlightbackground="#d9d9d9")
        self.root.Entry2.configure(highlightcolor="#000000")
        self.root.Entry2.configure(insertbackground="#000000")
        self.root.Entry2.configure(selectbackground="#d9d9d9")
        self.root.Entry2.configure(selectforeground="black")

        # Configuração do Botão de Escolha do Arquivo 1
        self.root.Button1 = tk.Button(self.root)
        self.root.Button1.place(relx=0.93, rely=0.211, height=26, width=27)
        self.root.Button1.configure(activebackground="#d9d9d9")
        self.root.Button1.configure(activeforeground="black")
        self.root.Button1.configure(background="#d9d9d9")
        self.root.Button1.configure(disabledforeground="#a3a3a3")
        self.root.Button1.configure(foreground="#000000")
        self.root.Button1.configure(highlightbackground="#d9d9d9")
        self.root.Button1.configure(highlightcolor="#000000")
        self.root.Button1.configure(text='''...''')
        self.root.Button1.configure(command=self.choose_file_1)

        # Configuração do Botão de Escolha do Arquivo 2
        self.root.Button2 = tk.Button(self.root)
        self.root.Button2.place(relx=0.93, rely=0.474, height=26, width=27)
        self.root.Button2.configure(activebackground="#d9d9d9")
        self.root.Button2.configure(activeforeground="black")
        self.root.Button2.configure(background="#d9d9d9")
        self.root.Button2.configure(cursor="fleur")
        self.root.Button2.configure(disabledforeground="#a3a3a3")
        self.root.Button2.configure(font="-family {Segoe UI} -size 9")
        self.root.Button2.configure(foreground="#000000")
        self.root.Button2.configure(highlightbackground="#d9d9d9")
        self.root.Button2.configure(highlightcolor="#000000")
        self.root.Button2.configure(text='''...''')
        self.root.Button2.configure(command=self.choose_file_2)

        # Configuração Geral dos Radio Buttons
        self.root.rdbtn = tk.IntVar()

        # Configuração do Radio Button 1
        self.root.Radiobutton1 = tk.Radiobutton(self.root)
        self.root.Radiobutton1.place(relx=0.017, rely=0.211, relheight=0.132, relwidth=0.256)
        self.root.Radiobutton1.configure(activebackground="#d9d9d9")
        self.root.Radiobutton1.configure(activeforeground="black")
        self.root.Radiobutton1.configure(anchor='w')
        self.root.Radiobutton1.configure(background="#d9d9d9")
        self.root.Radiobutton1.configure(compound='left')
        self.root.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.root.Radiobutton1.configure(font="-family {Segoe UI} -size 9")
        self.root.Radiobutton1.configure(foreground="#000000")
        self.root.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.root.Radiobutton1.configure(highlightcolor="#000000")
        self.root.Radiobutton1.configure(justify='left')
        self.root.Radiobutton1.configure(overrelief="groove")
        self.root.Radiobutton1.configure(text='''HB-JSON -> Python''')
        self.root.Radiobutton1.configure(underline="-100")
        self.root.Radiobutton1.configure(variable=self.root.rdbtn)
        self.root.Radiobutton1.configure(value=self.HB_TO_PY)
        self.root.Radiobutton1.configure(command=self.clear_entries)

        # Configuração do Radio Button 2
        self.root.Radiobutton2 = tk.Radiobutton(self.root)
        self.root.Radiobutton2.place(relx=0.017, rely=0.368, relheight=0.132, relwidth=0.322)
        self.root.Radiobutton2.configure(activebackground="#d9d9d9")
        self.root.Radiobutton2.configure(activeforeground="black")
        self.root.Radiobutton2.configure(anchor='w')
        self.root.Radiobutton2.configure(background="#d9d9d9")
        self.root.Radiobutton2.configure(compound='left')
        self.root.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.root.Radiobutton2.configure(font="-family {Segoe UI} -size 9")
        self.root.Radiobutton2.configure(foreground="#000000")
        self.root.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.root.Radiobutton2.configure(highlightcolor="#000000")
        self.root.Radiobutton2.configure(justify='left')
        self.root.Radiobutton2.configure(overrelief="groove")
        self.root.Radiobutton2.configure(text='''HB-JSON -> Jupyter Notebook''')
        self.root.Radiobutton2.configure(underline="-100")
        self.root.Radiobutton2.configure(variable=self.root.rdbtn)
        self.root.Radiobutton2.configure(value=self.HB_TO_IPYNB)
        self.root.Radiobutton2.configure(command=self.clear_entries)

        # Configuração do Radio Button 3
        self.root.Radiobutton3 = tk.Radiobutton(self.root)
        self.root.Radiobutton3.place(relx=0.017, rely=0.526, relheight=0.132, relwidth=0.322)
        self.root.Radiobutton3.configure(activebackground="#d9d9d9")
        self.root.Radiobutton3.configure(activeforeground="black")
        self.root.Radiobutton3.configure(anchor='w')
        self.root.Radiobutton3.configure(background="#d9d9d9")
        self.root.Radiobutton3.configure(compound='left')
        self.root.Radiobutton3.configure(disabledforeground="#a3a3a3")
        self.root.Radiobutton3.configure(font="-family {Segoe UI} -size 9")
        self.root.Radiobutton3.configure(foreground="#000000")
        self.root.Radiobutton3.configure(highlightbackground="#d9d9d9")
        self.root.Radiobutton3.configure(highlightcolor="#000000")
        self.root.Radiobutton3.configure(justify='left')
        self.root.Radiobutton3.configure(overrelief="groove")
        self.root.Radiobutton3.configure(text='''Jupyter Notebook -> HB-JSON''')
        self.root.Radiobutton3.configure(underline="-100")
        self.root.Radiobutton3.configure(variable=self.root.rdbtn)
        self.root.Radiobutton3.configure(value=self.IPYNB_TO_HB)
        self.root.Radiobutton3.configure(command=self.clear_entries)

        # Configuração da Label de Escolha do Arquivo 1
        self.root.TLabel1 = ttk.Label(self.root)
        self.root.TLabel1.place(relx=0.432, rely=0.105, height=17, width=158)
        self.root.TLabel1.configure(font="-family {Segoe UI} -size 9")
        self.root.TLabel1.configure(relief="flat")
        self.root.TLabel1.configure(anchor='w')
        self.root.TLabel1.configure(justify='left')
        self.root.TLabel1.configure(text='''Defina o arquivo de Origem''')
        self.root.TLabel1.configure(compound='left')

        # Configuração da Label de Escolha do Arquivo 2
        self.root.TLabel2 = ttk.Label(self.root)
        self.root.TLabel2.place(relx=0.432, rely=0.368, height=17, width=158)
        self.root.TLabel2.configure(font="-family {Segoe UI} -size 9")
        self.root.TLabel2.configure(relief="flat")
        self.root.TLabel2.configure(anchor='w')
        self.root.TLabel2.configure(justify='left')
        self.root.TLabel2.configure(text='''Defina o arquivo de Destino''')
        self.root.TLabel2.configure(compound='left')

        # Configuração do Botão Executar!
        self.Button3 = tk.Button(self.root)
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
            self.root.Button4 = tk.Button(self.root)
            self.root.Button4.place(relx=0.020, rely=0.737, height=26, width=120)
            self.root.Button4.configure(activebackground="#d9d9d9")
            self.root.Button4.configure(activeforeground="black")
            self.root.Button4.configure(background="#d9d9d9")
            self.root.Button4.configure(disabledforeground="#a3a3a3")
            self.root.Button4.configure(foreground="#000000")
            self.root.Button4.configure(highlightbackground="#d9d9d9")
            self.root.Button4.configure(highlightcolor="#000000")
            self.root.Button4.configure(text='''Variáveis''')
            self.root.Button4.configure(command=self.vars_window)

        self.root.mainloop()

    def vars_window(self):
        self.root2 = tk.Tk()

        # Configurações Principais
        self.root2.geometry("600x400")
        self.root2.minsize(120, 1)
        self.root2.maxsize(1370, 749)
        self.root2.resizable(1,  1)
        self.root2.title("Variáveis do D1")
        self.root2.configure(background="#d9d9d9")
        self.root2.configure(highlightbackground="#d9d9d9")
        self.root2.configure(highlightcolor="#000000")
        self.root2.iconbitmap(f"{self.root_dir}/img/quality.ico")
        self.root2.TSizegrip1 = ttk.Sizegrip(self.root2)
        self.root2.TSizegrip1.place(anchor='se', relx=1.0, rely=1.0)
        
        # Configurações do Frame
        self.root2.list_frame = tk.Frame(self.root2)
        self.root2.list_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Configurações da Tabela treeview
        self.root2.tree = ttk.Treeview(self.root2.list_frame, columns=('name', 'type', 'taskInputLabel', 'value'), show='headings')
        self.root2.tree.heading('name', text='Nome')
        self.root2.tree.heading('type', text='Tipo')
        self.root2.tree.heading('taskInputLabel', text='Label')
        self.root2.tree.heading('value', text='Valor')
        self.root2.tree.pack(fill=tk.BOTH, expand=True)

        # Configurações dos painel de botões
        self.root2.buttons_frame = tk.Frame(self.root2)
        self.root2.buttons_frame.pack(fill=tk.X, padx=5, pady=5)


if __name__ == "__main__":
    d1c = D1Converter(title="Ferramenta de Conversão do D1", experimental=False)
    d1c.main_window()