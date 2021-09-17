# `RichErr`

## BaseClass

> _class_ **richerr.RichErr**_(message: str | None, code: int | None, caused_by: BaseException | None, **kwargs)_

**Parameters:**

- **message** - Just a plain message to be sent with error. If no message provided, message will be resolved
  from default HTTP responses, with fallback to `self.DEFAULT_MESSAGE`
- **code** - error code. Default: `self.DEFAULT_CODE`
- **caused_by** - chain error. same as `raise Exception from previous_error`
- ****kwargs** - additional keyword arguments, which will be stored in **extras** attribute and shown in **error** dict

