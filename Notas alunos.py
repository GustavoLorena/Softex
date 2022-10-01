import pandas as pd

tabela_df = pd.read_csv(r'C:\Users\PC\Documents\Softex\notas_alunos.csv', sep=',')

tabela_df['Media'] = (tabela_df['Nota_1'] + tabela_df['Nota_2']) / 2
tabela_df['Situação'] = "Pendente"
tabela_df.loc[(tabela_df["Media"] < 7) | (
    tabela_df['Faltas'] > 5), 'Situação'] = 'Reprovado'
tabela_df.loc[(tabela_df["Media"] >= 7) & (
    tabela_df['Faltas'] <= 5), 'Situação'] = 'Aprovado'

print(tabela_df.head(5))

tabela_df.to_csv("alunos_situacao.csv")
print(tabela_df)

mediaTurma = tabela_df['Media'].median()
print("A media geral da turma foi: ", mediaTurma)
maiormedia = tabela_df['Media'].max()
print("A maior media da turma foi: ", maiormedia)
maisfaltas = tabela_df['Faltas'].max()
print("Maior numero de faltas: ", maisfaltas)
