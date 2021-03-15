from vantage6.tools.mock_client import ClientMockProtocol
from vantage6.tools.container_client import ClientContainerProtocol


## Mock client
client = ClientMockProtocol(["local/data.csv", "local/data.csv"], "v6-boilerplate-py")
# client = ClientContainerProtocol(
#     "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODc0NzY4OTAsIm5iZiI6MTU4NzQ3Njg5MCwianRpIjoiNzNmNWI1MjEtZWQwMi00YzFkLTg4ZDUtOGM4N2EzYjEwMWJhIiwiaWRlbnRpdHkiOnsidHlwZSI6ImNvbnRhaW5lciIsIm5vZGVfaWQiOjQsImNvbGxhYm9yYXRpb25faWQiOjEsInRhc2tfaWQiOjE2MDEsImltYWdlIjoiaGVsbG8td29ybGQifSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIiwidXNlcl9jbGFpbXMiOnsidHlwZSI6ImNvbnRhaW5lciIsInJvbGVzIjpbXX19.SxjyOjo-6rhz5-v17PvbSvC8WrsafEFIvhw2uPjrkbM",
#     host="https://trolltunga.vantage6.ai",
#     port=443,
#     path=""
# )

organizations = client.get_organizations_in_my_collaboration()
print(organizations)
ids = [organization["id"] for organization in organizations]

task = client.create_new_task({"method":"some_example_method"}, ids)
print(task)

results = client.get_results(task.get("id"))
print(results)

master_task = client.create_new_task({"master": 1, "method":"master"}, [ids[0]])
results = client.get_results(task.get("id"))
print(results)