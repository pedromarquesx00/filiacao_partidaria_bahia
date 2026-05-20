# Análise dos Números de Filiados - Bahia (2010 - 2024)
Esse projeto realiza uma análise exploratória e comparativa sobre a quantiade de filiados os maiores partidos da Bahia, cobrindo o intervalo de 14 anos. O objetivo é identificar as mudanças ao longo do tempo.

## Tecnologias Utilizadas
- *Python* (Linguagem Base)
- *Pandas* (Manipulação dos Dados)
- *Matplotlib/Seaborn* (Visualização dos Dados)

## Passo a Passo
1. Os dados brutos foram obtidos no Portal de Dados Abertos do TSE:[link:https://sig.tse.jus.br/ords/dwapr/r/seai/sig-eleicao-arquivo/conjuntos-de-dados?p10_cd_modulo=filiado_eleicao&cs=1AvODvRYvAl9WLdWMM5lkNs0f7zwonHnpkVLysn_bqHSnPn-w8VV7MeDIPpM-yUarH_o0YNg74frRdUaCm2wALQ].
2. Baixe os dados de filiação de 2010 a 2024 (Filiados da eleição).
3. Salve os arquivos em uma pasta data/ no seu ambiente local.
4. Certifique-se de baixar as dependências necessárias:
```bash
pip install pandas seaborn matplotlib
```

## Análise dos Dados
### Série Histórica
Com os dados levantados, nota-se o comportamento da população em relação a filiação partidária.
Com os 5 maiores partidos, no início da série, em 2010, tem-se a seguinte organização:
1º MDB
2º PT
3º PP
4º PSDB
5º DEM/UNIÃO*

*Nota: Para realizar essa comparação, os dados do partido DEM e UNINÃO foram colocados juntos, pois o partdo UNIÃO nasce da união do DEM com PSL. Para fins de análise, foi adotado essa união.*

Gráfico ![link:../01_gráficos/filiados.png]

Com o passar do tempo, percebe-se um movimento de filiados. O ponto crítico que salta aos olhos é o comportamento de 2018 a 2022.

Por uma análise estatística, conforme na tabela abaixo, nota-se o que os

Tabela ![link:../01_gráficos/crescimento.png]