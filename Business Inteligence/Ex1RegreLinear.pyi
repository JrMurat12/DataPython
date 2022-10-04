import pandas as pd
peso = [720,720,720,730,730,740,740,740,750,750,750,750,760,760,760,770,770,780,780,780,780,790,790,790]
velocidade = [257,263,266,269,271,275,274,278,278,275,280,284,281,286,289,293,297,295,299,299,301,296,303,308]

dados = pd.DataFrame(zip(peso, velocidade), columns=['peso','velocidade'])
print(dados)