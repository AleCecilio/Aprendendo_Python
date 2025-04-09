#Desafio Operador logico
trabalho_terca = True
trabalho_quinta = False

'''
- Confirmando os 2: TV 50' + Sorvete
- Confirmando Apenas 1: TV 32' + Sorvete
-  Não Confirmando Nenhum: Volta Pra Casa 
'''

TVgrande_sorvete = trabalho_quinta and trabalho_terca
TVpequena_sorvete = trabalho_terca != trabalho_quinta
volta_casa = not trabalho_quinta and not trabalho_terca

if TVgrande_sorvete :
    print("TV 50' e Sorvete")
if TVpequena_sorvete :
    print("TV 32' e Sorvete")
if volta_casa:
    print("Volta para Casa")

'''
Metodo do Professor 

trabalho_terca = True
trabalho_quinta = False

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
mais_saldavel = not sorvete 

print ("TV50 = {} TV32 = {} Sorvete={} Salvavel = {}"
    .format(tv_50, tv_32, sorvete, mais_saudavel) )
'''
