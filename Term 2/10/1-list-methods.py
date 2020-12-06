bascket = ['banana', 'banana', 'maedeh', 'apple', 'kiwi', 'strawberry', 'maedeh']

# تعداد دفعات تکرار یک عضو را به ما برمیگرداند
# 1
count = bascket.count('banana')
print(count)
# 2
print(bascket.count('banana'))

# شماره پلاک عضو را بر میگرداند
# 1
index = bascket.index('maedeh')
print(index)
# 2
print(bascket.index('maedeh'))

#  عضو جدید به شماره پلاک مورد نظر اضافه میکند
print(bascket)
bascket.insert(2, 'kiwi')
print(bascket)