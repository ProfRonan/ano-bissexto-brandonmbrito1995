"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    ano = int(input('Digite um ano: '))

    if(ano % 4 == 0 and not ano % 100 == 0):
      print(f'O ano {ano} é bissexto.')
    elif(ano % 100 == 0 and ano % 400 == 0):
      print(f'O ano {ano} é bissexto.')
    else:
      print(f'O ano {ano} não é bissexto.')


if __name__ == '__main__':
    main()
