from client.client import size_transmission_unit


def test_size_transmission_unit():
    quantity, unit = size_transmission_unit(3, 1)
    assert quantity == 3
    assert unit == 'bytes/s'

    quantity, unit = size_transmission_unit(199, 1.6)
    assert unit == 'bytes/s'

    quantity, unit = size_transmission_unit(200, 1.6)
    assert quantity == 1.0
    assert unit == 'kbps'

    quantity, unit = size_transmission_unit(199_999, 1.6)
    assert unit == 'kbps'

    quantity, unit = size_transmission_unit(200_000, 1.6)
    assert quantity == 1.0
    assert unit == 'mbps'
