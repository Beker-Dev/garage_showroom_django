from django.core.exceptions import ValidationError


def validate_password(password: str):
    required_length = 8
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_space = False
    if len(password) < required_length:
        raise ValidationError(f'Password must have at least {required_length} characters', code='min_length')
    else:
        for c in password:
            if c.islower():
                has_lowercase = True
            if c.isupper():
                has_uppercase = True
            if c.isdigit():
                has_digit = True
            if c.isspace():
                has_space = True
        else:
            if not has_lowercase or not has_uppercase or not has_digit or has_space:
                raise ValidationError(
                    f'Password must have at least one lowercase, uppercase, digit and no '
                    f'spaces', code='invalid'
                )
            else:
                return password


def compare_passwords(pw, pw2):
    pw_error = 'Password must be equal'
    if pw != pw2:
        raise ValidationError({'password': pw_error, 'password2': pw_error})
