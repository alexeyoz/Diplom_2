class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'
    CREATE_USER = BASE_URL + 'api/auth/register'
    LOGIN_USER = BASE_URL + 'api/auth/login'
    AUTH_USER = BASE_URL + 'api/auth/user'
    ORDER = BASE_URL + 'api/orders'


class ErrorMessage:
    USER_EXISTS = 'User already exists'
    NOT_ALL_FIELDS = 'Email, password and name are required fields'
    INCORRECT_LOGIN_PASSWORD = 'email or password are incorrect'
    NOT_AUTHORIZED = 'You should be authorised'
    INGREDIENTS_NOT_PROVIDED = 'Ingredient ids must be provided'
    INGREDIENTS_PROVIDED_INCORRECT = 'One or more ids provided are incorrect'


class Ingredients:
    INGREDIENTS = "61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6c", "61c0c5a71d1f82001bdaaa71"

