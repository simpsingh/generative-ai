import boto3
import json
import pprint

client = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

titan_model_id = 'amazon.titan-text-express-v1'

titan_config = json.dumps({
    "inputText" : "Write a short poem on Guru Nanak Dev Ji",
    "textGenerationConfig": {
    "maxTokenCount": 4096,
    "stopSequences": [],
    "temperature": 0.1,
    "topP": 1
    }
    })


response = client.invoke_model(
    body=titan_config,
    modelId=titan_model_id,
    accept="application/json",
    contentType="application/json"
)

response_body = json.loads(response.get("body").read())

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(response_body.get("results"))  
          
