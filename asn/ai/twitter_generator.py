from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI


def generate_twitter_post(background_info: str) -> str:
    prompt_str = '''ChatGPT, assume you are a governer at San Francisco, please generate a 280 character or less Twitter post. 
The background: {background}
'''
    prompt = ChatPromptTemplate.from_template(prompt_str)
    model = ChatOpenAI()
    chain = prompt | model
    res = chain.invoke({"background": background_info})
    return res.content

if __name__ == "__main__":
    # Example usage
    # Generate a Twitter post with background information
    background_info = "Monthly gathering for Peninsula for Everyone. Meet and organize with neighbors who are working to build a more inclusive and sustainable region."
    post = generate_twitter_post(background_info)
    print(post)
