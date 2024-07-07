import function as func
import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        usuario_criado = await func.criar_usuario(session)
        
        token_acesso = await func.fazer_login(session, usuario_criado)
        
        df = func.gerar_dataframe(token_acesso)

        print(df)

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
