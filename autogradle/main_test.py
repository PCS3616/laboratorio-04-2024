from pathlib import Path
import subprocess
import re
import tempfile

submission_path = Path("./submission")

def limpa(string):
    res=string.split(" ")
    res=list(filter(None, res))
    return int(res[1]+res[2],16)

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

def test_1_1():
    filecode = submission_path / "triangulos.mvn"
    assert filecode.exists(), f"A submissão não contém o arquivo '{filecode.name}'"

    input_file = tempfile.NamedTemporaryFile(mode='w')
    input_file.writelines([
        "0010	0001\n",
        "0012	0002\n",
        "0014	0003\n",
        ";0016	0000\n",
    ])
    input_file.flush()

    output_file = tempfile.NamedTemporaryFile(mode='r')

    inputs = [
        f"p {filecode.as_posix()}",
        "",
        f"p {input_file.name}",
        "",
        "r",
        "0",
        "n",
        "",
        f"m 0016 0017 {output_file.name}",
        "",
        "x",
        "",
    ]

    out = run_mvn('\n'.join(inputs))

    mvn_output = limpa(output_file.read())

    assert mvn_output == 0, \
            f"Seu código não está correto"

def test_1_2():
    filecode = submission_path / "triangulos.mvn"
    assert filecode.exists(), f"A submissão não contém o arquivo '{filecode.name}'"

    input_file = tempfile.NamedTemporaryFile(mode='w')
    input_file.writelines([
        "0010	0003\n",
        "0012	0004\n",
        "0014	0005\n",
        ";0016	0001\n",
    ])
    input_file.flush()

    output_file = tempfile.NamedTemporaryFile(mode='r')

    inputs = [
        f"p {filecode.as_posix()}",
        "",
        f"p {input_file.name}",
        "",
        "r",
        "0",
        "n",
        "",
        f"m 0016 0017 {output_file.name}",
        "",
        "x",
        "",
    ]

    out = run_mvn('\n'.join(inputs))

    mvn_output = limpa(output_file.read())

    assert mvn_output == 1, \
            f"Seu código não está correto"

def test_1_3():
    filecode = submission_path / "triangulos.mvn"
    assert filecode.exists(), f"A submissão não contém o arquivo '{filecode.name}'"

    input_file = tempfile.NamedTemporaryFile(mode='w')
    input_file.writelines([
        "0010	0003\n",
        "0012	0004\n",
        "0014	0004\n",
        ";0016	0002\n",
    ])
    input_file.flush()

    output_file = tempfile.NamedTemporaryFile(mode='r')

    inputs = [
        f"p {filecode.as_posix()}",
        "",
        f"p {input_file.name}",
        "",
        "r",
        "0",
        "n",
        "",
        f"m 0016 0017 {output_file.name}",
        "",
        "x",
        "",
    ]

    out = run_mvn('\n'.join(inputs))

    mvn_output = limpa(output_file.read())

    assert mvn_output == 2, \
            f"Seu código não está correto"

def test_1_4():
    filecode = submission_path / "triangulos.mvn"
    assert filecode.exists(), f"A submissão não contém o arquivo '{filecode.name}'"

    input_file = tempfile.NamedTemporaryFile(mode='w')
    input_file.writelines([
        "0010	0003\n",
        "0012	0004\n",
        "0014	0006\n",
        ";0016	0003\n",
    ])
    input_file.flush()

    output_file = tempfile.NamedTemporaryFile(mode='r')

    inputs = [
        f"p {filecode.as_posix()}",
        "",
        f"p {input_file.name}",
        "",
        "r",
        "0",
        "n",
        "",
        f"m 0016 0017 {output_file.name}",
        "",
        "x",
        "",
    ]

    out = run_mvn('\n'.join(inputs))

    mvn_output = limpa(output_file.read())

    assert mvn_output == 3, \
            f"Seu código não está correto"

def test_3():
    filecode = submission_path / "quadrados-perfeitos.mvn"
    assert filecode.exists(), f"A submissão não contém o arquivo '{filecode.name}'"

    output_file = tempfile.NamedTemporaryFile(mode='r')

    inputs = [
        f"p {filecode.as_posix()}",
        "",
        "r",
        "0",
        "n",
        "",
        f"m 0100 017f {output_file.name}",
        "",
        "x",
    ]

    out = run_mvn('\n'.join(inputs))

    mvn_output = output_file.read()
    expected_output = """
0100:  00  00  00  01  00  04  00  09  00  10  00  19  00  24  00  31  
0110:  00  40  00  51  00  64  00  79  00  90  00  a9  00  c4  00  e1  
0120:  01  00  01  21  01  44  01  69  01  90  01  b9  01  e4  02  11  
0130:  02  40  02  71  02  a4  02  d9  03  10  03  49  03  84  03  c1  
0140:  04  00  04  41  04  84  04  c9  05  10  05  59  05  a4  05  f1  
0150:  06  40  06  91  06  e4  07  39  07  90  07  e9  08  44  08  a1  
0160:  09  00  09  61  09  c4  0a  29  0a  90  0a  f9  0b  64  0b  d1  
0170:  0c  40  0c  b1  0d  24  0d  99  0e  10  0e  89  0f  04  0f  81  
Final do dump.""".strip()

    assert mvn_output == expected_output, \
            f"Seu código não está correto"
