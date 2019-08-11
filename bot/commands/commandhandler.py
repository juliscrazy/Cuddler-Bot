"""Assigns the command name to the right function call."""
from bot.commands import cmd_clear, cmd_help

class commandSelector:
    async def __init__(self, message):
        pass

    async def clear(self, message):
        """Clears a given amount of messages from the invoke channel."""
        await cmd_clear.run(message)

    async def help(self, message):
        """Sends help text in invoke channel."""
        await cmd_help.run(message)

CommandSelector = commandSelector