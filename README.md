# DONE_PYTOOLS


## O que é?

**DONE_PYTOOLS** é uma ferramenta desenvolvida para auxiliar na conversão entre **robôs Python da plataforma D1** e scripts Python convencionais (formato `.ipynb` ou `.py`).

## Como funciona a conversão?

Ao exportar um robô Python da plataforma D1, o arquivo gerado é um `.json`. Para facilitar o desenvolvimento, testes e leitura, esse arquivo precisa ser convertido para o formato `.ipynb` (Jupyter Notebook), que também é um `.json`, porém com estrutura distinta.

O processo reverso também é possível: converter de `.ipynb` para o formato compatível com a D1.

## Suporte

Em caso de dúvidas, entre em contato pelo e-mail:

📧 **diego.sousa@quality.com.br**

Responderemos o mais breve possível.

### Disclaimer
A conversão não abrange as variáveis (parâmetros) do robô Python, sendo necessária a declaração manual.


# Bibliotecas presentes no D1


<table id="21fb8813-98f7-80eb-829f-f0a983c2c887" class="simple-table">
    <thead class="simple-table-header">
        <tr id="21fb8813-98f7-802c-a905-c6cc7eefcb5d">
            <th id="FBbk" class="simple-table-header-color simple-table-header">Categoria</th>
            <th id="N?kk" class="simple-table-header-color simple-table-header" style="width:726px">Pacotes</th>
        </tr>
    </thead>
    <tbody>
        <tr id="21fb8813-98f7-8054-bfd2-d3790e6e4b56">
            <th id="FBbk" class="simple-table-header-color simple-table-header">Core Infra</th>
            <td id="N?kk" class="" style="width:726px"><code>pip</code>,
                    <code>setuptools</code> , 
                    <code>wheel</code></mark></td>
        </tr>
        <tr id="21fb8813-98f7-807e-87cc-db40342885f7">
            <th id="FBbk" class="simple-table-header-color simple-table-header">Manipulação de Dados</th>
            <td id="N?kk" class="" style="width:726px"><code>pandas</code>
                    <code>numpy</code>
                    <code>openpyxl</code>
                    , 
                    <code>python-dateutil</code> ,
                 <code>pytz</code> , 
                    <code>tzdata</code> , 
                    <code>et_xmlfile</code></mark></td>
        </tr>
        <tr id="21fb8813-98f7-809d-b4dd-fc52b16fc73c">
            <th id="FBbk" class="simple-table-header-color simple-table-header">Web e API Clients</th>
            <td id="N?kk" class="" style="width:726px"><code>requests</code>
                    <code>requests-file</code>
                    , 
                    <code>requests-oauthlib</code> ,
                 <code>requests-toolbelt</code> ,
                 <code>simple-salesforce</code> ,
                 <code>boxsdk</code> ,
                 <code>zeep</code> , 
                    <code>jira</code> , 
                    <code>oauthlib</code> , 
                    <code>isodate</code></mark></td>
        </tr>
        <tr id="21fb8813-98f7-8048-b092-fd15c1f418f1">
            <th id="FBbk" class="simple-table-header-color simple-table-header">Segurança / Criptografia</th>
            <td id="N?kk" class="" style="width:726px">
                    <code>cryptography</code> , 
                    <code>pycparser</code> , 
                    <code>cffi</code> , 
                    <code>PyJWT</code></mark></td>
        </tr>
        <tr id="21fb8813-98f7-80ec-ad1b-f8e72a4f9fc6">
            <th id="FBbk" class="simple-table-header-color simple-table-header">Parsing / Compatibilidade</th>
            <td id="N?kk" class="" style="width:726px"><code>attrs</code>
                    , 
                    <code>charset-normalizer</code> ,
                 <code>idna</code> , 
                    <code>six</code> , 
                    <code>packaging</code> , 
                    <code>typing_extensions</code> ,
                 <code>hcl</code></mark></td>
        </tr>
        <tr id="21fb8813-98f7-80b1-9afc-cc0066ea6566">
            <th id="FBbk" class="simple-table-header-color simple-table-header">Dev Tools / IDE</th>
            <td id="N?kk" class="" style="width:726px"><code>ipython</code>,<code>ipykernel</code>,
                <code>jupyter_client</code>
                <code>jupyter_core</code>
                <code>debugpy</code>
                <code>traitlets</code>
                <code>parso</code>
                <code>jedi</code>
                <code>nest-asyncio</code>
                <code>pexpect</code>
                <code>ptyprocess</code>
                <code>prompt_toolkit</code>
                <code>platformdirs</code>
                <code>decorator</code>
                <code>comm</code>
                <code>stack-data</code>
                <code>pure_eval</code>
                <code>asttokens</code>
                <code>executing</code></td>
        </tr>
        <tr id="21fb8813-98f7-8085-b026-ca6f2cd7cab4">
            <th id="FBbk" class="simple-table-header-color simple-table-header">Gráficos e Visualização</th>
            <td id="N?kk" class="" style="width:726px"><code>pillow</code>
                    <code>Pygments</code>
                    , 
                    <code>matplotlib-inline</code> ,
                 <code>ipython_pygments_lexers</code></mark></td>
        </tr>
        <tr id="21fb8813-98f7-80cf-851a-edc2bdb5e82d">
            <th id="FBbk" class="simple-table-header-color simple-table-header">Web Templating</th>
            <td id="N?kk" class="" style="width:726px"><code>Jinja2</code>
                    <code>MarkupSafe</code></mark></td>
        </tr>
        <tr id="21fb8813-98f7-80d7-8ede-cf5296c62778">
            <th id="FBbk" class="simple-table-header-color simple-table-header">Outros</th>
            <td id="N?kk" class="" style="width:726px"><code>psutil</code>
                    <code>tornado</code>
                    <code>more-itertools</code>
                    <code>pendulum</code>
                    <code>lxml</code>
                    <code>defusedxml</code>
                    <code>wcwidth</code></mark></td>
        </tr>
    </tbody>
