# Dify Agent inside Chatflow or Workflow

This demo is intended for a one-time invocation of Agent. You should reference the returned `response_text`

Use a code block, and set all necessary parameters.

The code I use for the code block is here:

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

## Detailed breakdown

### Get your Dify Agent API key

> Due to some security standards, it may also be named as `agent_id`

The api_key refers to your Backend Service API Secret Key

![image](https://github.com/user-attachments/assets/65ac5f2a-2337-4e8c-8aac-26b6cd6eb1c7)

### Security store your key

![image](https://github.com/user-attachments/assets/0126e9e9-632f-4874-9701-3ae18bd871c4)

Storing your key in Environment Variables is a good option, this only works for the specific app, not your whole Dify Studio.

Please also note that storing as a `Secret` means you will not be able to retrieve it later.

### Variables

The Agent allows you to make variables and use them somewhere; this example also supports this.

The initial one allows you to make one variable; you can increase or delete it as needed.

Example for no variables:

```python
def main(api_key: str, query: str, user: str) -> dict:
    import httpx
    import json

    url = "https://api.dify.ai/v1/chat-messages"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "text/event-stream"
    }
    data = {
        "inputs": {},

# The rest are the same
```

For 3 variables with fixed variable names:

```python
def main(api_key: str, query: str, var_abc: str, var_xyz: str, user: str, something: str) -> dict:
    import httpx
    import json

    url = "https://api.dify.ai/v1/chat-messages"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "text/event-stream"
    }
    data = {
        "inputs": {"abc": var_abc, "xyz": var_xyz, "something_else": something},
# The rest are same
```

Please let me know if you have any additional questions.

By GitHub Issue: <https://github.com/alterxyz/easy-dify-cookbook/issues/new>

Using this prompt and this page's details with any LLM or coding expert would be a good option for questions or customization.

<https://github.com/alterxyz/easy-dify-cookbook/blob/main/prompt/code_generator.md>


### Advance

However, you can continue chat with Agent, by implement some if-else node and conversation variable feature.

Here is my code that may help:

```python
import httpx
import json

def first_message_to_dify(api_key: str, query: str, user: str, inputs: dict) -> dict:

    url = "https://api.dify.ai/v1/chat-messages"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "text/event-stream",
    }
    data = {
        "inputs": inputs,
        "query": query,
        "response_mode": "streaming",
        "conversation_id": "",
        "user": user,
        "files": [],
    }

    full_response = ""
    conversation_id = ""
    metadata = ""

    with httpx.Client() as client:
        with client.stream("POST", url, json=data, headers=headers) as response:
            for line in response.iter_lines():
                if line.startswith("data: "):
                    try:
                        event_data = json.loads(line[6:])
                        # print(event_data)
                        if (
                            event_data["event"] == "agent_message"
                            or event_data["event"] == "message"
                        ):
                            full_response += event_data.get("answer", "")
                        elif event_data["event"] == "message_end":
                            conversation_id = event_data.get(
                                "conversation_id", "")
                            metadata = event_data
                    except json.JSONDecodeError:
                        pass
                    except KeyError:
                        pass

    return {
        "status_code": response.status_code,
        "response_text": full_response,
        "conversation_id": conversation_id,
        "metadata": metadata,
    }



    full_response = ""
    metadata = ""

    with httpx.Client() as client:
        with client.stream("POST", url, json=data, headers=headers) as response:
            for line in response.iter_lines():
                if line.startswith("data: "):
                    try:
                        event_data = json.loads(line[6:])
                        # print(event_data)
                        if (
                            event_data["event"] == "agent_message"
                            or event_data["event"] == "message"
                        ):
                            full_response += event_data.get("answer", "")
                        elif event_data["event"] == "message_end":
                            metadata = event_data
                    except json.JSONDecodeError:
                        pass
                    except KeyError:
                        pass

    return {
        "status_code": response.status_code,
        "response_text": full_response,
        "conversation_id": conversation_id,
        "metadata": metadata,
    }
```

---

Alter link: <https://ezdify.alterxyz.org/cookbook/#dify-agent-inside-chatflow-or-workflow>

Difyshare: <https://difyshare.com/flow/66f328dd00181db9338e>
