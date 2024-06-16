# TextFusion
## Scripts de extração de texto de pdf e docx e de divisião de arquivo

O programa 'extrator.py' percorre o diretório alvo e extrai o texto de arquivos pdf e docx que forem encontrados, reunindo-os num único documento txt ('output.txt').

O programa 'split_text_file.py' divide o arquivo 'output.txt' gerado com o script anterior em quantos arquivos forem necessários para que cada um tenha até 400.000 palavras. O objetivo é que esses arquivos possam alimentar ferramentas como o NotebookLM do Google.