from pytest import mark

import richerr


@mark.parametrize('inp, res', (
        (ValueError('Hello world'), {'error': {
            'code': 400,
            'exception': 'BadRequest',
            'message': 'Hello world',
            'caused_by': {'error': {
                'code': 400, 'exception': 'ValueError', 'message': 'Hello world', 'caused_by': None,
            }},
        }}),
))
def test_conversion(inp, res):
    assert richerr.RichErr.convert(inp).dict() == res
