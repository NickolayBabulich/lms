from rest_framework.serializers import ValidationError


class LinkToVideoValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_value = dict(value).get(self.field)
        print(tmp_value)
        if 'www.youtube.com' not in tmp_value and 'youtube.com' not in tmp_value:
            raise ValidationError("Ссылки допустимы только на YouTube!")
