from argparse import Namespace

from types.command_type import BaseCommand
from xlab.handler import user_token


class Token(BaseCommand):
    """Print token"""

    def get_name(self) -> str:
        return "token"

    def take_action(self, parsed_args: Namespace):
        print(user_token.get_jwt())
