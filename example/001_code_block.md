# Code Execution in Dify: A Python Cookbook

Code Execution is an essential feature of Flow nodes in Dify. For more details, visit the [official documentation](https://docs.dify.ai/guides/workflow/node/code).

This cookbook primarily focuses on Python usage in Dify.

Download the DSL file: [Your Code](/DSL/Your%20Code~.yml)

## Recent Updates

In version 0.7.0, "Advanced Dependencies" allowed the use of either jinja2 or httpx. As of version 0.7.1, this step is no longer necessary \- you can use both libraries without additional setup.

- [ ] Update available dependencies for Code nodes

## Key Points for Code Nodes

1. Avoid using `print` statements
2. Always return a dictionary
3. Ensure input and output variables are valid

```python
def main() -> dict:
    # 个人偏好小卡片 -> personal preference for small cards
    pp_sCard = "Good~"
    # 一般专有名词维护表; 不要添加太多没必要的词
    words = "OpenAI, Anthropic"
    # 你的名字
    your_name = "AlterXYZ"
    # 头像 url
    avatar_url = "xxxxxxx.jpg"
    # 背景图片 url
    bg_url = "https:xxxxxxxxxx.jpg!/fh/350"
    # 渐变背景 Url
    gradient_bg_url = "https://xxxxxxxx.png"
    # 正文颜色
    text_color = "#000000"
    # 名字颜色
    name_color = "#000000"
    # 字体大小
    font_size = "150"
    return {
        "pp_sCard": pp_sCard, # 个人偏好小卡片
        "words": words, # 一般专有名词维护表
        "your_name": your_name, # 你的名字
        "avatar_url": avatar_url, # 头像 url
        "bg_url": bg_url, # 背景图片 url
        "gradient_bg_url": gradient_bg_url, # 渐变背景 Url
        "text_color": text_color, # 正文颜色
        "name_color": name_color, # 名字颜色
        "font_size": font_size, # 字体大小
    }
```

## Code Generator

I've created a simple Dify app to help you generate Python code for Code nodes. You can also use this prompt with your preferred model to create code.

Prompt: [Code Generator](/prompt/code_generator.md)

DSL file: [Your Code](/DSL/Your%20Code~.yml)

Just try is: [Dify APP](https://udify.app/workflow/FplkYtJgBj6bQrqP)

## Getting Started

Let's begin with a simple Code node that requires minimal programming.

### Assigning Words to Variables

#### Step 1: Create a Code Block

![image1](/images/1.png)

---

#### Step 2: Locate the IDE

You'll find the IDE window on the right side of your Dify Studio.

![image2](/images/2.png)

---

#### Step 3: Write Your Code

Here's a sample code created using the "Code Generator":

> <https://ezdify.alterxyz.org/demo/code_generator/>

![image3](/images/3.png)

---

#### Step 4: Set Your Output

Ensure your output matches your return statement. In Dify, the return must be a dictionary.

Set the output parameter as the key. This name will be used in other blocks.

Your Code Block should look like this:

![image4](/images/4.png)

---

#### Step 5: Refine Your Code

Let's rename "message" to "prompt0" for clarity:

1. Change the code:
    1. From: `return {"greeting": greeting, "message": message}`
    2. To: `return {"greeting": greeting, "prompt0": message}`
2. Modify your OUTPUT VARIABLES:
    1. Change "message" to "prompt0"
    2. to match your code.

![image5](/images/5.png)

Rename the entire block for easy identification:

![image6](/images/6.png)  
_We'll call it "my variables"._

#### Step 6: Test Run

Click the play button at the top right of your Code block editor.

![image7](/images/7.png)

If everything looks good, you'll see:  
![image8](/images/8.png)

### Applications

#### Enhance Conversation Variables

Version 0.7.0 introduced "[Conversation Variables](https://dify.ai/blog/enhancing-llm-memory-with-conversation-variables-and-variable-assigners)".

But for those who really tried, you may be experiencing some hard moments where you can only choose a variable, you can not write it manually.

Code blocks offer a solution for situations where manual variable writing is needed. You are welcome\!

![image9](/images/9.png)

#### Global Prompt

When using multiple LLM nodes, Code blocks can help manage prompts globally, especially useful in Workflows where Conversation Variables are not available there yet.

![image10](/images/10.png)

But what if you have 10 LLM nodes, you will not wanna manually edit them one by one.  
Also this is essentially important for Workflow, since Conversation Variables feature only available at Chatflow.

#### More Uses

We welcome your comments on additional uses to help other Dify users\!

### Considerations

This simple code assigning two variables takes an average of 0.08 seconds to execute. While negligible for simple tasks, it's worth noting. Thanks to Dify's [Sandbox](https://github.com/langgenius/dify-sandbox) for efficient execution\!
