"""
Run sources.
"""
import asyncio

from sources.lib.helpers.args_helper import get_arguments
from sources.lib.helpers.log_helper import init_logger
from sources.lib.histogram import (build_histogram, process_data)


async def main():
    """
    Run Histogrammer.
    :return: None
    """
    arguments = await get_arguments()
    await init_logger(folder_name=".logs", root_path=arguments.log)
    words_count = await process_data(extension="*.txt", path=arguments.path)
    await build_histogram(words_count)


if __name__ == "__main__":
    asyncio.run(main())
