# noise-and-filters

Atividade da matéria de computação gráfica para o experimento de filtros e ruídos.

## Sobre

### Noises
Ruídos ou noises, são pixeis brancos, pretos ou em escala de cinza que podem ser encontrados em determinadas imagens.

#### White
No processamento digital de imagem, os pixels de uma imagem de ruído branco são dispostos tipicamente em uma grade retangular e assumidos como variáveis aleatórias independentes com distribuição de probabilidade uniforme ao longo de algum intervalo.

#### Salt and Pepper
O ruído de sal e pimenta é uma forma de ruído às vezes vista nas imagens. Também é conhecido como ruído de impulso. Esse ruído pode ser causado por distúrbios agudos e repentinos no sinal da imagem. Apresenta-se como pixels brancos e pretos de ocorrência esparsa.

#### Gaussian
Um filtro gaussiano é utilizado para borrar ou desfocar a imagem na qual ele é aplicado com o objetivo de reduzir os ruídos presentes na imagem. O resultado desta operação é a suavização da imagem.

### Filters
Existem filtros lineares, que suavizam e realçam detalhes da imagem e minimizam efeitos de ruído, sem alterar a média da imagem.
E existem os filtros não lineares que Minimizam/realçam ruídos e suavizam/realçam bordas, alterando a média da imagem, sendo os principais os operadores para detecção de bordas e os filtros morfológicos.

#### Passa-Baixa (Linear)
Suaviza a imagem atenuando as altas freqüências, que correspondem às transições abruptas. Tende a minimizar ruídos e apresenta o efeito de borramento da imagem.

#### Passa-Alta (Linear)
A filtragem passa-alta realça detalhes, produzindo uma "agudização" ("sharpering") da imagem, isto é, as transições entre regiões diferentes tornam-se mais nítidas. Estes filtros podem ser usados para realçar certas características presentes na imagem, tais como bordas, linhas curvas ou manchas.

#### Sobel (Não Linear)
Realça linhas verticais e horizontais mais escuras que o fundo, sem realçar pontos isolados. 

## Tecnologias Utilizadas

Para a implementação deste código fonte foi utilizada a linguagem de programação Python3 junto das bibliotecas Numpy, e Matplotlib. Isso através do AnacondaPrompt.

Numpy doc: [a link] https://docs.scipy.org/doc/numpy/dev/ <br/>
Matplotlib doc: [a link] https://matplotlib.org/api/pyplot_api.html
 

