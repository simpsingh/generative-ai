import boto3
import json

prompt_data = """
Write SQL code to join two tables with the following DDL
```sql
CREATE TABLE USER
<insert DDL here>

CREATE TABLE MORTGAGE
<insert DDL here>
"""

// Provide .csv extracts for above tables //

bedrock = boto3.client(service_name="bedrock-runtime")
payload = {
    "prompt": f"\n\nHuman:{prompt_data}\n\nAssistant:",
    "max_tokens_to_sample": 512,
    "temperature": 0.8,
    "top_p": 0.8,
}

body = json.dumps(payload)
model_id = "anthropic.claude-v2" // calling foundation model claude-v2 from anthropic //
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json",
)

response_body = json.loads(response.get("body").read())
response_text = response_body.get("completion")
print(response_text)
