import sys
import argparse
import asyncio
import logging
from typing import Tuple
from aioshutil import copy2
from aiopath import AsyncPath
from time import time

# Logger config
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_paths_from_args() -> Tuple[str, str]:
    parser = argparse.ArgumentParser(
        description="Asynchronously sorts files by extension into target directories."
    )
    parser.add_argument(
        "--src",
        type=str,
        default=".",
        help="Path to the source folder to read files from (default: current directory)",
    )
    parser.add_argument(
        "--dest",
        type=str,
        default="./sorted_files",
        help="Path to the destination folder where sorted files will be moved (default: ./sorted_files)",
    )

    args = parser.parse_args()
    return args.src, args.dest


async def read_folder(source_dir: AsyncPath, destination_dir: AsyncPath) -> None:
    tasks = []
    async for item in source_dir.iterdir():
        if await item.is_dir():
            await read_folder(item, destination_dir)

        elif await item.is_file():
            task = asyncio.create_task(copy_file(item, destination_dir))
            tasks.append(task)

    if tasks:
        await asyncio.gather(*tasks)


async def copy_file(file_path: AsyncPath, destination_folder: AsyncPath) -> None:
    try:
        extension = file_path.suffix[1:] if file_path.suffix else "no_extension"
        extension = extension.replace("/", "_")
        target_dir = destination_folder / extension

        await target_dir.mkdir(parents=True, exist_ok=True)
        await copy2(file_path, target_dir)

        logging.info("Successfully copied: %s to %s", file_path.name, target_dir)

    except FileNotFoundError:
        logging.error("Failed to copy %s: Source file not found.", file_path)
    except PermissionError:
        logging.error(
            "Failed to copy %s: Permission denied to access source or destination.",
            file_path,
        )
    except OSError as e:
        logging.error("Failed to copy %s due to OS error: %s", file_path, e)
    except Exception as e:
        logging.error("An unexpected error occurred while copying %s: %s", file_path, e)


async def main():
    start = time()

    source_str, destination_str = get_paths_from_args()
    source_path: AsyncPath = AsyncPath(source_str)
    destination_path: AsyncPath = AsyncPath(destination_str)

    if not await source_path.exists():
        logging.error("Source path %s does not exist", source_path)
        sys.exit(1)

    if not await source_path.is_dir():
        logging.error("Source path %s is not a directory", source_path)
        sys.exit(1)

    try:
        await destination_path.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        logging.error(
            "Error creating destination directory %s: %s", destination_path, e
        )
        sys.exit(1)

    logging.info('Start sorting files from "%s" to "%s"', source_path, destination_path)

    await read_folder(source_path, destination_path)

    logging.info("DONE in %s", start - time())


if __name__ == "__main__":
    asyncio.run(main())
