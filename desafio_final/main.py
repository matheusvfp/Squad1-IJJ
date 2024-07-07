import functions as func
import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        usuario_criado = await func.criar_usuario(session)
        if usuario_criado is None:
            sys.exit('Falha na criação do usuário. Encerrando o programa.')

        token_acesso = await func.fazer_login(session, usuario_criado)
        if token_acesso is None:
            sys.exit('Falha no login. Encerrando o programa.')

        df = func.gerar_dataframe(token_acesso)
        if df is None:
            sys.exit('Falha na criação do DataFrame. Encerrando o programa.')

        print(df)

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
