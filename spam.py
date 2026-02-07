
import discord
from discord.ext import commands
import asyncio


class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        await self.tree.sync()
        print(" Commandes synchronisées")

bot = MyBot()


def get_ephemeral_embed():
    embed = discord.Embed(
        title="Action de Spam",
        description="clique sur le bouton ci-dessous pour lancer le spam dans ce salon",
        color=0x2b2d31
    )
    return embed


class SpamView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="SPAM",
        style=discord.ButtonStyle.danger,
        emoji="🚨"
    )
    async def spam_button_callback(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        spam_message = (
            "https://discord.gg/link\n" #enter your spam content
            "Spam messages\n\n"
        )

        
        final_message = spam_message * 2


        await interaction.response.send_message(
            content=final_message
        )



@bot.tree.command(
    name="spam",
    description="affiche un bouton pour spamme"
)
async def spam(interaction: discord.Interaction):
    await interaction.response.send_message(
        embed=get_ephemeral_embed(),
        view=SpamView(),
        ephemeral=True
    )


bot.run("YOUR TOKEN")
