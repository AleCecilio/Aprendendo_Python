def fibonacci(quantidade, sequencia = (0, 1)):
    return sequencia if len(sequencia) == quantidade else \
        fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    # Listar os 20 primeiros números dessa sequência
    for fib in fibonacci(20):
        print(fib)
