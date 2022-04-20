# PySpec

Projeto desenvolvido por Guilherme Rabelo para o Trabalho de Conclusão de Curso de Química - Atribuições Tecnológicas em 2018

O trabalho consistia em construir um espectrofotômetro de mesa para laboratórios, utilizando materiais de baixo custo, impressão 3D e programação em Python para o seu desenvolvimento.


O programa Spec.py serve como controlador do aparelho. Atuando para capturar imagens com uma webcam e processá-las, convertendo as imagens em um gráfico de intensidade luminosa por comprimento de onda.


O programa consiste de 4 funções:
  - main(): Função principal, responsável por "guiar" a aplicação.
  - Captura_Imagem(): Função responsável por acessar a webcam e capturar uma foto.
  - Medida(): Função responsável por pelo primeiro tratamento das imagens capturadas, incluindo o recorte da área de interesse e armazenamento da imagem capturada no disco.
  - Img_para_Espectro(): Função responsável por converter os dados da imagem capturada em duas listas de dados, contendo os valores de comprimento de onda e de intensidade luminosa.


Os valores absolutos contidos no programa foram obtidos por calibrações realizadas no período do projeto.

No arquivo "Trabalho de Conclusão de Curso.pdf" estão mais detalhes sobre o projeto realizado.
