# Tipos Numéricos em Python

Em Python, os tipos numéricos são fundamentais para o processamento de dados e cálculos matemáticos. Existem três tipos numéricos principais: inteiros (integers), números de ponto flutuante (floating-point numbers) e números complexos (complex numbers). Vamos explorar cada um deles:

## 1. Inteiros (int)
Inteiros são números sem casas decimais. Em Python, eles podem ser positivos, negativos ou zero. A precisão dos inteiros em Python é ilimitada, o que significa que você pode trabalhar com inteiros muito grandes, desde que tenha memória suficiente.

Exemplos:
```python
x = 10
y = -5
z = 0
```

## 2. Números de Ponto Flutuante (float)
Números de ponto flutuante são números que possuem uma parte inteira e uma parte fracionária, representados com casas decimais. Em Python, os floats são representados usando a notação de ponto flutuante de dupla precisão (64 bits).

Exemplos:
```python
a = 3.14
b = -0.001
c = 2.0
```

## 3. Números Complexos (complex)
Números complexos têm uma parte real e uma parte imaginária, representados na forma a + bj, onde a é a parte real e b é a parte imaginária, e j (ou i em algumas convenções matemáticas) é a unidade imaginária.

Exemplos:
```python
num1 = 2 + 3j
num2 = -1j
num3 = 4.5 + 0j
```

# Operações Comuns com Tipos Numéricos
Python suporta uma ampla gama de operações aritméticas com esses tipos numéricos. Aqui estão algumas das operações básicas:

## Adição
```python
soma = 5 + 3.2  # 8.2
```

## Subtração
```python
subtracao = 10 - 4  # 6
```

## Multiplicação
```python
multiplicacao = 7 * 3  # 21
```

## Divisão
```python
divisao = 10 / 4  # 2.5
```

## Divisão Inteira
```python
divisao_inteira = 10 // 4  # 2
```

## Módulo
```python
modulo = 10 % 3  # 1
```

## Exponenciação
```python
exponenciacao = 2 ** 3  # 8
```

# Conversões Entre Tipos Numéricos
Às vezes, é necessário converter entre diferentes tipos numéricos. Python fornece funções para isso:

## De inteiro para float
```python
float_num = float(5)  # 5.0
```

## De float para inteiro
```python
int_num = int(3.14)  # 3
```

## De número real para número complexo
```python
complex_num = complex(2)  # (2+0j)
```

## De string para número
```python
int_from_str = int("10")  # 10
float_from_str = float("3.14")  # 3.14
``

Com esses conceitos e operações, você estará bem equipado para trabalhar com números em Python. Se precisar de mais detalhes ou exemplos específicos, sinta-se à vontade para perguntar!