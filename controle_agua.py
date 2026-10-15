from colorama import Fore, Style, init

# Inicializa o colorama para garantir o funcionamento correto das cores no terminal
init(autoreset=True)


def definir_alerta(nivel):
  """Retorna a tupla contendo a mensagem de situação e a cor correspondente

  conforme o nível do reservatório informado.
  """
  # Lista de dicionários representando os 5 níveis do reservatório, mensagens e cores
  niveis_reservatorio = [
      {
          "nivel": 1,
          "situacao": "Nível 1: Muito baixo (crítico)",
          "cor": Fore.RED,
      },
      {"nivel": 2, "situacao": "Nível 2: Baixo", "cor": Fore.YELLOW},
      {"nivel": 3, "situacao": "Nível 3: Médio", "cor": Fore.GREEN},
      {"nivel": 4, "situacao": "Nível 4: Alto", "cor": Fore.CYAN},
      {"nivel": 5, "situacao": "Nível 5: Muito alto (alerta)", "cor": Fore.BLUE},
  ]

  # Busca e retorna a situação correspondente ao nível informado
  for item in niveis_reservatorio:
    if item["nivel"] == nivel:
      return item["situacao"], item["cor"]

  return "Nível desconhecido", Style.RESET_ALL


def simular_monitoramento():
  print("=== SISTEMA DE MONITORAMENTO DE RESERVATÓRIO DE ÁGUA ===")
  print("Simulando os níveis do reservatório no terminal...\n")

  # Simula a verificação iterando pelos 5 níveis definidos
  for nivel_atual in range(1, 6):
    situacao, cor = definir_alerta(nivel_atual)

    # Exibe a mensagem formatada com a cor específica da situação
    print(f"{cor}{situacao}{Style.RESET_ALL}")


if __name__ == "__main__":
  simular_monitoramento()