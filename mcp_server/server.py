import os
import secrets
import string
from fastmcp import FastMCP

# Pobieramy sekret ze zmiennej środowiskowej
MCP_SECRET = os.getenv("MCP_SECRET")
if not MCP_SECRET:
    raise RuntimeError("Brak zdefiniowanej zmiennej środowiskowej MCP_SECRET!")

# Inicjalizacja serwera FastMCP
mcp = FastMCP("mcp-wms")


@mcp.tool()
def get_order_status(order_id: str) -> dict:
    """Sprawdza status zamówienia lub przesyłki w systemie WMS/e-commerce.

    Użyj tego narzędzia, gdy klient podaje numer zamówienia lub paczki i pyta o
    jej status.
    """
    clean_id = order_id.strip().upper()
    random_tracking = "".join(secrets.choice(string.digits) for _ in range(10))

    return {
        "order_id": clean_id,
        "status": "W trasie (Wydano do doręczenia)",
        "carrier": "InPost Paczkomaty",
        "tracking_number": f"6880{random_tracking}",
        "estimated_delivery": "Jutro do godziny 14:00",
        "paid": True,
    }


if __name__ == "__main__":
    # Uruchamiamy natywny transport SSE dla n8n na porcie 8000
    mcp.run(transport="sse", host="0.0.0.0", port=8000)