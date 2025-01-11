def date_to_month(fecha: str) -> str:
    """
    Convierte una fecha en formato 'YYYY-MM-DD' al nombre del mes en español.
    
    Args:
        fecha (str): Fecha en formato 'YYYY-MM-DD'.
    
    Returns:
        str: Nombre del mes en español en mayúsculas.
    """
    meses = [
        "ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO",
        "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"
    ]
    try:
        # Extraer el mes de la fecha
        mes = int(fecha.split("-")[1])  # Segundo elemento es el mes
        return meses[mes - 1]  # Restar 1 porque las listas comienzan en índice 0
    except (IndexError, ValueError):
        raise ValueError("Formato de fecha inválido. Debe ser 'YYYY-MM-DD'.")

