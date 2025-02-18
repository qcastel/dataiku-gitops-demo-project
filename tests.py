import os
import sys
import time

from dataikuapi import DSSClient

# Environment variables
DATAIKU_API_TOKEN = os.getenv('DATAIKU_API_TOKEN')

def run_tests(instance_url, api_key, project_key):
    # Implment the tests suits of your choice. Here for the demo, we simply run a recipe
    client = DSSClient(instance_url, api_key, no_check_certificate=True)
    project = client.get_project(project_key)
    recipe = project.get_recipe('compute_test')
    try:
        recipe.run(wait=True, no_fail=False)
        return 'SUCCESS'
    except Exception as e:
        print(f"An error occurred while running the job: {e}")
        return 'FAILED'

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python tests.py <instance_url> <api-key> <project_key>")
        sys.exit(1)

    instance_url = sys.argv[1]
    api_key = sys.argv[2]
    project_key = sys.argv[3]
    test_status = run_tests(instance_url, api_key, project_key)
    if test_status == 'SUCCESS':
        print("Tests passed.")
        sys.exit(0)
    else:
        print("Tests failed.")
        sys.exit(1) 