'''
- Imprimir a lista de unidades de conversão
- Solicitar o valor que se deseja converter usando a frase “Valor a ser convertido: ”
- Solicitar a unidade origem do valor usando a frase “Converter de: ”
- Solicitar a unidade destino de conversão usando a frase “Converter para: ”
- Exibir o valor convertido com a frase “Conversão: {valor} {unidade origem} = {valor}
{unidade destino}”
'''

ano_luz = {'pc': 0.31, 'al': 1, 'ae': 63241.09, 'ml': 525960.23, 'sl': 31557609.92}
unidades = {
    'Parsec': ['pc'],
    'Ano-luz': ['al'],
    'Unidade Astronômica': ['ae'],
    'Minuto-Luz(ml)': ['ml'],
    'Segundo-Luz': ['sl']
}

print('-------- Unidades possíveis para Conversão --------')
for unidade, num in unidades.items():
    print(f'{unidade}')

valor = int(input("Valor a ser Convertido: "))
print("-- Para conversão use o nome das Unidades. --")
conv_de = input("Converter de: ")
conv_para = input("Converter para: ")