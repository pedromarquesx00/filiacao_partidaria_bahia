# Análise dos Números de Filiados - Bahia (2010 - 2024)
Esse projeto realiza uma análise exploratória e comparativa sobre a quantidade de filiados os maiores partidos da Bahia, cobrindo o intervalo de 14 anos. O objetivo é identificar as mudanças ao longo do tempo.

## Tecnologias Utilizadas
* *Python* (Linguagem Base)
* *Pandas* (Manipulação dos Dados)
* *Matplotlib/Seaborn* (Visualização dos Dados)

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

![Gráfico](../01_gráficos/filiados.png)

### Movimentações e Insights
Com o avanço dos anos, o gráfico revela três fenômenos políticos:
1. A ultrapassagem do PT (2020-2022): O PT apresentou uma curva inicial de aceleração (2010-2012) seguindo um crescimento orgânico e contínuo.Em contrapartida, o MDB, apesar de histórico, sofreu uma retração de aproximadamente 17% entre 2018-2022. Esse movimento colocou o PT em primeiro lugar.
2. A volatilidade do PSDB (2016-2018): O partido apresenta uma queda abrupta de -25,13%. O que pode indicar a sensibilidade do partido às janelas partidárias e aos reflexos do cenário político nacional da época na Bahia.
3. O efeito da fusão (DEM/UNIÃO): A junção entre o DEM e o PSL para criar o UNIÃO demonstra um poder imenso de capilaridade. O movimento gerou um aumento vertical de 105,47% na base de filiados da linha histórica, fazendo com que o DEM/UNIÃO saltasse para o segundo lugar geral.

Para validar matematicamente o ritmo dessas transformações, foi calculada a taxa de crescimento percentual período a período (YoY - Year over Year), conforme apresentado na tabela abaixo:

![Tabela de Crescimento](../01_gráficos/crescimento.png)

## Próximos passos
- [ ] Cruzar o volume de filiados ativos com o número real de prefeituras conquistadas por cada partido nas eleições de 2012, 2016, 2020 e 2024 para medir a eficiência de conversão (Filiados vs. Poder Local).
- [ ] Realizar o recorte demográfico de Gênero e Raça/Cor utilizando a técnica de Small Multiples (subgráficos em grade) para identificar qual partido possui a base mais diversa da Bahia.