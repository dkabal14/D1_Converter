import json
import os
import sys


root_dir = os.path.abspath(
    os.path.dirname(__file__)
    )

usage_error = (f"O programa {__file__.split("\\")[-1]} deve ser executado da seguinte forma:\n\t>python.exe {__file__.split("\\")[-1]} <caminho para o arquivo .json> <caminho para o arquivo .ipynb>\nO programa aceita caminhos do Windows (Ex: c:\arquivo.json)")

try:
    input_file = sys.argv[1]
    input_file = input_file.replace("\\", "/")
except Exception as e:
    raise Exception(usage_error)

try:
    output_file = sys.argv[2]
    output_file = output_file.replace("\\", "/")
except Exception as e:
    raise Exception(usage_error)

with open(input_file, 'r', encoding='utf-8') as jf:
    jsonData = json.load(jf)

cells = jsonData['nodes'][0]['config']['cells']

with open(output_file, 'w', encoding='utf-8') as pyf:
    i = 1
    for cell in cells:
        pyf.write(f'\n# CÉLULA {i}:\n# {"="*80}\n')
        pyf.write(cell['input'].replace('\r', ''))
        pyf.write(f'\n# {"="*80}\n')
        i += 1