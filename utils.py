import shutil
from player.utils import get_first_folder_name
import os
from player.config import config


def clean_tools(platform_key: str):
    """Clean up the tools directory by having only ffmpeg binary."""
    if platform_key == "nt":
        folder_path = os.path.join(
            config.tools_dir, get_first_folder_name(config.tools_dir)
        )
        # have only the bin folder, copy those files to tools dir, delete all
        bin_path = os.path.join(folder_path, "bin")
        # copy all the files in this bin folder to tools dir
        for item in os.listdir(bin_path):
            s = os.path.join(bin_path, item)
            d = os.path.join(config.tools_dir, item)
            if os.path.isdir(s):
                continue
            else:
                os.replace(s, d)
        shutil.rmtree(folder_path)

clean_tools("nt")