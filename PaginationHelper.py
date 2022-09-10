# TODO: complete this class
import codewars_test as test
import math


class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.__list = collection
        self.__per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.__list)

    # returns the number of pages
    def page_count(self):
        return math.ceil(self.item_count() / self.__per_page)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):

        def is_last_page(idx):
            return idx == self.page_count() - 1

        if page_index > self.page_count() - 1:
            return -1
        if is_last_page(page_index):
            if self.item_count() % self.__per_page == 0:
                return self.__per_page
            else:
                return self.item_count() % self.__per_page
        else:
            return self.__per_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        page = math.floor(item_index / self.__per_page)
        if 0 <= page <= self.page_count() - 1 and 0 <= item_index <= self.item_count()-1:
            return page
        else:
            return -1

collection = range(1,25)
helper = PaginationHelper(collection, 10)

test.assert_equals(helper.page_count(), 3, 'page_count is returning incorrect value.')
test.assert_equals(helper.page_index(24), -1, 'page_index returned incorrect value')
test.assert_equals(helper.item_count(), 24, 'item_count returned incorrect value')