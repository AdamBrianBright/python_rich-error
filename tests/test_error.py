from django.core.exceptions import ValidationError as DjangoValidationError
from pydantic import BaseModel, ValidationError as PydanticValidationError, constr
from pytest import mark
from rest_framework.exceptions import ValidationError as DRFValidationError

import richerr


class HelloWorld(BaseModel):
    hello: constr(min_length=24)


pydanticValidationError: PydanticValidationError = PydanticValidationError.from_exception_data('', [])
try:
    HelloWorld.model_validate({'hello': 'world!'})
except PydanticValidationError as _err:
    pydanticValidationError = _err
    del _err


@mark.parametrize('inp, res', (
        (
                ValueError('Hello world'),
                {'error': {
                    'code': 400,
                    'exception': 'BadRequest',
                    'message': 'Hello world',
                    'caused_by': {'error': {
                        'code': 400, 'exception': 'ValueError', 'message': 'Hello world', 'caused_by': None,
                    }},
                }}
        ),
        (
                pydanticValidationError,
                {'error': {
                    'caused_by': {'error': {
                        'caused_by': None,
                        'code': 500,
                        'exception': 'ValidationError',
                        'message': '1 validation error for '
                                   'HelloWorld\n'
                                   'hello\n'
                                   '  String should have at least '
                                   '24 characters '
                                   '[type=string_too_short, '
                                   "input_value='world!', "
                                   'input_type=str]\n'
                                   '    For further information '
                                   'visit '
                                   'https://errors.pydantic.dev/2.4/v/string_too_short',
                    }},
                    'code': 400,
                    'exception': 'ValidationError',
                    'message': '"hello": String should have at least 24 characters',
                }}
        ),
        (
                DjangoValidationError('Message', code=304),
                {'error': {
                    'caused_by': {'error': {
                        'caused_by': None, 'code': 406, 'exception': 'ValidationError', 'message': "['Message']"
                    }},
                    'code': 406,
                    'exception': 'NotAcceptable',
                    'message': 'Message',
                }}
        ),
        (
                DRFValidationError('Detail', code=304),
                {'error': {
                    'caused_by': {'error': {
                        'caused_by': None, 'code': 406, 'exception': 'ValidationError',
                        'message': "[ErrorDetail(string='Detail', "'code=304)]'
                    }},
                    'code': 406,
                    'exception': 'NotAcceptable',
                    'message': 'Detail',
                }}
        ),
))
def test_conversion(inp, res):
    assert richerr.RichErr.convert(inp).dict() == res


@mark.parametrize('err', (
        richerr.RichErr(),
))
def test_is_hashable(err):
    assert hash(err)
