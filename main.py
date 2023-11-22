import math

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class PessoaModel(BaseModel):
   primeiro_nome : str
   ultimo_nome : str
   idade : int

class BhaskaraModel(BaseModel):
   a : float
   b : float
   c : float

class FraseModel(BaseModel):
   frase : str

@app.get("/")
def index():
   return { "data" : "Testando FastAPI!" }

@app.post("/hello")
def helloPost(pessoa : PessoaModel):
   return {
       "data" : f'Hello {pessoa.primeiro_nome} {pessoa.ultimo_nome}, you are {pessoa.idade}!'
   }


@app.get("/hello/{name}")
def helloName(name):
   return { 
"data" : f'Hello {name}!' 
}

@app.get("/quadrado/{num}")
def quadrado(num: int):
   return {
       "data" : {
           "num" : num,
           "quadrado" : num ** 2
       }
   }

# Optional [int] = 20

@app.get("/pares")
def listaPares(limit : int):
   pares = []
   for i in range(0, limit+1, 2):
       pares.append(i)
  
   return {
       "limit" : limit,
       "pares" : pares
   }

@app.get("/quadrados")
def quadrados(max : Optional [int] = 10):
   quadrados = []
   for i in range(0, max+1, 1):
       quadrados.append(i*i)

   return {
           "max" : max,
           "quadrados" : quadrados
   }

@app.get("/tabuada/{num}")
def tabuada(num : int, start:Optional [int] = 0, end:Optional [int] = 10):
   tabuada = []
   for i in range(start, end+1, 1):
       tabuada.append(i*num)

   return {
           "num" : num,
           "start" : start,
           "end" : end,
           "tabuada" : tabuada
   }

@app.post("/bhaskara")
def equationPost(bhaskara : BhaskaraModel):
    delta = (bhaskara.b ** 2) - 4 * bhaskara.a * bhaskara.c
    x1 = (( bhaskara.b * -1 ) + math.sqrt(delta)) / (2 * bhaskara.a)
    x2 = (( bhaskara.b * -1 ) - math.sqrt(delta)) / (2 * bhaskara.a)

    return {
       "equation" : f'{bhaskara.a}x² + {bhaskara.b}x + {bhaskara.c}',
       "delta": delta,
       "raiz": math.sqrt(delta),
       "x1": x1,
       "x2": x2
    }

@app.post("/conta")
def helloPost(frase : FraseModel):
   vogais = ["a", "e", "i", "o", "u"]
   espaço = [" "]

   numeroVogais = 0
   numeroEspaços = 0

   for caracteres in frase.frase:
      if caracteres in vogais:
         numeroVogais += 1

   for caracteres in frase.frase:
      if caracteres in espaço:
         numeroEspaços += 1

   outros = len(frase.frase) - (numeroVogais + numeroEspaços)
   
   return {
       "frase": frase.frase,
       "vogais": numeroVogais,
       "espacos": numeroEspaços,
       "outros": outros 
   }


