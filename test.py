from vantage6.tools.mock_client import ClientMockProtocol

client = ClientMockProtocol(["local/data.csv", "local/data.csv"], "v6-boilerplate-py")

# Get all organizations in the collaboration
organizations = client.get_organizations_in_my_collaboration()
print(organizations)
ids = [organization["id"] for organization in organizations]

# Manually run the method at all the organization
task = client.create_new_task({"method":"some_example_method"}, ids)
print(task)

# Get the results
results = client.get_results(task.get("id"))
print(results)

# Let one organization take care of running the method at all organizations (and combining the results)
master_task = client.create_new_task({"master": 1, "method":"master"}, [ids[0]])
results = client.get_results(master_task.get("id"))
print(results)
