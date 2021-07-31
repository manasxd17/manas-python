def conCat(*args):
    result = {}
    for arg in args:
        result.update(arg)
    return result

a = conCat(
{1:10,2:20},
{3:30,4:40},
{5:50,6:60})
print(a)
