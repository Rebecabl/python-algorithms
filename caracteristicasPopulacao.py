# Foi realizada uma pesquisa de algumas características físicas da população de uma certa região, a qual coletou os seguintes dados referentes a cada habitante para serem analisados:  
# - idade  
# - sexo (masculino e feminino)- cor dos olhos (azuis, verdes ou castanhos)- cor dos cabelos ( louros, castanhos, pretos)
# Faça um programa que determine e escreva:   
# - a maior idade dos habitantes- a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos (inclusive) e que tenham olhos verdes e cabelos louros.
# O programa deve encerrar a solicitação de dados dos habitantes quando o valor -1 for fornecido como idade.
# Grave um vídeo de no máximo dois minutos com você explicando o código escrito e anexe à atividade, junto com o código do programa


# Inicializa as variáveis para armazenar os dados
maior_idade = 0
qtde_mulheres = 0

# Solicita os dados dos habitantes até que seja inserido -1 como idade
while True:
    idade = int(input("Digite a idade do habitante (-1 para encerrar): "))
    
    if idade == -1:
        break
    
    sexo = input("Digite o sexo do habitante (M/F): ")
    cor_olhos = input("Digite a cor dos olhos do habitante (azuis, verdes ou castanhos): ")
    cor_cabelos = input("Digite a cor dos cabelos do habitante (louros, castanhos ou pretos): ")
    
    # Verifica se é a maior idade até agora
    if idade > maior_idade:
        maior_idade = idade
    
    # Verifica se é uma mulher entre 18 e 35 anos com olhos verdes e cabelos louros
    if sexo == "F" and 18 <= idade <= 35 and cor_olhos == "verdes" and cor_cabelos == "louros":
        qtde_mulheres += 1

# Imprime os resultados
print("A maior idade dos habitantes é: ", maior_idade)
print("A quantidade de mulheres entre 18 e 35 anos com olhos verdes e cabelos louros é: ", qtde_mulheres)