</table>


## Boas práticas


### Verificação do ambiente


```py 
try:
    hcl.system_variable["organization_id"]
    LOCAL = False
except:
    LOCAL = True
```


Esse código detecta se o script está rodando localmente ou na nuvem Highbound. Ele tenta acessar uma variável do `hcl`, que só existe nos robôs Highbound. Se der erro, define `LOCAL = True`, indicando que está fora da nuvem. Isso permite adaptar o comportamento do código conforme o ambiente.


### Importação de arquivos


A importação é simples: basta utilizar `hcl.load_working_file()` quando não estiver em ambiente local, seguido da importação convencional.


```py
import pandas as pd

if not LOCAL:
    hcl.load_working_file("requirements.txt")
    hcl.load_working_file("RazaoContabil.xlsx")
    hcl.load_working_file("LancamentosContabeis.xlsx")
    hcl.load_working_file("PlanoDeContas.xlsx")

df_RazaoContabil = pd.read_excel("RazaoContabil", sheet_name="Plan1")
df_LancamentosContabeis = pd.read_excel("LancamentosContabeis", sheet_name="Plan1")
df_PlanoDeContas = pd.read_excel("PlanoDeContas", sheet_name="Plan1")
```


### Importação de bibliotecas

Se não estiver em ambiente local, há duas abordagens viáveis: a primeira é instalar os pacotes diretamente via uma lista no próprio código, usando `subprocess` com `pip install`. Essa abordagem é útil para scripts simples ou dinâmicos, mas pouco escalável. A segunda é mais adequada para projetos maiores, usar um `requirements.txt` e instalar todas as dependências com `pip install -r requirements.txt`.


1. Primeira abordagem - Hardcoding


```py
if not LOCAL:
    import subprocess
    import sys

    modulos = ["scikit_learn"]
    subprocess.check_call([sys.executable, "-m", "pip", "install", *modulos])

    #Adicionar todos módulos manualmente
    import sklearn

```
2. Segunda abordagem - requirements.txt


```py
if not LOCAL:
    import subprocess
    import sys

    hcl.load_working_file("requirements.txt")
    subprocess.check_call([sys.executable, "-r", "pip", "install", "-r", "requirements.txt"])

    #Adicionar todos módulos manualmente
    import sklearn
```
