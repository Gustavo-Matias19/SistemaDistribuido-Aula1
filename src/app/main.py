from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Lista que armazena todas as tarefas
tarefas = list()


# Define o formato dos dados de uma tarefa
class Tarefa(BaseModel):
    tarefa: str
    prioridade: int
    feito: bool


# GET /
# Retorna todas as tarefas cadastradas
@app.get("/")
def root():
    return tarefas


# GET /tarefa/{pos}
# Retorna uma tarefa especifica pela posicaoo na lista
@app.get("/tarefa/{pos}")
def get_tarefa(pos: int):
    return tarefas[pos]


# POST /adicionar/
# Adiciona uma nova tarefa a lista
@app.post("/adicionar/")
def criar_tarefa(tarefa: Tarefa):

    # Define a tarefa como nao concluida
    tarefa.feito = False

    # Adiciona a tarefa na lista
    tarefas.append(tarefa)

    # Retorna a quantidade de tarefas cadastradas
    return len(tarefas)


# PUT /feito/{pos}
# Marca uma tarefa como concluida
@app.put("/feito/{pos}")
def marcar_feito(pos: int):

    # Altera o campo "feito" para True
    tarefas[pos].feito = True

    # Retorna a tarefa atualizada
    return tarefas[pos]


# DELETE /deletar/{pos}
# Remove uma tarefa da lista
@app.delete("/deletar/{pos}")
def deletar_tarefa(pos: int):

    # Remove a tarefa pela posicao e guarda a tarefa removida
    tarefa = tarefas.pop(pos)

    # Retorna a tarefa que foi removida
    return tarefa