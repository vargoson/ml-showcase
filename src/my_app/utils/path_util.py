import os

def get_asset_path(asset_filename: str) -> str:

    """
    Returns the absolute path to an asset located in the
    'my_app/webpages/assets' directory.

    """
    utils_dir = os.path.dirname(os.path.abspath(__file__))
    my_app_dir = os.path.abspath(os.path.join(utils_dir, ".."))
    asset_dir = os.path.join(my_app_dir, "webpages", "assets")
    return os.path.join(asset_dir, asset_filename)
