from cpf_uteis import (
    etapa1_dv1,
    etapa1_dv2,
    etapa2_dv1,
    etapa2_dv2,
    dv,
    filtra_mascara_cpf,
    verifica_tem_11_numeros,
    verifica_sequencia_cpf,
)


def test_etapa1_dv1():
    """Testa o resultado da soma dos produtos de cada dígito por um peso de 2 a 10, na ordem inversa (do nono para o primeiro)."""
    assert etapa1_dv1("398136146") == 258


def test_etapa1_dv2():
    """Testa o resultado da soma dos produtos de cada dígito por um peso de 3 a 11, também na ordem inversa."""
    assert etapa1_dv2("398136146") == 299


def test_etapa2_dv1():
    """Testa o Calculo do dv1 do CPF"""
    assert etapa2_dv1("398136146") == 6


def test_etapa2_dv2():
    """Testa o Calculo do dv2 do CPF"""
    assert etapa2_dv2("398136146") == 8


def test_filtra_mascara():
    """Testa se tira a mascara do cpf"""
    assert filtra_mascara_cpf("115.504.629-38") == "11550462938"
    assert filtra_mascara_cpf("115.504.629") == "115504629"
    assert filtra_mascara_cpf("11550462938") == "11550462938"
    assert filtra_mascara_cpf("115504629") == "115504629"


def test_dv():
    """Testa o Calculo do dv do cpf sem mascara"""
    assert dv("115504629") == "38"
    assert dv("451021461") == "81"
    assert dv("241620696") == "62"
    assert dv("595340180") == "90"
    assert dv("262970126") == "36"
    assert dv("124437587") == "02"
    assert dv("922404392") == "54"
    assert dv("641223665") == "18"


def test_tem_11_numeros():
    """Verifica se o cpf contem 11 numeros"""
    assert verifica_tem_11_numeros("115.504.629") == False
    assert verifica_tem_11_numeros("aaa..11550462938") == True
    assert verifica_tem_11_numeros("112.115.461-38") == True
    assert verifica_tem_11_numeros("11550462938") == True
    assert verifica_tem_11_numeros("115504629") == False
    assert verifica_tem_11_numeros("1155046293") == False


def test_verifica_sequencia_cpf():
    "Verifica se o cpf é uma sequencia de numeros"
    assert verifica_sequencia_cpf("111111111") == True
    assert verifica_sequencia_cpf("222222222") == True
    assert verifica_sequencia_cpf("11550462938") == False
    assert verifica_sequencia_cpf("115504629") == False
    assert verifica_sequencia_cpf("1155046293") == False
    assert verifica_sequencia_cpf("11550462938") == False
    assert verifica_sequencia_cpf("115504629") == False
    assert verifica_sequencia_cpf("1155046293") == False
    assert verifica_sequencia_cpf("115.504.629-38") == False
    assert verifica_sequencia_cpf("11550462938") == False
    assert verifica_sequencia_cpf("115504629") == False
    assert verifica_sequencia_cpf("1155046293") == False
