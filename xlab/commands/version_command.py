import sys

from config import version as config_version
from types.command_type import *
from xlab.handler.user_token import update_version_check


class Version(BaseCommand):
    """Get Openxlab Version"""

    def get_name(self) -> str:
        return "version"

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            '--update-check',
            required=False,
            action='store_true',
            help='get the latest version of openxlab cli',
        )

    def take_action(self, parsed_args: Namespace) -> int:
        check_version = parsed_args.update_check
        if not check_version:
            print("OpenXLab %s" % config_version.version)
        else:
            try:
                # update check
                current_version, latest_version, is_latest_version = update_version_check()
            except Exception as e:
                print(f"{e}")
                return

            # current_version < latest_version
            if not is_latest_version:
                print(
                    f"You are using openxlab version {current_version}; however, version {latest_version} is available. Consider using 'pip install -U openxlab' to avoid version compatibility problems."
                )
            #  current_version >= latest_version
            else:
                print(
                    f"You are using openxlab version {current_version}, it is already the latest version."
                )
        return 0
