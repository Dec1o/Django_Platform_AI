from django.db import models
from groups_files.models import GroupFile  # Importa o modelo de grupos

class AIChat(models.Model):
    group = models.ForeignKey(GroupFile, on_delete=models.CASCADE, related_name='ai_chats')  # FK obrigatória para o grupo
    chat_name = models.CharField(max_length=255)  # Nome do chat, editável
    temperature = models.FloatField(default=0.7)  # Temperatura do chat, editável
    prompt = models.TextField()  # Prompt principal da IA, editável

    def __str__(self):
        return self.chat_name
