import re
from rest_framework.serializers import ValidationError


class LinkVideoValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile('^https?://(?:www\.)?youtube\.com/.+$')
        tmp_val = dict(value).get(self.field)
        if tmp_val is not None and not bool(reg.match(tmp_val)):
            raise ValidationError('LinkVideo is not ok')
        if tmp_val is not None and 'youtube.com' not in tmp_val:
            raise ValidationError('Разрешены только ссылки на YouTube')
