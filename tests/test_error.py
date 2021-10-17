from django.core.exceptions import ValidationError as DjangoValidationError
from pydantic import BaseModel
from pydantic.error_wrappers import ErrorWrapper, ValidationError as PydanticValidationError
from pytest import mark
from rest_framework.exceptions import ValidationError as DRFValidationError

import richerr


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
        PydanticValidationError([ErrorWrapper(ValueError('Hello world'), 'Loc')], BaseModel),
        {'error': {
            'caused_by': {'error': {
                'caused_by': None, 'code': 500, 'exception': 'ValidationError',
                'message': '1 validation error for BaseModel\nLoc\n  Hello world (type=value_error)'
            }},
            'code': 400,
            'exception': 'ValidationError',
            'message': '"Loc": Hello world',
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
