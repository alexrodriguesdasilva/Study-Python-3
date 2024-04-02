# restapi-flask-lab
Repositorio criado para praticar sobre o curso Projeto DevOps: Flask API - Do código ao deploy! do Mateus Muler

# Comandos:
# recomendado sempre usar um ambiente virtual para isolar as dependencias
python3 -m venv venv # Cria o ambiente virtual para o projeto 
source venv/bin/activate # Ativa nosso ambiente virtual

pip freeze #imprimir as dependencias utilizadas no projeto
pip freeze > requirements.txt #Jogar as dependencias do projeto no arquivo requirements.txt

docker build -t restapi:0.1 . # buildando imagem Dockerfile
docker run -P restapi:0.1 # executa a imagem localmente, o -P vai subir o container em uma porta aleatoria