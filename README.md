# MolecHex

Pequeno programa que gera Hexagonos como da imagem abaixo, inspirado nas ideias de @JosuéLucas. Feito com Python v3.7 e PyGame v2.0.0.
![Hexagon generated by an 11x11 matrix](https://github.com/ffernandoalves/MolecHex/blob/master/image/matriz11x11.png)

O programa aceita somente matriz de ordem ímpares quadraticas: 3x3, 5x5...

Na função `main()`:
```
start = Start(env_color, dic_color, SCREEN, size_matriz=11,
    organism_img=(False, organism_img, (40, 40)), hexagonal_shape=True,
    complete_matrix=False,
    matrix_shape=[None, #'rectangular' / 'square'
                (13, 16)])
```
Em `size_matriz` é onde decide a ordem da matriz, por exemplo, a ordem padrão é 11x11. Gera uma matriz (lista) com 121 elementos e de cada linha de índice par vai sendo retirado elementos e movimentado metade da largura da forma geometrica, para assumir o formato de hexagono.

É usado a biblioteca **PyGame** para criar os hexaganos (como também os quadrados se escolher) e a barra de informações na tela.
Onde cada hexagono é chamado de particula e o player é o organismo.

Depois de baixado, execute:
```
pip3.7 install -r requirements.txt
python3.7 main.py
```

ps: movimentos do organismo bugado
