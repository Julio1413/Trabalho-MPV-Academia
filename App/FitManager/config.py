from pathlib import Path
#Pasta global
PASTA_GLOBAL = (Path(__file__).resolve().parent.parent) 
print(PASTA_GLOBAL)

#Pastas importantes
PASTA_USUARIOS = PASTA_GLOBAL / "Users"
PASTA_TREINOS = PASTA_GLOBAL / 'Treinos'

#Arquivos importantes
ARQUIVO_LISTA_TREINOS = PASTA_TREINOS / 'Treinos.json'
ARQUIVO_USUARIO = PASTA_USUARIOS / 'Usuario.json'
JSON_USUARIOS = PASTA_USUARIOS / 'Usuarios.json'



