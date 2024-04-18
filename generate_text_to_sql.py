import boto3
import json

bedrock = boto3.client(
    service_name='bedrock-runtime', 
    region_name='us-west-2'
)

input = {
  "modelId": "meta.llama2-13b-chat-v1", // Anthropic Claude v2 FM was used in actual PoC.
  "contentType": "application/json",
  "accept": "*/*",
  "body": "{\"prompt\":\"Write a JOIN SQL query to join two tables namely customer and mortgage, displaying mortgage left to pay in ascending order of the mortgage amount left to pay to the bank.\",\"max_gen_len\":512,\"temperature\":0.5,\"top_p\":0.9}"
}

# Invoke the model and get back the response
response = bedrock.invoke_model(body=input["body"],
                                modelId=input["modelId"],
                                accept=input["accept"],
                                contentType=input["contentType"])

response_body = json.loads(response['body'].read())

# Print the response from the model
print(response_body)
