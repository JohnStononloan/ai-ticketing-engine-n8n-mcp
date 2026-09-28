# FastMCP WMS Tool Specification

This service implements a Model Context Protocol (MCP) tool running via SSE transport to allow LLMs to query live warehouse/order data securely.

## Tool Definition
- **Tool Name:** `get_order_status`
- **Transport:** Server-Sent Events (SSE)
- **Port:** `8000`
- **Authentication:** Bearer Header Auth (`MCP_SECRET`)

## Input Parameters
| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `order_id` | string | Yes | Sanitized tracking or order reference ID (e.g., `ZAM/10928`). |

## Response Payload Structure
```json
{
  "order_id": "ZAM/10928",
  "status": "W trasie (Wydano do doręczenia)",
  "carrier": "InPost Paczkomaty",
  "tracking_number": "68801948201948",
  "estimated_delivery": "Jutro do godziny 14:00",
  "paid": true
}