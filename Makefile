# Variables
PYTHON=python3
PIP=pip
DOCKER_IMAGE=fastapi-events-app
DOCKER_TAG=latest

# Instalación de dependencias
install:
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Correr el servidor en modo desarrollo (con autoreload)
run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Correr el servidor en producción (sin autoreload)
run-prod:
	uvicorn app.main:app --host 0.0.0.0 --port 8000

# Ejecutar pruebas unitarias con salida detallada
test:
	pytest -v

# Construir imagen Docker
docker-build:
	docker build -t $(DOCKER_IMAGE):$(DOCKER_TAG) .

# Correr contenedor Docker
docker-run:
	docker run -it --rm -p 8000:8000 $(DOCKER_IMAGE):$(DOCKER_TAG)

# Ejecutar pruebas dentro de Docker (opcional, si tienes test env en la imagen)
docker-test:
	docker run --rm $(DOCKER_IMAGE):$(DOCKER_TAG) pytest -v

# Ayuda
help:
	@echo "Comandos disponibles:"
	@echo "  install       -> Instala dependencias"
	@echo "  run           -> Inicia servidor con recarga automática"
	@echo "  run-prod      -> Inicia servidor sin recarga (producción)"
	@echo "  test          -> Ejecuta pruebas unitarias con pytest"
	@echo "  docker-build  -> Construye la imagen Docker"
	@echo "  docker-run    -> Ejecuta la app en un contenedor Docker"
	@echo "  docker-test   -> Ejecuta pruebas dentro del contenedor Docker (opcional)"
