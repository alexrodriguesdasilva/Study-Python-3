# Tipo string

## Em Python, um dado é considerado do tipo string sempre que:
### Estiver entre àspas simples -> 'uma string'
### Estiver entre àspas duplas -> "uma string"
### Estiver entre àspas simples triplas -> '''uma string'''
### Estiver entre àspas duplas triplas -> """uma string"""

Exemplos:
```python
nome = 'Alex Rodrigues'
print(nome)
print(type(nome))
```

```python
nome = "Gina's Bar"
print(nome)
print(type(nome))
```

```python
nome = '''Alex Rodrigues'''
print(nome)
print(type(nome))
```

```python
nome = """Alex Rodrigues"""
print(nome)
print(type(nome))
```

## Imprimindo todas as letras de uma string em maiusculas
```python
nome = 'Alex Rodrigues'
print(nome.upper())
```

## Imprimindo todas as letras de uma string em minusculas
```python
nome = 'Alex Rodrigues'
print(nome.lower())
```

## Imprimindo as palavras em forma de uma lista de strings
```python
nome = 'Alex Rodrigues'
print(nome.split())
```

## slice de string
```python
nome = 'Alex Rodrigues'
print(nome[0:4])
print(nome[5:14])
print(nome.split()[0])