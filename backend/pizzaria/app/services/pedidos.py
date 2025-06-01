import asyncio
import logging

async def processar_pedido(pedido_id):
    logging.info(f"Iniciando processamento do pedido {pedido_id}...")
    await asyncio.sleep(2)
    logging.info(f"Pedido {pedido_id} processado com sucesso.")
