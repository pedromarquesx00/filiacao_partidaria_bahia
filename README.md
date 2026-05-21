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
1. MDB (Líder absoluto, próximo a marca de 95.000 filiados)
2. PT (Segundo lugar, na casa dos 72.000 filiados)
3. PP (Terceira força, estável perto dos 68.000 filiados)
4. PSDB (Quarta força, por volta de 58.000 filiados)
5. DEM/UNIÃO* (Quinta força, fechando o grupo dos grandes)

*Note: Para garantir a consistência e a integridade histórica da análise, os dados das siglas DEM e UNIÃO foram consolidados em uma única linha de tendência. Como o partido União Brasil nasceu da fusão do DEM com o PSL em 2022, essa unificação metodológica foi adotada para refletir a continuidade de sua base estrutural.*

Gráfico ![link:../01_gráficos/filiados.png]
### Movimentações e Insights
Com o avanço dos anos, o gráfico revela três fenômenos políticos:
1. A ultrapassem do PT (2020-2022): Ao longo do tempo, o PT mantinha uma curva de crescimento com um pico de 2010 para 2012, e manteve um crescimento orgânico do longo do tempo. o MDB tem certa estabilidade, entretanto, de 2018 até 2022, somam uma queda de aproximadamente 17%, colocando o PT em primeiro lugar.
2. A volatilidade do PSDB (2016-2018): O partido apresenta uma queda abrupa de -25,13%. O que pode indicar a sensibilidade do partido às janelas partidárias e ao cenário político nacional da época refletida no estado baiano.
3. O efeito da fusão: Com a junção entre o partido DEM e PSL para criar o UNIÃO, nota-se a popularidade e capilaridade da junção partidária. Com um aumento de 105,47%, DEM/UNIÃO ocupa o segudo lugar de partidos com mais filiados.

Para validar matematicamente o ritmo dessas transformações, foi calculada a taxa de crescimento percentual período a período (YoY - Year over Year), conforme apresentado na tabela abaixo:
Tabela ![link:../01_gráficos/crescimento.png]

### Hipóteses
