# Trabalho prático - Aspectos Teóricos da Computação (DCC146)

#### Alunos: 
- Augusto Castilho  - 201876044
- Giovane Machado   - 201876019
- Matheus Rubio     - 201876036

## Executando a aplicação

A aplicação é desenvolvida na linguagem Python, e para realizar a sua execução é necessário possuir a versão 3.10 ou superior do python pois versões em versões abaixo desta a aplicação pode não funcionar corretamente.
> Caso tenha dificuldades em instalar ou alterar a versão do seu Python em ambiente linux, onde é ligeiramente mais complexo, sugerimos dois tutoriais que podem te ajudar:
>   - [Instalar gerenciador de versões do python (PYENV)](https://gist.github.com/luzfcb/ef29561ff81e81e348ab7d6824e14404)
>   - [Instalar o Python na versão 3.10](https://computingforgeeks.com/how-to-install-python-on-ubuntu-linux-system/)

Tendo seu ambiente configurado, basta ir na pasta raiz do projeto digitar o seguinte comando no seu terminal:

<p align=center>
  <b>python3 __init__.py</b><br>
  ou <br>
  <b>python3.10 __init__.py</b><br>
</p>

## Estruturas de dados
- MessageLogs

  Classe com todos os seus métodos estáticos, criada com o intuito de auxiliar no momento da impressão de mensagens [INFO], [WARNING], [ERROR] e [SUCCESS].
- Commands

  Classe também com todos os seus métodos estáticos, nela estão presentes os métodos responsáveis por cada comando existente no menu da aplicação, conforme orientado, comandos ainda não implementados estão com o aviso de que ainda não foram implementados.
- Tag

	Classe que contém as informações de uma tag a ser criada, somente com os campos “tagName” e “tagValue”, também possui um método estático utilizado para realizar a validação de uma tag informada pelo usuário.

- __init__.py

  Arquivo responsável pela execução de todo o código da aplicação, imprime um menu com os comandos disponíveis para serem utilizados, aguarda a resposta do usuário, verifica se é um comando ou a adição de uma tag válida, se for um comando válido, irá executar o comando especificado, se for uma tag válida, irá verificar se a tag já existe no array de tags e caso não tenha sido criada anteriormente durante a execução do código irá adicionar a tag especificada pelo usuário a lista de tags. O código após cada comando ou tag definida ainda continua em execução, enquanto não houver uma resposta do tipo “:q”, a execução dele não é interrompida.
