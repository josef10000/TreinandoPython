# Folder Organizer

Este é um script em Python para organizar automaticamente os arquivos em suas respectivas pastas com base em suas extensões. Ele organiza tanto a pasta de downloads quanto a área de trabalho (desktop).

## Como usar

1. Certifique-se de ter o Python instalado em seu sistema.

2. Baixe o arquivo `folder_organizer.py` neste repositório.

3. Abra um terminal ou prompt de comando e navegue até o diretório onde o arquivo `folder_organizer.py` foi baixado.

4. Execute o seguinte comando para iniciar a organização:

   ```shell
   python folder_organizer.py

   Certifique-se de ter as permissões necessárias para criar pastas e mover arquivos nas pastas de downloads e área de trabalho.

Observações
O script ignorará o próprio arquivo folder_organizer.py ao organizar os arquivos.

Os arquivos serão agrupados em pastas com base em suas extensões. Por exemplo, todos os arquivos com a extensão .pdf serão movidos para a pasta pdf, os arquivos com a extensão .jpg serão movidos para a pasta jpg, e assim por diante.

Certifique-se de revisar os arquivos antes de executar o script, pois ele moverá os arquivos para suas respectivas pastas automaticamente.

O script usa o módulo os e shutil do Python para realizar as operações de movimentação e criação de pastas.
