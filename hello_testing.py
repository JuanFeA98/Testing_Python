'''Hello, Testing!'''

def calculate_total(products):
    '''
    Realiza la suma sobre una lista de productos
    '''
    total = 0
    for product in products:
        total += product['price']

    return total

def test_calculate_total_with_empty_list():
    '''
    Test para la función "calculate_total" cuanto la lista esta vacia.
    '''
    assert calculate_total([]) == 0


def test_calculate_total_with_single_product():
    '''
    Test para la función "calculate_total" cuanto la lista solo tiene un registro.
    '''
    products = [
        {
            'name': 'Notebook',
            'price': 10000
        }
    ]

    assert calculate_total(products) == 10000

def test_calculate_total_with_multiple_product():
    '''
    Test para la función "calculate_total" cuanto la lista tiene varios registros.
    '''
    products = [
        {
            'name': 'Notebook',
            'price': 10000
        },
        {
            'name': 'Pencil',
            'price': 2000
        },
        {
            'name': 'Book',
            'price': 40000
        }
    ]

    assert calculate_total(products) == 52000


if __name__ == '__main__':
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product()
