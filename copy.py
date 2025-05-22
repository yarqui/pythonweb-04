import sys
import argparse
import aioshutil
from colorama import Fore, Style




# def copy_and_sort_files(source_dir: Path, destination_dir: Path) -> None:
#     """
#     Recursively copy files from source_dir into destination_dir,
#     sorting them into subfolders by file extension.
#     """
#     try:
#         for item in source_dir.iterdir():
#             if item.is_dir():
#                 copy_and_sort_files(item, destination_dir)
#             elif item.is_file():
#                 try:
#                     # Check read access
#                     if not is_readable(item):
#                         print(f"{Fore.YELLOW}Skipping unreadable file: {item}")
#                         continue

#                     ext = item.suffix[1:] if item.suffix else "no_extension"

#                     # Create destination subfolder
#                     target_dir = destination_dir / ext
#                     target_dir.mkdir(parents=True, exist_ok=True)

#                     # Copy file
#                     shutil.copy2(item, target_dir)
#                     print(
#                         f"{Fore.GREEN}Copied: {Fore.WHITE}{item} > {Fore.GREEN}{target_dir}"
#                     )

#                 except Exception as e:
#                     print(f"{Fore.RED}Failed to copy {item}: {e}")
#     except Exception as e:
#         print(f"{Fore.RED}Error accessing directory {source_dir}: {e}")


# def parse_arguments():
#     """
#     Parse CLI arguments and return source and destination paths.
#     """
#     if len(sys.argv) < 2:
#         print(f"{Fore.RED}Usage: python script.py <source_dir> [destination_dir]")
#         sys.exit(1)

#     path_source = Path(sys.argv[1])
#     path_destination = (
#         Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist").resolve()
#     )

    # if not path_source.exists():
    #     print(f"{Fore.RED}Error: Source path does not exist.")
    #     sys.exit(1)
    # if not path_source.is_dir():
    #     print(f"{Fore.RED}Error: Source path is not a directory.")
    #     sys.exit(1)

    # path_destination.mkdir(parents=True, exist_ok=True)

    # return path_source, path_destination


# def is_readable(path: Path) -> bool:
#     """
#     Check if a file at the given path is readable.

#     This function attempts to open the file in binary read mode ("rb").
#     If the file can be opened successfully, it is considered readable.
#     If an exception occurs (e.g., due to missing permissions, file locking, or corruption),
#     the function returns False.

#     Args:
#         path (Path): The path to the file to check.

#     Returns:
#         bool: True if the file is readable, False otherwise.
#     """
#     try:
#         with open(path, "rb"):
#             return True
#     except Exception:
#         return False


