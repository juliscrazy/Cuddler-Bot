"""Assigns the command name to the right function call."""
from bot.commands import cmd_clear, cmd_help

class commandSelector:
    def __init__(self, message):
        pass

    def clear(self, message):
        """Clears a given amount of messages from the invoke channel."""
        cmd_clear.run(message)

    def help(self, message):
        """Sends help text in invoke channel."""
        cmd_help.run(message)

CommandSelector = commandSelector