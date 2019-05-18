from kubernetes import client, config

#see https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-api/#accessing-the-cluster-api to know how to get the token
#The command look like kubectl get secrets | grep default | cut -f1 -d ' ') | grep -E '^token' | cut -f2 -d':' | tr -d '\t' but better check the official doc link
aToken="eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZWZhdWx0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImFwaS1zZXJ2aWNlLWFjY291bnQtdG9rZW4tYzdmemciLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiYXBpLXNlcnZpY2UtYWNjb3VudCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6IjAxZTIwNmUwLTc1MzktMTFlOS04MmU1LTQyMDEwYTgwMDE5NyIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmFwaS1zZXJ2aWNlLWFjY291bnQifQ.bfWurP_wJ3E7gC7qb8zO4RXTcL6bYXGv__kJVjjgiqy_9a5xUmxAPaoVNyZ_N3cIKIUt6SgNkCE-8POyFLRThtS9QYHyHTMC9f7HhPTXCC7v19B1wQsik-1hX-XSb8IOvVHYx3ePxWjpoEHSn_RIHzTOoOH4JXB9GAZAO_V-KfKk6x8LuXKIxwE7WRM_O8-PI8LO9tcMG0RTkiJFLmHquOD4_Liiu_Asp0-V3oNKPpseIj-kj9Evj0cIFJFpTJnghdjFbrAMHy0o3P8TyX8Zz_zm6ET8B9jiAJdU3_P-9WkfNYrBpiQy7onuJsVHlqVlSv2O568QjTndWtBWdAaDTw"


# Configs can be set in Configuration class directly or using helper utility
configuration = client.Configuration()
configuration.host="https://35.202.190.47"
configuration.verify_ssl=False
# configuration.debug = True

configuration.api_key={"authorization":"Bearer "+ aToken}
client.Configuration.set_default(configuration)

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
print(v1.list_namespaced_pod('tools'))
