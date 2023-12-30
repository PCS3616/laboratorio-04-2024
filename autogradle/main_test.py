from pathlib import Path
import subprocess
import re
import tempfile

submission_path = Path("./submission")

def limpa(string):
    res=string.split(" ")
    res=list(filter(None, res))
    return int(res[1]+res[2],16)

def twos_complement(hexstr,bits):
    value = int(hexstr,16)
    if value & (1 << (bits-1)):
        value -= 1 << bits
    return value
  
def fatorial(n: int):
  if n <= 1:
    return 1
  return n*fatorial(n-1)

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
    filecode = submission_path / "subtracao.mvn"
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

def test_2(n: int = 0):
    filecode = submission_path / "fatorial.mvn"
    assert filecode.exists(), f"A submissão não contém o arquivo '{filecode.name}'"

    n_str = "{:04X}".format(n)
    input_file = tempfile.NamedTemporaryFile(mode='w')
    input_file.writelines([
        f"0100	{n_str}\n"
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
        f"m 0102 0103 {output_file.name}",
        "",
        "x",
        "",
    ]

    run_mvn('\n'.join(inputs))

    fat = limpa(output_file.read())

    assert fat == fatorial(n), \
      f"Seu código não está correto\nConfira seu envio."

def test_2_1():
  test_2(0)

def test_2_2():
  test_2(1)

def test_2_3():
  test_2(4)

def test_2_4():
  test_2(5)
