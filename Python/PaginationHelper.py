# For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper class, which is a utility class helpful for querying paging information related to an array.

# The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. The types of values contained within the collection/array are not relevant.

# The following are some examples of how this class is used:

# helper = PaginationHelper(['a','b','c','d','e','f'], 4)
# helper.page_count() # should == 2
# helper.item_count() # should == 6
# helper.page_item_count(0) # should == 4
# helper.page_item_count(1) # last page - should == 2
# helper.page_item_count(2) # should == -1 since the page is invalid

# # page_index takes an item index and returns the page that it belongs on
# helper.page_index(5) # should == 1 (zero based index)
# helper.page_index(2) # should == 0
# helper.page_index(20) # should == -1
# helper.page_index(-10) # should == -1 because negative indexes are invalid


class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        
    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
        
    
    # returns the number of pages
    def page_count(self):
        pages = []
        index1 = 0
        
        if len(self.collection) == 0:
            return 0
        
        while index1 <= len(self.collection) - 1:
            pages.append(self.collection[index1 : index1 + self.items_per_page])
            index1 += self.items_per_page
        
        return len(pages)
        
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        pages = []
        index1 = 0

        if not self.collection:
            return -1

        while index1 <= len(self.collection) - 1:
            pages.append(self.collection[index1 : index1 + self.items_per_page])
            index1 += self.items_per_page

        if page_index < len(pages) and page_index >= 0:
            return len(pages[page_index])
        else:
            return -1
        
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        item = -1
        if item_index < len(self.collection) and item_index >= 0 and self.collection:
            item = self.collection[item_index]
        else:
            return item
        
        page_index = 0
        index1 = 0
        
        while index1 <= len(self.collection):
            page = self.collection[index1 : index1 + self.items_per_page]
            if item in page and item_index >= index1 and item_index <= index1 + self.items_per_page:
                return page_index
            index1 += self.items_per_page
            page_index += 1




# helper = PaginationHelper(['a','b','c','d','e','f'], 4)

# print(helper.item_count()) # 6
# print(helper.page_count()) # 2
# print(helper.page_item_count(0)) # 4
# print(helper.page_item_count(1)) # 2
# print(helper.page_item_count(2)) # -1
# print(helper.page_index(5)) # 1
# print(helper.page_index(2)) # 0
# print(helper.page_index(20)) # -1
# print(helper.page_index(-10)) # -1

# empty = PaginationHelper([], 10)
# print(empty.item_count()) # 0
# print(empty.page_count()) # 0
# print(empty.page_index( 0)) # -1
# print(empty.page_index( 1)) # -1
# print(empty.page_index(-1)) # -1
# print(empty.page_item_count(0)) # -1
# print(empty.page_item_count(1)) # -1
# print(empty.page_item_count(-1)) # -1

# edge1 = PaginationHelper([1,2,3,4], 1)

# print(edge1.page_count()) # 4

# edge4 = PaginationHelper([1,2,3,4], 4)

# print(edge4.page_count()) # 1
# print(edge4.page_item_count(1)) # -1

edge37 = PaginationHelper([1,2,3,4,5,6,7,8,9,10,34,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37], 6)

print(edge37.page_index(33)) # 5

#####
# class PaginationHelper:
#     def __init__(self, collection, items_per_page):
#         self._item_count = len(collection)
#         self.items_per_page = items_per_page

#     def item_count(self):
#         return self._item_count

#     def page_count(self):
#         return -(self._item_count // -self.items_per_page)

#     def page_item_count(self, page_index):
#         return min(self.items_per_page, self._item_count - page_index * self.items_per_page) \
#             if 0 <= page_index < self.page_count() else -1

#     def page_index(self, item_index):
#         return item_index // self.items_per_page \
#             if 0 <= item_index < self._item_count else -1

#####
# class PaginationHelper:

#     # The constructor takes in an array of items and a integer indicating
#     # how many items fit within a single page
#     def __init__(self, collection, items_per_page):
#         self.collection = collection
#         self.items_per_page = items_per_page

#     # returns the number of items within the entire collection
#     def item_count(self):
#         return len(self.collection)

#     # returns the number of pages
#     def page_count(self):
#         return 1+(self.item_count() // self.items_per_page)

#     # returns the number of items on the current page. page_index is zero based
#     # this method should return -1 for page_index values that are out of range
#     def page_item_count(self, page_index):
#         # Covers all full pages
#         if page_index+1 < self.page_count():
#             return self.items_per_page
#         # The last page
#         elif page_index+1 == self.page_count():
#             return (self.item_count() % self.items_per_page)
#         else:
#             return -1

#     # determines what page an item is on. Zero based indexes.
#     # this method should return -1 for item_index values that are out of range
#     def page_index(self, item_index):
#         if item_index >= 0:
#             if self.item_count() >= (item_index+1):
#                 return (item_index+1) // self.items_per_page
#         return -1


#####
# class PaginationHelper:
#     def __init__(self, collection, items_per_page):
#         self.coll = collection
#         self.item = items_per_page
#         self.a, self.b = divmod(self.item_count(), self.item)

#     def item_count(self):
#         return len(self.coll)

#     def page_count(self):
#         return self.a + bool(self.b)

#     def page_item_count(self, page_index):
#         if page_index in range(self.page_count()):
#             return [self.b, self.item][page_index < self.a]
#         return -1

#     def page_index(self, item_index):
#         if item_index in range(self.item_count()):
#             return item_index // self.item
#         return -1

#####
# class PaginationHelper:
    
#     # The constructor takes in an array of items and an integer indicating
#     # how many items fit within a single page
#     def __init__(self, collection, items_per_page):
#         self.collection = collection 
#         self.items_per_page = items_per_page
#         self.pages = [self.collection[i:i+self.items_per_page] for i in range(0,len(self.collection),self.items_per_page)]
    
#     # returns the number of items within the entire collection
#     def item_count(self):
#         return len(self.collection)
    
#     # returns the number of pages
#     def page_count(self):
#         return len(self.pages)
    
#     # returns the number of items on the given page. page_index is zero based
#     # this method should return -1 for page_index values that are out of range
#     def page_item_count(self, page_index):
#         return -1 if page_index > len(self.pages)-1 or page_index < 0 else len(self.pages[page_index])
    
#     # determines what page an item at the given index is on. Zero based indexes.
#     # this method should return -1 for item_index values that are out of range
#     def page_index(self, item_index):
#         return -1 if len(self.collection)-1 < item_index or item_index < 0 else item_index//self.items_per_page