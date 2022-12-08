# from .a import A
# from .b import B
'''
One extension of this recipe involves the introduction of “lazy” imports. As shown, the
__init__.py file imports all of the required subcomponents all at once. However, for a
very large module, perhaps you only want to load components as they are needed. To
do that, here is a slight variation of __init__.py:
'''
def A():
    from .a import A
    return A()
def B():
    from .b import B
    return B()