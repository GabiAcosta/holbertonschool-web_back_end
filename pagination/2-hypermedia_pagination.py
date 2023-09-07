#!/usr/bin/env python3
"""
This script defines a Server class for paginating a database of
popular baby names.
"""
import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """
    Calculate the range of indices to retrieve a specific page of data.
    """
    return ((page - 1) * page_size, page_size * page)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of data from the database.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        index = index_range(page, page_size)
        first = index[0]
        last = index[1]
        return self.dataset()[first:last]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieve a page of data with hypermedia information.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        if page + 1 < total_pages:
            next_page = page + 1
        else:
            next_page = None

        if page != 1:
            prev_page = page - 1
        else:
            prev_page = None

        return {
            "page_size": len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
