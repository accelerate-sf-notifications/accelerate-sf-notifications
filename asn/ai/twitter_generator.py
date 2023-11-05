from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


def generate_twitter_post(background_info: str) -> str:
    prompt_str = '''ChatGPT, assume you are a governer at San Francisco, please generate a 280 character or less Twitter post. 
The background: {background}

Write twitter for this topic:
22:58 Colleagues I'm today submitting
23:00 a drafting request to the city
23:03 attorney and controller that
23:05 will continue in needed
23:06 conversation about the crisis of
23:09 police under staffing in san
23:09 francisco.
23:11 The rules yesterday considered
23:14 my charter amendment to address
23:16 police staffing with a measured
23:18 evidence based 5 year plan.
23:21 The substantive core was amend
23:24 over my oksz I will not litigate
23:25 that here we will have
23:26 opportunity as a board of
23:28 supervisors to debate the merits
23:32 now a reimagined version as
23:33 amended.
'''
    prompt = ChatPromptTemplate.from_template(prompt_str)
    model = ChatOpenAI(model='gpt-3.5-turbo-16k')
    chain = prompt | model
    res = chain.invoke({"background": background_info})
    return res.content

if __name__ == "__main__":
    # Example usage
    # Generate a Twitter post with background information
    from asn.const import video_transcript_text
    background_info = video_transcript_text
    post = generate_twitter_post(background_info)
    print(post)
