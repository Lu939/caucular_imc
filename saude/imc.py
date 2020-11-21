pessoa = dict()
numero_pessoas = abaixo_peso = normal = sobrepeso = obesidade = obesidade_grave = 0
while True:
    pessoa['nome'] = str(input('Digite o nome:')).strip().upper()
    numero_pessoas += 1
    pessoa['peso'] = float(input('Digite o peso:'))
    pessoa['altura'] = float(input('Digite a altura'))
    pessoa['imc'] = pessoa['peso']/(pessoa['altura'] * 2)
    if pessoa['imc'] < 18.5:
        pessoa['situacao'] = 'Abaixo do peso'
        abaixo_peso += 1
    elif 18.5 <= pessoa['imc'] <= 24.9:
        pessoa['situacao'] = 'Normal'
        normal += 1
    elif 25 <= pessoa['imc'] <= 29.9:
        pessoa['situacao'] = 'Sobrepeso'
        sobrepeso += 1
    elif 30.0 <= pessoa['imc'] <= 39.9:
        pessoa['situacao'] = 'Obesidade'
        obesidade += 1
    elif pessoa['imc'] >= 40:
        pessoa['situacao'] = 'Obesidade grave'
        obesidade_grave += 1
    for c, v in pessoa.items():
        print(f'{c} => {v}')
    resp = str(input('Continuar sim ou não [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Foram avaliadas {numero_pessoas} pessoas\n {abaixo_peso} estão abaixo do peso\n {normal} estão normais')
print(f'{sobrepeso} estão com sobrepeso\n {obesidade} estão obesas\n {obesidade_grave} estão com obesidade grave')