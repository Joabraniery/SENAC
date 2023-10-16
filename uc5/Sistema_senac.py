class Curso:
    def __init__(self, nome, vagas_minimas):
        self.nome = nome
        self.vagas_minimas = vagas_minimas
        self.alunos = []

class Professor:
    def __init__(self, nome, horas_semanais):
        self.nome = nome
        self.horas_semanais = horas_semanais
        self.cursos = []

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.cursos = []

class Senac:
    def __init__(self):
        self.cursos = []
        self.professores = []
        self.alunos = []

    def criar_curso(self, nome, vagas_minimas):
        curso = Curso(nome, vagas_minimas)
        self.cursos.append(curso)
        return curso

    def contratar_professor(self, nome, horas_semanais):
        professor = Professor(nome, horas_semanais)
        self.professores.append(professor)
        return professor

    def matricular_aluno(self, nome):
        aluno = Aluno(nome)
        self.alunos.append(aluno)
        return aluno

    def inscrever_aluno_curso(self, aluno, curso):
        if aluno in self.alunos and curso in self.cursos:
            if len(aluno.cursos) < 2 and len(curso.alunos) < curso.vagas_minimas:
                aluno.cursos.append(curso)
                curso.alunos.append(aluno)
                return True
        return False

    def atribuir_professor_curso(self, professor, curso):
        if professor in self.professores and curso in self.cursos:
            if sum(p.horas_semanais for p in professor.cursos) + curso.horas_semanais <= 40:
                professor.cursos.append(curso)
                return True
        return False

# Aplicação:

senac = Senac()
curso1 = senac.criar_curso("Curso de Python", 10)
curso2 = senac.criar_curso("Curso de JavaScript", 10)

# Cadastrando 5 professores
professor1 = senac.contratar_professor("João", 20)
professor2 = senac.contratar_professor("Maria", 30)
professor3 = senac.contratar_professor("Pedro", 15)
professor4 = senac.contratar_professor("Ana", 25)
professor5 = senac.contratar_professor("Carlos", 10)

# Matriculando 20 alunos
aluno1 = senac.matricular_aluno("Alice")
aluno2 = senac.matricular_aluno("Bob")
aluno3 = senac.matricular_aluno("Carol")
aluno4 = senac.matricular_aluno("Daniel")
aluno5 = senac.matricular_aluno("Eva")
aluno6 = senac.matricular_aluno("Felipe")
aluno7 = senac.matricular_aluno("Gisele")
aluno8 = senac.matricular_aluno("Hugo")
aluno9 = senac.matricular_aluno("Igor")
aluno10 = senac.matricular_aluno("Julia")
aluno11 = senac.matricular_aluno("Kevin")
aluno12 = senac.matricular_aluno("Laura")
aluno13 = senac.matricular_aluno("Miguel")
aluno14 = senac.matricular_aluno("Nina")
aluno15 = senac.matricular_aluno("Oscar")
aluno16 = senac.matricular_aluno("Paula")
aluno17 = senac.matricular_aluno("Quiteria")
aluno18 = senac.matricular_aluno("Ricardo")
aluno19 = senac.matricular_aluno("Sofia")
aluno20 = senac.matricular_aluno("Túlio")

# Inscrevendo alunos em cursos
senac.inscrever_aluno_curso(aluno1, curso1)
senac.inscrever_aluno_curso(aluno1, curso2)
senac.inscrever_aluno_curso(aluno2, curso1)
senac.inscrever_aluno_curso(aluno3, curso2)
senac.inscrever_aluno_curso(aluno4, curso1)

# Atribuindo a cursos
senac.atribuir_professor_curso(professor1, curso1)
senac.atribuir_professor_curso(professor2, curso2)
senac.atribuir_professor_curso(professor3, curso1)
senac.atribuir_professor_curso(professor4, curso2)
senac.atribuir_professor_curso(professor5, curso1)
