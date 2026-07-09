from pathlib import Path
#Pasta global
PASTA_GLOBAL = (Path(__file__).resolve().parent.parent) 
print(PASTA_GLOBAL)

#Pastas importantes
PASTA_USUARIOS = PASTA_GLOBAL / "Users"


#Arquivos importantes
ARQUIVO_USUARIO = PASTA_USUARIOS / 'Usuario.json'
JSON_USUARIOS = PASTA_USUARIOS / 'Usuarios.json'



