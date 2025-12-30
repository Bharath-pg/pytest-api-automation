# conftest.py
import pytest
from config.config import TOKEN
from utils.logger import get_logger

logger = get_logger()

@pytest.fixture
def auth_headers():
    return {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

@pytest.fixture(scope="function")
def setup_teardown():
    logger.info("🚀 Test Setup Started")
    yield
    logger.info("🧹 Test Teardown Completed")
