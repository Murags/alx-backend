#!/usr/bin/env python3
"""pagination"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """_summary_

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Raises:
            AssertionError: _description_

        Returns:
            List[List]: _description_
        """
        if isinstance(page, int) and \
                isinstance(page_size, int) and page_size > 0 and page > 0:
            tp = index_range(page, page_size)
            data = self.dataset()
            return data[tp[0]:tp[1]]
        else:
            raise AssertionError


def index_range(page: int, page_size: int) -> tuple:
    """returns a tuple of page start and end

    Args:
        page (int): page number
        page_size (int): page sizes

    Returns:
        tuple: of start and end of page
    """
    start = page_size * (page - 1)
    end = page_size * page

    return (start, end)
