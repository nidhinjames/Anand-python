foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print "-:::LIST:::-"
print foo
print ""
print "-:::FILTER:::-"
print filter(lambda x:x%3 == 0, foo)
print ""
print "-:::MAP:::-"
print map(lambda x:x+2+10, foo)
print ""
print "-:::REDUCE:::-"
print reduce(lambda x,y:x+y, foo)
