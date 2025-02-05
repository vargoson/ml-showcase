# src/my_app/utils/path_util.py
import os

def get_asset_path(asset_filename: str) -> str:
    """
    Returns the absolute path to an asset located in the
    'my_app/webpages/assets' directory.
    """
    # Get the directory of the current file (i.e. .../src/my_app/utils)
    utils_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to the 'my_app' directory.
    my_app_dir = os.path.abspath(os.path.join(utils_dir, ".."))
    # Then navigate to 'webpages/assets'
    asset_dir = os.path.join(my_app_dir, "webpages", "assets")
    # Return the full path to the asset file.
    return os.path.join(asset_dir, asset_filename)
