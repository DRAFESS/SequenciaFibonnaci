def fibonacci_sequence(limit):
    sequence = [0, 1]
    while sequence[-1] < limit:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence

def is_in_fibonacci(number):
    sequence = fibonacci_sequence(number)
    if number in sequence:
        return f"O número {number} pertence à sequência de Fibonacci."
    else:
        return f"O número {number} não pertence à sequência de Fibonacci."

number_to_check = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

result = is_in_fibonacci(number_to_check)
print(result)
