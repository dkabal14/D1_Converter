import json
import os
import sys
import re


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

sample_file = f"{root_dir}\\smp\\sample_ipynb.json"

with open(input_file, 'r', encoding='utf-8') as jf:
    json_data = json.load(jf)

with open(sample_file, 'r', encoding='utf-8') as jf:
    sample_data = json.load(jf)


cells = json_data['nodes'][0]['config']['cells']
for cell in cells:
    markdown = False
    code = False
    input_lines = cell['input'].strip()

    print('')

    cell_sample = {
        "metadata": {},
        "source": []
    }

    # Split input_lines into lines to check the first line
    lines = input_lines.splitlines()
 
        
    if lines and re.match(r'^#\s*%%\s*\[markdown\]', lines[0]):
        cell_sample['cell_type'] = 'markdown'
        for line in lines[1:]:
            # Remove leading '#' and any whitespace
            cleaned_line = re.sub(r'^#\s*', '', line).strip()
            cell_sample['source'].append(cleaned_line + '\n')
    else:
        cell_sample['cell_type'] = 'code'
        for line in lines:
            # Add the line as is, without any modifications
            cell_sample['source'].append(line)

    print(cell_sample)
    # if not bool(input_lines):
    #     pass
    # elif len(input_lines) == 1:
    #     if '# %% [markdown]' in input_lines[0]:
    #         cell_sample["cell_type"] = "markdown"
    #     else:
    #         cell_sample["cell_type"] = "code"

    #     cell_sample["source"].append(input_lines[1])

    # elif len(input_lines) > 1:
    #     if '# %% [markdown]' in input_lines[0]:
    #         cell_sample["cell_type"] = "markdown"
    #         markdown = True
    #     else:
    #         cell_sample["cell_type"] = "code"
    #         code = True

    #     cnt = 0
    #     for input in input_lines:
    #         if cnt == 0:
    #             cnt += 1
    #             continue
    #         elif not cnt == len(input_lines):
    #             if markdown:
    #                 cell_sample["source"].append(f"{re.sub(r'^#\s*', '', input) if bool(re.search(r'#\s*', input)) else input}\n")
    #             else:
    #                 cell_sample["source"].append(f"{input}\n")
    #         else:
    #             if markdown:
    #                 cell_sample["source"].append(f"{re.sub(r'^#\s*', '', input) if bool(re.search(r'#\s*', input)) else input}\n")
    #             else:
    #                 cell_sample["source"].append(input)

    #         cnt += 1
    
    sample_data["cells"].append(cell_sample)
    # print(json.dumps(sample_data))
with open(output_file, 'w', encoding='utf-8') as of:
    of.write(json.dumps(sample_data))