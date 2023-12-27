from pathlib import Path
import subprocess
import re
import tempfile

submission_path = Path("./submission")

def twos_complement(hexstr,bits):
    value = int(hexstr,16)
    if value & (1 << (bits-1)):
        value -= 1 << bits
    return value

def run_mvn(input_text):
    # I hate the current MVN
    # A good class solve this, but now are a really mess code

    p = subprocess.run(
        [
            "python", 
            "-m", 
            "MVN.mvnMonitor"
        ],
        input=input_text,
        capture_output=True, 
        text=True,
    )
    return p.stdout

def test_1():
    filecode = submission_path / "ex2-subtracao.mvn"
    assert filecode.exists(), f"A submissão não contém o arquivo '{filecode.name}'"
    
    with open(filecode, mode='r') as f:
        code = f.read().upper()

        assert len(re.findall(r"A[\dA-F]{3}", code)) > 0, \
            "O seu código deve conter uma chamada de subrotina"

        assert len(re.findall(r"B[\dA-F]{3}", code)) > 0, \
            "O seu código deve conter uma subrotina"

    inputs = [
        f"p {filecode.as_posix()}",
         "r",
         "",
         "n",
         "",
         "m 0010 0015",
         "x",
         "",
    ]

    output = run_mvn('\n'.join(inputs))

    saida=output.split("\n")[-6:-3]
    print(saida)

    nums=saida[-1].split("  ")
    x=twos_complement(nums[1]+nums[2], 16)
    y=twos_complement(nums[3]+nums[4], 16)
    r=twos_complement(nums[5]+nums[6], 16)

    assert x-y == r, \
        f"Seu código não está correto\nConfira seu envio."

def test_2():
    filecode = submission_path / "op-mnem.mvn"
    assert filecode.exists(), f"A submissão não contém o arquivo '{filecode.name}'"

    input_file = tempfile.NamedTemporaryFile(mode='w')
    input_file.writelines("""
0000 0300

; Testa OP2MNEM e MNEM2OP
;;
02FC 0000 ; OP2MNEM funcionou?
02FE 0000 ; MNEM2OP funcionou?
;;
0300 8410 ; Carrega OPCODE de JZ
0302 9010 ; Escreve no operador de OPCODE
0304 A100 ; Chama OP2MNEM
0306 8412 ; Carrega MNEM de JZ
0308 5012 ; Subtrai MNEM de JZ do resultado de OP2MNEM
030A 130E ; Se for igual, sinaliza que funcionou
030C 0312 ; Senão, continua
030E 3001 ; AC <= 1
0310 92FC ; Sinaliza que OP2MNEM funcionou
0312 3000 ; AC <= 0
0314 9010 ; OPCODE <= 0
0316 9012 ; MNEM <= 0
0318 8412 ; Carrega MNEM de JZ
031A 9012 ; Escreve no operador de MNEM
031C A200 ; Chama MNEM2OP
031E 8410 ; Carrega OPCODE de JZ
0320 5010 ; Subtrai OPCODE de JZ do resultado de MNEM2OP
0322 1326 ; Se for igual, sinaliza que funcionou
0324 032A ; Senão, finaliza MAIN
0326 3001 ; AC <= 1
0328 92FE ; Sinaliza que MNEM2OP funcionou
032A C32A ; HALT

0410 0001
0412 4A5A
    """)
    input_file.flush()

    output_file = tempfile.NamedTemporaryFile(mode='r')

    inputs = [
        f"p {filecode.as_posix()}",
        "",
        f"p {input_file.name}",
        "",
        "r",
        "0",
        "y",
        "",
        f"m 02FC 02FF {output_file.name}",
        "",
        "x",
        "",
    ]

    out = run_mvn('\n'.join(inputs))

    mvn_output = output_file.read().lstrip('02f0:').strip()

    print(mvn_output)

    assert mvn_output == "00  01  00  01", \
            f"Seu código não está correto"
