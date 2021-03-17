MORTY TEST
=======================

Introdução
------------
*  Aplicação da Lei de Benford para Análise de Casos de COVID-19 no Brasil. TCC - Engenharia de Computação - UEMA - 2020.2.

Estrutura:
-----------
* morty.py - Contém classe principal, Morty. E a classe de Test para Qui-Quadrado.
* test.ipynb - Contém os testes dos datasets pela benfordslaw

Tecnologias utilizadas:
-----------------------
Backend:
--------
 * Python 3.*

Library:
------------------------
 * pandas
 * numpy
 * matplotlib
 * seaborn
 * math
 * scipy.stats (chisquare)
 * benfordslaw

Para contribuir
----------------------------

    cd (Caminho do Diretório em que desejas clonar)
    git clone https://github.com/euclidesfreire/mortytest.git
    cd mortytest

Instalação:
-----------

* Passo 1: 
    - Instale as Bibliotecas Necessárias 

* Passo 2:
    - Criar pastas de "Resultados".
        Na pasta "mortytest", entre pelo terminal e execute o seguinte comando:
        (Lembre-se de ter permitido o arquivo ser executado)
        - ./make_build.sh 
* Passo 3: 
    - Abra o notebook "test", e execute todos os testes. 

Licenças e Citações:
---------------------
 *  Datasets
    - Brasil.io
        - A licença do código é [LGPL3] e dos dados convertidos Creative Commons Attribution ShareAlike. 
        * Fonte: Secretarias de Saúde das Unidades Federativas, dados tratados por Álvaro Justen e equipe de voluntários [Brasil.IO]
        * Brasil.IO: boletins epidemiológicos da COVID-19 por município por dia, disponível em: https://brasil.io/dataset/covid19/ (última atualização: 03 de 03 de 2021, acesso em 03 de 03 de 2021).


- "Morty Test - Testar o que trouxe morte, pela certeza que precisamos."

[Creative Commons Attribution ShareAlike]: https://creativecommons.org/licenses/by-sa/4.0/
[LGPL3]: https://www.gnu.org/licenses/lgpl-3.0.en.html
[Brasil.IO]: http://brasil.io/