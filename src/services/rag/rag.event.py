from services.rag.rag_model_anthropic_claude_v2 import handler
import json

event = {
    "body": json.dumps({"question": "What does GDPR stand for?"})
}

response = handler(event, {})

print(response)