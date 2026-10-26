# Relatório — Gabryel Rodrigues Ferreira (3547)

Relatório do projeto, preenchido na sua branch. Cada marco acrescenta a sua seção. Responda com as suas palavras e com
os números da sua execução; cada resposta cabe em até 6 linhas, além das tabelas.

## Marco 1

### Ambiente

~/venvs/prog2-venv/bin/python
=== Etapa 0: ambiente ===
Python 3.14.7 | NumPy 2.5.4 | fornecido 3.0


### R1 — Expressões regulares

<!-- Uma string que re.match aceita e re.fullmatch rejeita com o padrão de tag; consequência para valida_tag. -->

### R2 — Linhas inválidas

<!-- Por que ler_log devolve as linhas descartadas; uma situação real em que descartar em silêncio esconderia um problema. -->

### R3 — Late binding

<!-- Por que errados["PT102"](4095) dá 409,5 e por que a sua criar_conversores não tem o problema. -->

### R4 — Escala nominal

<!-- Hipótese para a diferença da Etapa 2(f) e onde, no código da base, está a explicação. -->

### R5 — Previsão × medição (Etapa 3)

Previsões registradas no commit: <!-- cole o hash curto do commit de previsões -->

| Grandeza | Previsão | Medido |
| --- | --- | --- |
| Memória da lista / memória do `uint16` | A lista vai ocupar mais memória que o array uint16.| |
| Tempo do laço / tempo vetorizado |Espero que a vetorização seja mais rápida em muitos casos. | |
| Tempo da compreensão / tempo do laço | Acho que a compreensão será muito mais rápida do que laço. | |

<!-- Explique a maior diferença entre previsão e medição; por que uint16 * 20 dá 16364; que dtype você escolheria para contagens e para kPa. -->

### R6 — Tipos da SerieTemporal (Etapa 4d)

| Expressão | Tipo previsto | Tipo observado |
| --- | --- | --- |
| `s + s` |SerieTemporal| |
| `s[1:]` |SerieTemporal| |
| `s * 2` |SerieTemporal| |
| `s.sum()` |Float| |
| `s[0]` |Float| |

<!-- Explique o resultado que mais surpreendeu você. -->

### R7 — Issue #4
O sintoma é que a media movel retorna 570 invés de 571.
O teste de regressão (test_media_move) avalia se a função retorna a quantidade correta.
A causa foi que uso de acumulada[janela:] descartava um valor da soma acumulada, reduzindo em um a quantidade de resultados. Além disso, a primeira janela precisa ser tratada separadamente, pois não existe uma soma anterior a subtrair.
Para corrigir isso utilizei acumulada[janela - 1:].copy() e subtraí as somas acumuladas anteriores apenas das posições seguintes. A solução não utiliza laços, não modifica a série original e retorna uma SerieTemporal.