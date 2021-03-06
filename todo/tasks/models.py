from django.db import models

class Task(models.Model):  #Classe 

    #Status da tarefa que foi criada.
    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done'),
    )   
    
    title = models.CharField(max_length=255) #Título da tarefa
    description = models.TextField()  #Descrição da tarefa.
    done = models.CharField(      
        max_length=5,
        choices=STATUS,
    )

    #Data e horário de criação e atualização
 
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title