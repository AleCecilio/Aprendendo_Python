'''
Exercício 10: Jogo de Perguntas
 Crie um quiz com perguntas, alternativas e resposta correta de um arquivo JSON.
 Mostre no terminal.
 Calcule o score.
 Use comprehension e funções.
'''

import json
import sys
import time

# --- Verificar Se a String Não está Vazia ---
def verificar_String(prompt):
    while True:
        string = input(prompt).strip().upper()
        if string == "":
            print('O campo não pode estar vazio!!!')
            continue

        if string in {'A','B','C','D'}:
            return string
        
        print('Digite Uma Alternativa Válida!!!')
    
     
# --- Quiz ---
def quiz():
    print('--- QUIZ ---')
    repostas_marcadas = []
    try:
        with open('quiz.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        
        pontuacao = 0 
        gabarito = [questao['resposta_correta'] for questao in dados['quiz']]
        total_questoes = len(dados['quiz'])

        for i, questao in enumerate(dados['quiz'], start=1):
            print(f'\nQUESTÃO {i}:')
            print(questao['pergunta'])
            for alternativa in questao['alternativas']:
                print(alternativa)

            resposta = verificar_String('Resposta: -> ')
            repostas_marcadas.append(resposta)

            if resposta == questao['resposta_correta']:
                print('\n--- Correto! ---')
                print('-------------------------------------------')
                pontuacao +=1
                time.sleep(2)
            else:
                print(f'\nResposta Errada!!!\n Resposta Correta {questao['resposta_correta']}')
                print('-------------------------------------------')
                time.sleep(2)

        return pontuacao,total_questoes,repostas_marcadas,gabarito
    
    except FileNotFoundError:
        print('O Quiz Ainda Não Está Pronto!!!')
        sys.exit('Encerrando Programa!')


# --- Execução ---
if __name__ == '__main__':
    pontos, total, respostas, gabarito = quiz()
    print(f'\nVocê Acertou {pontos} questões de {total}')
    time.sleep(2)

    print('\n--- GABARITO ---')
    for i, correta in enumerate(gabarito, start=1):
        print(f'QUESTÃO {i}: {correta}')
    time.sleep(2)

    print('\n--- SUAS RESPOSTAS ---')
    for i,resposta in enumerate(respostas,start=1):
        print(f'QUESTÃO {i}: {resposta}')
    time.sleep(2)
