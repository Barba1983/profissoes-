
print("""
______________________________
     
     Guru das profissões.
  Grupo de Ciências Sociais.
________________________________

""")
nome= input('Para começar, insira seu nome: ')
print('Olá,',nome)
print("""
____________________________________________________________________________________________________________
|                                                                                                           |
|Vamos fazer algumas pergutas e você deverá digitar s e depois enter para sim ou n seguido de enter para não|
|___________________________________________________________________________________________________________|""")
leitura= input("""
Primeira pergunta:
Você gosta de ler?
""")
if leitura=='s':
    publico=input("""
Resposta registrada, vamos para a segunda pergunta:
Você tem facilidade (gosta) de falar em público?
    """)
    if publico=="s":
        estudos = input("""
Resposta registrada, vamos para a terceira pergunta:
Você gosta de estudar (muito e por muito tempo)?
            """)
        if estudos=='n':
            print("""
Segundo a nossa pesquisa, o curso que você tem mais afinidade é ............. 

_________

|DIREITO|
_________

O curso de direito exige uma grande quantidade de leitura e facilidade em falar em público. A graduação em direito 
(bacharelado) leva mais de cinco anos para ser concluida. 

Lembre-se, esse não é um estudo científico. Nosso objetivo era fazer você pensar nos prós e contras de cada curso.
Siga para a próxima parte da nossa sala e se informe sobre os cursos.

Obrigado pela paticipação. 

:* 

""")
            else:
                print(':(')

        else:
            print(":(")


else:
    print(":(")
