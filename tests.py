import os
import pytest
from dataikuapi import DSSClient

# Environment variables
DATAIKU_INSTANCE_URL = os.getenv('DATAIKU_INSTANCE_URL')
DATAIKU_API_KEY = os.getenv('DATAIKU_API_KEY')
DATAIKU_PROJECT_KEY = os.getenv('DATAIKU_PROJECT_KEY')

# Fixture for the Dataiku client
@pytest.fixture
def dss_client():
    return DSSClient(DATAIKU_INSTANCE_URL, DATAIKU_API_KEY, no_check_certificate=True)

# Fixture for the project
@pytest.fixture
def project(dss_client):
    return dss_client.get_project(DATAIKU_PROJECT_KEY)

def test_compute_recipe(project):
    """Test that the compute_test recipe runs successfully"""
    recipe = project.get_recipe('compute_test')
    try:
        recipe.run(wait=True, no_fail=False)
        assert True
    except Exception as e:
        pytest.fail(f"Recipe execution failed: {e}") 