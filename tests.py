import os
import time
import sys
from dataiku import Client

# Environment variables
DATAIKU_API_TOKEN = os.getenv('DATAIKU_API_TOKEN')

def run_tests(instance_url, project_key):
    client = Client(instance_url, DATAIKU_API_TOKEN)
    project = client.get_project(project_key)
    recipe = project.get_recipe('compute_fake_csv_copy')
    run = recipe.run_and_wait()

    # Wait for the recipe to complete
    while run.status not in ['SUCCESS', 'FAILED']:
        time.sleep(10)  # Wait for 10 seconds before checking again
        run.refresh()

    return run.status

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python tests.py <instance_url> <project_key>")
        sys.exit(1)

    instance_url = sys.argv[1]
    project_key = sys.argv[2]
    test_status = run_tests(instance_url, project_key)
    if test_status == 'SUCCESS':
        print("Tests passed.")
        sys.exit(0)
    else:
        print("Tests failed.")
        sys.exit(1) 