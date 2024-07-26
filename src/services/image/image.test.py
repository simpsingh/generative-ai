from image import handler
import json

event = {
    "body": json.dumps({"description": "A calm individual with a detached soul meditating onto God"})
}

response = handler(event, {})

print(response)