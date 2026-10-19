
# Exercise 1
# The members would be refrenced, because their information can be shown
# independently of any books. The reviews are a more complex case, but I 
# would make them a reference, since we might want to show all the reviews
# that some particular member has written.


# Exercise 2
# Advantage: An order can be displayed without a second lookup into `products`. 
# The copy also keeps the order a faithful historical record: if the product 
# is later renamed or discontinued, old orders still show what the customer 
# actually bought.
# Disadvantage: The name is stored in many places, so it can go out of sync. 
# If a product's name is corrected, say a typo fix, every existing order keeps 
# the old name unless we update them all.
