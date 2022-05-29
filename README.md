# Multi files request
[![license mit](https://img.shields.io/badge/license-MIT-green)](LICENSE.md)<br>

## PT-BR<br>

Este script envia um ou mais arquivos para determinada API e armazena suas respostas em um arquivo de texto.<br>

As linhas 90 e 123 devem ser alteradas de acordo com o padrão da resposta<br>

### Importações necessárias<br>

Utilize 'pip install -r requirements.txt' para instalar todas as dependências.<br>

### Utilização<br>
Após instalar as dependências do arquivo requirements.txt iniciamos o main.py<br>
O programa irá perguntar se desejamos enviar apenas um arquivo (opção 1) ou se desejamos enviar todos os arquivos que estão dentro de uma pasta (que deve estar no mesmo diretório do arquivo main.py) (opção 2)<br>
* Caso a opção 1 for selecionada, digitamos o nome do arquivo a ser enviado Ex. **./documento1.pdf**<br>
* Caso a opção 2 for selecionada, digitamos o nome da pasta que contém todos os arquivos que serão enviados Ex. **./nomeDaMinhaPasta**<br>

Em seguida o programa irá perguntar qual a **URL**, que é para onde a requisição será enviada.<br>
O programa criará uma pasta chamada **RESPONSES**, e é lá que as respectivas respostas serão armazenadas em formato txt.<br>
Obs. caso já exista um arquivo com o mesmo nome na pasta **RESPONSES** o programa irá ignorar este arquivo, ou seja, se ocorrer erro em um dos arquivos basta iniciar o processo novamente já que o programa ignora os arquivos que já foram enviados (comparando pelo nome respectivo na pasta **responses**)<br>

#### Automação<br>
Para deixar o código ainda mais automático, podemos alterar as linhas **73** e **104** e comentar as linhas **74** e **105** para salvar a **URL** dentro do código e evitar de ter que ficar digitando todas as vezes.<br>Podemos também dizer ao código sempre o que fazer quanto a enviar um arquivo ou uma pasta.<br>


### Dúvidas<br>

Qualquer dúvida ou erro **[entre em contato comigo](https://www.instagram.com/mts.e/)** ou **[reporte um problema](https://github.com/euMts/multifiles_request/issues)** aqui no github.<br>

Ultima atualização: 25/04/2022<br>