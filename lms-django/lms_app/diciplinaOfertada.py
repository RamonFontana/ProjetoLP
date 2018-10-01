from django.db import models

class DisciplinaOfertada(models.Model):

    def save(self):

        if (self.curso not in 'ADS SI BD'):
            raise Exception("Curso não existente")
        
        curso = len(DisciplinaOfertada.objects.filter(curso=self.curso))
        turma = len(DisciplinaOfertada.objects.filter(turma=self.turma))
        ano = len(DisciplinaOfertada.objects.filter(ano=self.ano))
        semestre = len(DisciplinaOfertada.objects.filter(semestre=self.semestre))
        professor = len(DisciplinaOfertada.objects.filter(professor=self.professor))
        disciplina = len(DisciplinaOfertada.objects.filter(disciplina=self.disciplina))

        if (curso > 0 and turma > 0 and ano > 0 and semestre > 0 and professor > 0 and diciplina > 0):
            raise Exception("Diciplina ofertada já existe")

        super(DisciplinaOfertada,self).save()

    curso = models.TextField(max_length=255)
    turma = models.TextField(max_length=5)
    ano = models.IntegerField() #um inteiro, representa um ano
    semestre = models.IntegerField() #um inteiro, 1 para primeiro sem e 2 para segundo
    professor = models.IntegerField() #id de um professor valido
    disciplina = models.IntegerField() #id de uma disciplina valida
