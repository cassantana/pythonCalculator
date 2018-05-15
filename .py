def main():
    print('\n*************** python calculator *****************')
    print('''selecione a operação desejada
    1 - soma
    2 - subtração
    3 - multiplicação
    4 - divisão
    ''')
    while True:
        try:
            operação = int(input('digite sua opção (1/2/3/4): '))
            primnum = int(input('digite o primeiro número: '))
            segnum = int(input('digite o segundo número: '))
        except:
            print('Você não digitou um número! Tente novamente.')
            continue        
    
        try:
            if operação == 1:
                soma = primnum + segnum
                print('\n')
                print(f'{primnum} + {segnum} =', soma)
                print('\n')
                break
            elif operação == 2:
                subtração = primnum - segnum
                print('\n')
                print(f'{primnum} - {segnum} =', subtração)
                print('\n')
                break
            elif operação == 3:
                multiplicação = primnum * segnum
                print('\n')
                print(f'{primnum} * {segnum} = ', multiplicação)
                print('\n')
                break
            elif operação == 4:
                divisão = primnum / segnum
                print('\n')
                print(f'{primnum} / {segnum} =', divisão)
                print('\n')
                break
            else:
                return 'Operação inválida!'
                break
        except ZeroDivisionError:
            print('Operação não permitida. Não é possível dividir um número por zero')
            break
main()
