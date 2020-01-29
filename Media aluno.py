print('Boa tarde aluno, o programa está em execução')
nome = input('Qual é seu nome?')
matéria = input('Qual é a matéria ?')
nota1 = float(input('Qual é a primeira nota?'))
nota2 = float(input('Qual é a segunda nota?'))
nota3 = float(input('Qual é a terceira nota?'))
nota4 = float(input('Qual é a quarta nota?'))
média = (nota1+nota2+nota3+nota4)/4
if média >= 7:
    print('Parabéns!!!')
    print('Aluno', nome, 'você foi APROVADO. Sua média em', matéria, 'foi',
          média, )
else:
    print('Aluno', nome, 'você foi REPROVADO.Sua média em',
          matéria, 'foi', média, '.')

    
    print testando alteração
