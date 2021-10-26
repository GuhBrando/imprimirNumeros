def imprimirNumerosMenorParaMaior(QtdVezes, count):
    print(count)
    if  QtdVezes == count:
        return 1
    return imprimirNumerosMenorParaMaior(QtdVezes, count + 1)

def imprimirNumerosMaiorParaMenor(QtdVezes):
    print(QtdVezes)
    if QtdVezes == 1:
        return 1
    return imprimirNumerosMaiorParaMenor(QtdVezes - 1)

def main():
    opcao = int(input("Digite 0 para imprimir do maior para o menor e 1 para o menor do maior: "))
    if opcao == 0:
        num = int(input("Digite a quantidade de vezes que deseja processar: "))
        imprimirNumerosMaiorParaMenor(num)
    elif opcao == 1:
        num = int(input("Digite a quantidade de vezes que deseja processar: "))
        imprimirNumerosMenorParaMaior(num, 1)
    
if __name__ == "__main__":
    main()