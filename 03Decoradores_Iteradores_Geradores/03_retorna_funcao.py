def calculadora(operacao):
    def soma(a,b):
        return a + b
    def sub(a,b):
        return a - b
    def mult(a,b):
        return a * b
    def div(a,b):
        return a / b
    
    match operacao:
        case '+':
            return soma
        case '-':
            return sub
        case '*':
            return mult
        case '/':
            return div
        
print(calculadora('+')(2,2))
print(calculadora('-')(2,2))
print(calculadora('*')(2,2))
print(calculadora('/')(2,2))