from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class PessoaModel(BaseModel):
   primeiro_nome : str
   ultimo_nome : str
   idade : int

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

@app.get("/pares")
def listaPares(limit : Optional [int] = 20):
   pares = []
   for i in range(0, limit+1, 2):
       pares.append(i)
  
   return {
       "limit" : limit,
       "pares" : pares
   }

@app.get("/quadrados")
def quadrados(max : Optional [int] = 20):
   quadrados = []
   for i in range(1, max+1, 2):
       quadrados.append(i)

   return {
       "data" : {
           "max" : max,
           "quadrados" : quadrados
       }
   }



