import os

class Root:
  @staticmethod
  def join(*paths: str) -> str:
    return os.path.join(Root._get_root_path(), *paths)

  @staticmethod
  def assets(*paths: str) -> str:
    return os.path.join(Root._get_root_path(), 'assets/', *paths)

  @staticmethod
  def out(*paths: str) -> str:
    return os.path.join(Root._get_root_path(), 'out/', *paths)

  @staticmethod
  def _get_root_path() -> str:
    lib_dir_path = os.path.dirname(os.path.abspath(__file__))
    src_dir_path = os.path.dirname(lib_dir_path)
    root_dir_path = os.path.dirname(src_dir_path)

    return root_dir_path
