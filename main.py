import os
import discord
from dotenv import load_dotenv

class FoodBeast(discord.Client):
    """
    Class representing FoodBeast, the beast of food.
    """
    def __init__(self):
        """
        Constructor. Only necessary intent is the message content.
        """
        my_intents = discord.Intents.default()
        my_intents.message_content = True
        super().__init__(intents=my_intents)

        # Will be instantiated in on_ready
        # Type is optional GuildChannel, cannot import it for some reason
        self._channel = None

    async def on_ready(self) -> None:
        """
        Function for when FoodBeast is first started up.
        """
        guild_name = os.getenv('DISCORD_GUILD')
        guild = discord.utils.find(lambda guild: guild.name == guild_name, self.guilds)
        self._channel = discord.utils.find(lambda channel: channel.name == 'general', guild.channels)
        await self._channel.send('Hello! I am FoodBeast.')

    async def on_message(self, message) -> None:
        """
        Function for when a message is sent.
        :param message: The message that was sent.
        """
        if message.author == self.user:
            # Never want to reply to ourselves
            return

if __name__ == '__main__':
    """
    Main method.
    """
    load_dotenv()
    FoodBeast().run(os.getenv('DISCORD_TOKEN'))
