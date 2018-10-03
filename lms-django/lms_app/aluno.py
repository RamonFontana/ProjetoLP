from django.db import models

class Aluno(models.Model):
    def __str__(self):
        return self.nome + ' -- ' + self.email
    
    def save(self):
        print("Salvado com sucesso")
        if (self.login == ''):
            raise Exception("sem login")
        
        if (self.email == ''):
            self.email = 'email nao fornecido'

        if len(Aluno.objects.filter(login=self.login)) > 0:
            raise Exception("Login ja cadastrado")

        super(Aluno,self).save()


    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    login = models.TextField(max_length=20)
    senha = models.TextField(max_length=20)