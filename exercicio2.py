def isFibonacci(n):
    
    if n < 0:
        return False
    
    a = 0
    b = 1

    while a <= n:
        if a == n:
            return True
        temp = a + b  
        a = b        
        b = temp

    return False

if __name__ == "__main__":
    try:
        number = (int(input("Digite um número:")))

        if isFibonacci(number):
            print(f"O número {number} pertence a sequência Fibonacci")
        else:
            print(f"O número {number} não pertence a sequência Fibonaci")
    except ValueError:
        print("Por favor, insira um número!")