# Process Events API

Una API construida con **FastAPI** que recibe una lista de eventos, filtra los que ocurrirán en el futuro y retorna el evento más lejano (con el `timestamp` más alto en formato epoch UTC).

---

## Características

- Procesa eventos con `timestamp` en formato epoch (UTC).
- Filtra los eventos futuros respecto al tiempo actual.
- Devuelve el evento más lejano.
- Soporte completo para pruebas con `pytest`.
- Preparada para ejecución local y en Docker.

---

## Endpoints

### `POST /v1/process_events`

Procesa una lista de eventos y devuelve el evento con el `timestamp` más alto (futuro).

####  Request Body (JSON)

[
  {
    "event_id": "evento_1",
    "timestamp": 1737172800,
    "data": "Datos del evento 1"
  },
  {
    "event_id": "evento_2",
    "timestamp": 1737172801,
    "data": "Datos del evento 2"
  },
  {
    "event_id": "evento_3",
    "timestamp": 1737172802,
    "data": "Datos del evento 3"
  }
]

 Respuestas posibles
200 OK: Devuelve el evento más lejano.

204 No Content: No hay eventos futuros en la

Requisitos
Python 3.11+

pip

Make (opcional, para automatizar comandos)

## Instalación local

Editar
git clone https://github.com/libardo24/fastapi_process_events.git
cd fastapi_process_events

python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Iniciar la aplicación
make run
# o directamente
uvicorn app.main:app --reload

##Ejecutar pruebas
pytest -v
# o usando Make
make test

Uso con Docker
Asegúrate de tener Docker instalado y en funcionamiento.

bash
Copiar
Editar
# Construir imagen
make docker-build

# Ejecutar contenedor
make docker-run
# La API estará disponible en: http://localhost:8000

# Ejecutar pruebas dentro del contenedor
make docker-test

fastapi_process_events/
├── app/
│   ├── core/           # Configuración global (settings)
│   ├── models/         # Modelos Pydantic
│   ├── services/       # Lógica de negocio
│   ├── routers/        # Endpoints (APIRouter)
│   └── main.py         # Punto de entrada FastAPI
├── tests/              # Pruebas unitarias
├── requirements.txt
├── Makefile
└── README.md
