# PCS3616 - Laboratório 4 - MVN 2

Nesta aula vamos continuar o trabalho da semana passada, hoje você deve
criar mais alguns programas em linguagem de máquina de MVN.

## 1. `subtracao.mvn`
Escrever um programa que executa a subtração
de dois inteiros *em uma sub-rotina*. O programa principal
armazena os inteiros nas posições 0x010 (variável x) e 0x012 (variável
y) e chama a sub-rotina, que deve executar a operação x-y e armazenar o
resultado na posição de memória 0x014.

## 2. `op-mnem.mvn`
Desenvolva duas sub-rotinas (`OP2MNEM` e `MNEM2OP`), cujas finalidades são:

### OP2MNEM (endereço inicial: 0x100)
converte um número inteiro dado, 0≤ n ≤ 15, localizado na posição de 
memória OPCODE (0x010) no mnemônico correspondente, formado por dois
caracteres ASCII (consultar a tabela de mnemônicos fornecida adiante).
O mnemônico deverá ser armazenado na posição de memória MNEM (0x012).

### MNEM2OP (endereço inicial: 0x200)
faz a conversão oposta,
transformando um mnemônico válido localizado em MNEM, dado como dois
caracteres ASCII, em um número inteiro correspondente, , 0 ≤ n ≤ 15,
armazenado na posição de memória OPCODE, novamente conforme a tabela
de mnemônicos fornecida.

### Um pequeno programa principal (endereço inicial: 0x300)
deve ilustrar o uso das duas sub-rotinas.

Observação: ambos os parâmetros, MNEM e OPCODE, são representados como
inteiros, ocupando, cada qual, dois bytes de memória.

Exemplo de operação:

-   Dado o OPCODE 0x0001, armazenado na posição OPCODE e OPCODE + 1 de
    memória, contendo respectivamente os bytes 00 e 01, a sub-rotina
    OP2MNEM retorna como resultado o par de letras JZ (*jump if zero*),
    cujos códigos ASCII são 4A e 5A, respectivamente. Em outras
    palavras, a posição de memória MNEM deverá conter o byte 0x4A e a
    posição MNEM+1 deverá conter o byte 0x5A.

-   Dado o mnemônico JZ em (MNEM, MNEM+1), ou seja, dado o par de bytes
    (0x4A, 0x5A), a sub-rotina MNEM2OP retornará em (OPCODE, OPCODE+1) o
    par de bytes (00, 01).
