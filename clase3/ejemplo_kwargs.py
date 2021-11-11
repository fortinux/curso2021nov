# Ejemplo kwargs
def test_kwargs(**kwargs):
    for key, value in kwargs.items():
        print('{0} = {1}'.format(key, value))


kwargs = {'tres':3, 'cinco':5}

test_kwargs(**kwargs)