'''
For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper class, which is a utility class helpful for querying paging information related to an array.

The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. The types of values contained within the collection/array are not relevant.

'''
class PaginationHelper:
    def __init__(self, coll, items):
      self.items = items
      self.coll  = coll
      self.paged = [coll[i:i+items] for i in range(0, len(coll)+1, items)]
    def item_count(self):
      return len(self.coll)    
  

    def page_count(self):
      return len(self.paged)
	
    def page_item_count(self, page_index):
      if page_index < 0: return -1
      try:
          return len(self.paged[page_index])
      except:
          return -1
  
    def page_index(self,item_index):
      if item_index > len(self.coll) - 1 or item_index < 0:
