from config import version as config_version
from dataset.commands.commit import Commit
from dataset.commands.create import Create
from dataset.commands.download import Download

# from openxlab.dataset.commands.download import Download
from dataset.commands.get import Get
from dataset.commands.info import Info
from dataset.commands.ls import Ls
from dataset.commands.remove import Remove
from dataset.commands.upload_file import UploadFile
from dataset.commands.upload_folder import UploadFolder
from dataset.commands.visibility import Visibility
from dataset.handler.commit_dataset_info import commit
from dataset.handler.create_dataset_repository import create_repo
from dataset.handler.download_dataset_repository import download
from dataset.handler.get_dataset_repository import get
from dataset.handler.info_dataset_repository import info
from dataset.handler.list_dataset_repository import query
from dataset.handler.remove_dataset_repository import remove_repo
from dataset.handler.upload_dataset_file import upload_file
from dataset.handler.upload_dataset_folder import upload_folder
from dataset.handler.visible_dataset_repository import visibility
from types.command_type import *


def help():
    print("help")


class Dataset(BaseCommand):
    """Dataset Demo"""

    sub_command_list = [
        Get,
        Create,
        UploadFile,
        UploadFolder,
        Info,
        Ls,
        Commit,
        Download,
        Remove,
        Visibility,
    ]

    def get_name(self) -> str:
        return "dataset"

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.usage = "openxlab dataset [OPTIONS]\n\n"
        # parser.add_argument(
        #     "--test",
        #     help=(" This argument is a test argument"),
        # )
