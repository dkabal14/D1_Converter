pyinstaller `
    --onefile `
    --add-data=.\src:.\src `
    --add-data=.\img:.\img `
    --icon=.\img\quality.ico `
    --collect-all=json `
    --collect-all=os `
    --collect-all=sys `
    --collect-all=re `
    --collect-all=uuid `
    --version-file=$PSScriptRoot\version.txt `
    --noconsole `
    --distpath d:\ `
    $PSScriptRoot\D1_PyTools_GUI.py