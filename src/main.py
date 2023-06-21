import asyncio
import aiohttp
import revolt
from revolt.ext import commands

class Zoo(commands.CommandsClient):
    async def get_prefix(self, message: revolt.Message):
        return "<@01H3FE4G5YYDSGPNJP7D9A03QT>"

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send("pong")

    async def main():
        async with aiohttp.ClientSession() as session:
            client = Client(session, "")
            await client.start()

if __name__ == "__main__":
    asyncio.run(Zoo.main())