import pytest

from app.config import get_environment


def test_default_environment(monkeypatch):
    """Test that the default environment is 'development' when PORTFOLIO_ENV is not set."""
    monkeypatch.delenv("PORTFOLIO_ENV", raising=False)

    assert get_environment() == "development"


@pytest.mark.parametrize("env_value, expected",
                         [("Test", "test"),
                          ("PRODUCTION", "production"),
                          (" Development ", "development")]
                         )
def test_valid_environment_normalized(env_value, expected, monkeypatch):
    """Test that valid environments are returned correctly."""
    monkeypatch.setenv("PORTFOLIO_ENV", env_value)

    assert get_environment() == expected


@pytest.mark.parametrize("env_value", ["invalid", "staging", "  "])
def test_invalid_environment(env_value, monkeypatch):
    """Test that invalid environment values raise a ValueError."""
    monkeypatch.setenv("PORTFOLIO_ENV", env_value)

    with pytest.raises(ValueError, match="Invalid PORTFOLIO_ENV"):
        get_environment()
