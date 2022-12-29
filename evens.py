def even_number_of_evens(numbers):

    """
    Should raise a TypeError if a list is not passed into the  function
    error message: "A list was not passed into the fucntion"
    if numbers is empty return False
    if the number of even numbers is odd, return false
    if the number of even number is 0, return false
    if the number of even numbers is even, return True
    """
    if isinstance(numbers, list):
        evens = 0

        evens = sum([1 for n in numbers if n % 2 == 0])

        return True if evens and evens % 2 == 0 else False

     
    else:
        raise TypeError("A list was not passed into the function")

if __name__ == '__main__':
    even_number_of_evens([2, 1, 4])