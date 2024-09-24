# Dify Agent inside Chatflow or Workflow

Use a code block, and set all necessary parameter.

Use the input and output variables notes for your setting.

The code I use for code block is here:

```python
"""
Input Variables:
api_key: String, query: String, var_name: String, var_input: String, user: String
Output Variables:
status_code: Number, response_text: String, conversation_id: String, usage: Object
"""

def main(api_key: str, query: str, var_name: str, var_input: str, user: str) -> dict:
    import httpx
    import json

    url = "https://api.dify.ai/v1/chat-messages"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "text/event-stream"
    }
    data = {
        "inputs": {var_name: var_input},
        "query": query,
        "response_mode": "streaming",
        "conversation_id": "",
        "user": f"workflow-{user}",
        "files": []
    }

    full_response = ""
    conversation_id = ""
    usage = {}

    with httpx.Client() as client:
        with client.stream("POST", url, json=data, headers=headers) as response:
            for line in response.iter_lines():
                if line.startswith("data: "):
                    try:
                        event_data = json.loads(line[6:])
                        # print(event_data)
                        if event_data['event'] == 'agent_message':
                            full_response += event_data.get('answer', '')
                        elif event_data['event'] == 'message_end':
                            conversation_id = event_data.get('conversation_id', '')
                            usage = event_data.get('metadata', {}).get('usage', {})
                    except json.JSONDecodeError:
                        pass
                    except KeyError:
                        pass

    return {
        "status_code": response.status_code,
        "response_text": full_response,
    }
```

The result would be like:

![image](https://github.com/user-attachments/assets/2c80f051-4fe3-4ea8-a2a6-b3ad7be86088)

View more about code block here:

<https://ezdify.alterxyz.org/cookbook/#code-block>

<https://github.com/alterxyz/easy-dify-cookbook/blob/main/prompt/code_generator.md>

---

Alter link: <https://ezdify.alterxyz.org/cookbook/#dify-agent-inside-chatflow-or-workflow>
