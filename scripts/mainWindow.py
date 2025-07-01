from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt6 import uic
import subprocess
import varWindow
import sys
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.root_dir = os.path.dirname(os.path.abspath(__file__)).replace('\scripts','')

        # Carrega tela principal
        uic.loadUi("ui/mainWindow.ui", self)
        
        # Set a versão no nome da tela
        window_name = self.windowTitle()
        self.setWindowTitle(window_name + 'v0.0.5')

        self.btn_vars.clicked.connect(self.open_var_window)
        
        self.btn_origem.clicked.connect(self.choose_file_1)
        self.btn_destino.clicked.connect(self.choose_file_2)
        
        self.btn_run.clicked.connect(self.run_conversion)

    def open_var_window(self):
        popup = varWindow.VarWindow()
        popup.exec() 
        
    def verify_groupbutton(self) -> str:
        """
        Verifica se algum button está marcado, retorna ele ou um erro.
        """
        if self.radioButton_1.isChecked():
            selected_button = 1
        elif self.radioButton_2.isChecked():
            selected_button = 2
        elif self.radioButton_3.isChecked():
            selected_button = 3
        else:
            raise Exception('É necessário escolher um tipo de conversão!')
        
        return selected_button
    
    def to_path_linux(self, path) -> str:
        """
        Converte o caminho do arquivo para o formato Linux.
        """
        return path.replace("\\", "/")
    
    def to_path_windows(self, path) -> str:
        """
        Converte o caminho do arquivo para o formato Windows.
        """
        return path.replace("/", "\\")
        
    def choose_file_1(self):
        try:
            selected_button = self.verify_groupbutton()
            
            if selected_button == 1:
                file_type = 'Arquivo de um Robô (*.json)'
            elif selected_button == 2:
                file_type = 'Arquivo de um Robô (*.json)'
            elif selected_button == 3:
                file_type = 'IPython Jupyter Notebook (*.ipynb)'

            init_dir = os.environ.get('USERPROFILE', os.getcwd())
            init_file = ""

            if self.Entry1.text():
                init_dir = os.path.dirname(self.Entry1.text())
                init_file = os.path.basename(self.Entry1.text()).rsplit(".", 1)[0]

            file_name, _ = QFileDialog.getOpenFileName(
                self,
                "Escolha o arquivo de entrada",
                os.path.join(init_dir, init_file),
                file_type
            )

            if file_name:
                self.Entry1.setText(self.to_path_windows(file_name))

        except Exception as e:
            QMessageBox.warning(self, "Atenção!", str(e))


    def choose_file_2(self):
        try:
            selected_button = self.verify_groupbutton()
            
            if selected_button == 1:
                file_type = 'Script Python (*.py)'
            elif selected_button == 2:
                file_type = 'IPython Jupyter Notebook (*.ipynb)'
            elif selected_button == 3:
                file_type = 'Robô Highbond (*.json)'

            init_dir = os.environ.get('USERPROFILE', os.getcwd())
            init_file = ""

            if self.Entry1.text():
                init_dir = os.path.dirname(self.Entry1.text())
                init_file = os.path.basename(self.Entry1.text()).rsplit(".", 1)[0]

            file_name, _ = QFileDialog.getSaveFileName(
                self,
                "Salvar como",
                os.path.join(init_dir, init_file),
                file_type
            )

            if file_name:
                self.Entry2.setText(self.to_path_windows(file_name))

        except Exception as e:
            QMessageBox.warning(self, "Atenção!", str(e))
            
    def clear_entries(self):
        self.Entry1.setText('')
        self.Entry2.setText('')
        
    def run_conversion(self):
        try:
            i_file = self.to_path_linux(self.Entry1.text())
            o_file = self.to_path_linux(self.Entry2.text())

            if not bool(i_file) and not bool(o_file):
                raise Exception("Os arquivos de origem e destino precisam estar preenchidos!")
            elif not bool(i_file):
                raise Exception("O arquivo de origem precisa estar preenchido!")
            elif not bool(o_file):
                raise Exception("O arquivo de destino precisa estar preenchido!")
            
            if self.radioButton_1.isChecked():
                run1 = subprocess.run(['python.exe', f"{self.root_dir}/src/hb-json_to_py.py", i_file, o_file], capture_output=True, check=False)
                if run1.returncode != 0:
                    raise Exception(f"Falha na execução com o código {run1.returncode}: {run1.stderr}")
                else:
                    QMessageBox.information(self, 'Sucesso', f'Arquivo "{o_file}" criado com sucesso!')

            elif self.radioButton_2.isChecked():
                run2 = subprocess.run(['python.exe', f"{self.root_dir}/src/hb-json_to_ipynb.py", i_file, o_file], capture_output=True, check=False)
                if run2.returncode != 0:
                    raise Exception(f"Falha na execução com o código {run2.returncode}: {run2.stderr}")
                else:
                    QMessageBox.information(self, 'Sucesso', f'Arquivo "{o_file}" criado com sucesso!')

            elif self.radioButton_3.isChecked():
                run3 = subprocess.run(['python.exe', f"{self.root_dir}/src/ipynb_to_hb-json.py", i_file, o_file], capture_output=True, check=False)
                if run3.returncode != 0:
                    raise Exception(f"Falha na execução com o código {run3.returncode}: {run3.stderr}")
                else:
                    QMessageBox.information(self, 'Sucesso', f'Arquivo "{o_file}" criado com sucesso!')
            else:
                raise Exception("É necessário escolher um tipo de conversão!")

        except Exception as e:
            QMessageBox.warning(self, "Atenção", str(e))
            
            
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())