import json
import os
import sys
import re
from uuid import uuid4


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

sample_file = f"{root_dir}\\smp\\sample_hb-json.json"

with open(input_file, 'r', encoding='utf-8') as jf:
    input_data = json.load(jf)

with open(sample_file, 'r', encoding='utf-8') as jf:
    result_json = json.load(jf)

result_json['nodes'][0]['id'] = str(uuid4())

for cell in input_data['cells']:
    dict_markdown = {}
    dict_markdown['id'] = str(uuid4())

    if cell['cell_type'] == 'markdown':

        output_text = ['# %% [markdown]\r\n'] + cell['source']
        output_text = "".join(output_text)
        dict_markdown['input'] = output_text

    elif cell['cell_type'] == 'code':

        output_text = ['# %%\r\n'] + [re.sub(r"\n$", r"\r\n", cell_source) for cell_source in cell['source']]
        output_text = "".join(output_text)
        dict_markdown['input'] = output_text
    
    result_json['nodes'][0]['config']['cells'].append(dict_markdown)

with open(output_file, 'w', encoding='utf-8') as output:
    output_data = json.dumps(result_json)
    output.write(output_data)