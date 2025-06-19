from fastapi import APIRouter, status, Response
from typing import List
from app.models.event import Event
from app.services.event_service import filter_future_events, get_latest_event

router = APIRouter()

@router.post(
    "/process_events",
    status_code=status.HTTP_200_OK,
    summary="Procesar eventos y devolver el más lejano",
    response_model=Event,
    responses={
        200: {"description": "Evento más lejano encontrado"},
        204: {"description": "No hay eventos futuros"},
        422: {"description": "Error de validación en los datos enviados"}
    },
    tags=["Events"],
    description="""
Este endpoint recibe una lista de eventos con formato JSON, cada uno con `event_id`, `timestamp` y `data`.  
Filtra aquellos eventos cuyo `timestamp` sea igual o mayor a la hora actual (UTC) y retorna el evento con el timestamp más lejano.  
Si no hay eventos futuros, retorna un código 204.
"""
)
async def process_events(events: List[Event]):
    """
    Procesa una lista de eventos y retorna el más lejano en el tiempo.
    """
    future_events = filter_future_events(events)
    if not future_events:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    latest_event = get_latest_event(future_events)
    return latest_event

