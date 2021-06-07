## @module MyModule1.py
# Documentation for MyModule 1
#
# More information can come here.

class dog:

    """
    Class that contains a dog object
    
    This class represent a dog object.
    
    :var name: The name of the dog
    :var breed: The type of dog
    
    """

    def __init__(self, name, breed):
    
        self.name = name
        self.breed = breed
        
    def call(self):
        """
        class method that calls a dog.
        """
        print('Come here, {}!!'.format(self.name))
        
        

def read_dogs(file):
    """
    function that reads in a list of dogs.
    
    The list of docs must be formatted into two columns,
    with the names of the dogs in the first column,
    and the breed of the dogs in the second column.
    
    :param file: the file containing the dog information
    :rtype: returns a list of :class:`dog`.
    """

    pass
