from test2 import A

class B(A):
    def show(self):
        print(self.get_instance.send_request())

B().show()