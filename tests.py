import os
import time
import requests
import sys

# Environment variables
DATAIKU_API_TOKEN = os.getenv('DATAIKU_API_TOKEN')

# Headers for API requests
headers = {
    'Authorization': f'Bearer {DATAIKU_API_TOKEN}',
    'Content-Type': 'application/json'
}

def run_tests(instance_url, project_key):
    # Run a dummy recipe
    recipe_url = f'{instance_url}/public/api/projects/{project_key}/recipes/run'
    recipe_data = {
        'recipeId': 'dummy_recipe_id',  # Replace with the actual recipe ID
        'projectKey': project_key
    }
    recipe_response = requests.post(recipe_url, json=recipe_data, headers=headers)
    recipe_response.raise_for_status()
    recipe_run_id = recipe_response.json()['id']

    # Wait for the recipe to complete
    while True:
        recipe_status_url = f'{instance_url}/public/api/projects/{project_key}/recipes/{recipe_run_id}'
        recipe_status_response = requests.get(recipe_status_url, headers=headers)
        recipe_status_response.raise_for_status()
        recipe_status = recipe_status_response.json()['status']

        if recipe_status in ['success', 'failed']:
            return recipe_status

        time.sleep(10)  # Wait for 10 seconds before checking again

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python tests.py <instance_url> <project_key>")
        sys.exit(1)

    instance_url = sys.argv[1]
    project_key = sys.argv[2]
    test_status = run_tests(instance_url, project_key)
    if test_status == 'success':
        print("Tests passed.")
        sys.exit(0)
    else:
        print("Tests failed.")
        sys.exit(1) 