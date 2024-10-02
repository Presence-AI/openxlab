from types.command_type import *
from model.commands.download import Download
from model.commands.wget import Wget
from model.commands.upload import Upload
from model.commands.init import Init
from model.commands.create import Create
from model.commands.list import List
from model.commands.visibility import Visibility
from model.commands.remove import Remove
from model.commands.inference import Inference


class Model(BaseCommand):
    """model"""

    sub_command_list = [Upload, Download, Init, Create, List, Visibility, Remove, Inference, Wget]

    def get_name(self) -> str:
        return "model"

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            "--foo",
            type=str,
            help=(
                "this is an argument for test"
            ),
        )

    def take_action(self, parsed_args: Namespace) -> int:
        pass
