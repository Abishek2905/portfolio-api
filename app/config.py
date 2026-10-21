import os

ALLOWED_ENVIRONMENTS = {"development", "test", "production"}


def get_environment() -> str:
    """
    This method helps get the current environment for the application.
    It checks the PORTFOLIO_ENV environment variable and returns its value. If the variable is not set, it defaults to 'development'.
    It also validates that the environment is one of the allowed values: 'development', 'test', or 'production'. If the value is invalid, it raises a ValueError."""

    current_env = os.getenv("PORTFOLIO_ENV", "development").strip().lower()

    if current_env not in ALLOWED_ENVIRONMENTS:
        raise ValueError(f'Invalid PORTFOLIO_ENV: {current_env}. '
                         f'Expected development, test, or production.')

    return current_env
