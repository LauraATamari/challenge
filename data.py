import random
import csv

#gerando data para analise

with open('data.csv', 'w', newline='') as file:
    output = csv.writer(file)

    generos = ['masculino', 'feminino', 'transgenero', 'nao-binario', 'outro', 'prefiro nao informar']
    etnias = ['branco', 'negro', 'pardo', 'indigena', 'amarelo', 'outro']
    es_civil = ['solteiro', 'casado', 'divorciado', 'viuvo']
    deficiencias = ['nao', 'deficiencia fisica', 'deficiencia intelectual', 'deficiencia auditiva', 'deficiencia visual']
    orientacoes = ['heterossexual', 'homossexual', 'bissexual', 'assexual', 'pansexual', 'outro', 'prefiro nao informar']
    vulnerabilidades = ['nao', 'territorial', 'genero', 'orientacao sexual', 'etnia']
    formacoes = ['bacharelado', 'licenciatura', 'tecnologo', 'especializacao', 'MBA', 'mestrado', 'doutorado']
    experiencias = ['sim', 'nao']
    estados = ['AC', 'Al', 'AP', 'AM', 'BA', 'CE', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO', 'DF']
    idimoas = ['nao', 'espanhol', 'ingles', 'mandarim', 'japones', 'alemao']
    ensinos = ['USP', 'PUC', 'UNESP', 'FIAP', 'UNIP', 'UNINOVE']
    cursos = ['engenharia', 'sistemas de informacao', 'pedagogia', 'medicina', 'enfermagem', 'veterinaria', 'turismo']
    for _ in range(501):
        genero = random.choice(generos)
        etnia = random.choice(etnias)
        civil = random.choice(es_civil)
        deficiencia = random.choice(deficiencias)
        orientacao = random.choice(orientacoes)
        vulnerabilidade = random.choice(vulnerabilidades)
        formacao = random.choice(formacoes)
        experiencia = random.choice(experiencias)
        estado = random.choice(estados)
        idioma = random.choice(idimoas)
        ensino = random.choice(ensinos)
        curso = random.choice(cursos)

        output.writerow([genero, etnia, civil, deficiencia, orientacao, vulnerabilidade, formacao, experiencia, estado, idioma, ensino, curso])


