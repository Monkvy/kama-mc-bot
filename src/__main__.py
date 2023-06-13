import discord
from discord import app_commands
from discord.ext import commands
import process


if __name__ == "__main__":
    bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        print(f"{bot.user} is now online")
        try:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(e)

    @bot.tree.command(name="open")
    @app_commands.describe(pid="PID")
    @app_commands.describe(input="input")
    async def open(interaction: discord.Interaction, pid: int, input: str):
        proc = process.open(pid)
        output, error = proc.communicate(input=input)

        await interaction.response.send_message(f"output: {output} ;; error: {error}")


    with open("TOKEN", "r") as fr:
        bot.run(fr.read())
