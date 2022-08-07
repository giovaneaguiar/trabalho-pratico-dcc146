# Trabalho Prático - Aspectos Teóricos da Computação (DCC146)

#### Alunos: 
- Augusto Castilho  - 201876044
- Giovane Machado   - 201876019
- Matheus Rubio     - 201876036

## Executando a aplicação

A aplicação é desenvolvida na linguagem Python, e para realizar a sua execução é necessário possuir a versão 3.10 ou superior do Python pois versões em versões abaixo desta a aplicação pode não funcionar corretamente.
> Caso tenha dificuldades em instalar ou alterar a versão do seu Python em ambiente Linux, onde é ligeiramente mais complexo, sugerimos dois tutoriais que podem te ajudar:
>   - [Instalar gerenciador de versões do python (PYENV)](https://gist.github.com/luzfcb/ef29561ff81e81e348ab7d6824e14404)
>   - [Instalar o Python na versão 3.10](https://computingforgeeks.com/how-to-install-python-on-ubuntu-linux-system/)

Tendo seu ambiente configurado, basta ir na pasta raiz do projeto digitar o seguinte comando no seu terminal:

<p align=center>
  <b>python3 __init__.py</b>
  ,
  <b>python3.10 __init__.py</b>
	ou 
 <b>python __init__.py</b><br>
</p>

## Estruturas de dados

● init.py: arquivo principal utilizado para execução, responsável pela
entrada dos comandos.

● src: pasta onde fica os arquivos do projeto.

● Tag.py: arquivo responsável pela análise e controle das tag’s.

● Automaton.py: arquivo responsável pela estrutura do autômato.

● Converter.py: arquivo responsável pela criação e armazenamento dos autômatos.

● MessageLogs.py: arquivo para auxiliar mensagens como [INFO],
[WARNING], [ERROR] e [SUCCESS].

● Graph: pasta onde ficam os arquivos dos grafos.

● Edge.py: arquivo responsável pelo aresta do grafo (transição de um
estado).

● Node.py: arquivo responsável pelo nó do grafo (estado do autômato).

#### Ao executar, você terá as seguintes possibilidades:

• :d - realizar a divisão em tags da string do arquivo informado.

• :c - carregar um arquivo com definições de tags.

• :o - especificar o caminho do arquivo de saída para a divisão em tags.

• :p - realizar a divisão em tags da entrada informada.

• :a - listar as definições formais dos autômatos em memória.

• :l - listar as definições de tag válidas.

• :q - sair do programa.

• :s - salvar as tags.
