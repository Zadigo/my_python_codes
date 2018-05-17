def v(self,r):
    print(r)

def z(self):
    print('g')

def class_factory(class_name, *methods):
    method_dict = {}

    for method in methods:
        if callable(method):
            method_dict[method.__name__] = method
        
        else:
            print('%s is not callable. Received %s' % (method, method.__class__,))
        
    # Create class
    custom_class = type(class_name, (), method_dict)

    return custom_class

NewClass=class_factory('A',v,z)
i=NewClass()
i.v('prit')