from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from asn.const import video_transcript_text


# TODO make it easier to use
def search_event_from_video(search_item: str, transcript_text: str=video_transcript_text):
    prompt_str = '''Please help me to find the [Search item] from the [Background], find <= 5 items.

Search item:
{search_item}
Background: 
{background}

Please response in json format like:
[
    {{
        "content": "district 2020-1 and determine",
        "time:": 00:09:58",
        "message": "I think they are discussing district."
    }},
    {{
        ...
    }}
    ...
]
'''
    prompt = ChatPromptTemplate.from_template(prompt_str)
    # model = ChatOpenAI(model='gpt-3.5-turbo-16k')
    model = ChatOpenAI(model='gpt-4', temperature=0.1)
    chain = prompt | model
    res = chain.invoke({
        "background": transcript_text,
        "search_item": search_item
    })
    # import ipdb; ipdb.set_trace()
    print("search_item:", search_item)
    return res.content


def qa_from_video(search_item: str, transcript_text: str=video_transcript_text):
    prompt_str = '''Please help me to answer the [Question], you'll find the answer from [Background].

[Question]:
{search_item}
[Background]: 
{background}

Response:
'''
    prompt = ChatPromptTemplate.from_template(prompt_str)
    model = ChatOpenAI(temperature=0.1, model='gpt-3.5-turbo-16k')
    # model = ChatOpenAI(model='gpt-4')
    chain = prompt | model
    res = chain.invoke({
        "background": transcript_text,
        "search_item": search_item
    })
    # print(res)
    # import ipdb; ipdb.set_trace()
    # print("search_item:", search_item)
    return res.content
    

def gen_tags_from_video(transcript_text: str=video_transcript_text) -> str:
    prompt_str = '''Please help me generate <=10 tags that is the highlight of the video which will be used to search content in the video. Respond in an array.
Thhe tags are:
- Meaningful
- Easy to understand
- 

[Video transcript]: 
{background}

Response:
[?, ?...]
'''
    prompt = ChatPromptTemplate.from_template(prompt_str)
    model = ChatOpenAI(temperature=0.1, model='gpt-3.5-turbo-16k')
    # model = ChatOpenAI(model='gpt-4')
    chain = prompt | model
    res = chain.invoke({
        "background": transcript_text,
    })
    return res.content

if __name__ == "__main__":
    # Example usage
    # Generate a Twitter post with background information
    # item_search1 = "voting for revolving funds"
    # item_search1 = "Pledge of Allegiance"
    # item_search1 = "homelessness"
    item_search1 = "Policy staffing"
    post1 = search_event_from_video(item_search1)
    print(post1)
    '''
    [
        {
            "content": "item 10 an ordinance to amend the administrative code remove the authorization for cash revolving funds and reduce the max amount of the cash revolve ing fund for the port.",
            "time": "00:06:36",
            "message": "They are discussing an ordinance to amend the administrative code to remove the authorization for cash revolving funds and reduce the maximum amount of the cash revolving fund for the port."
        }
    ]


    '''

    # item_search2 = "What are they discussing"
    # post2 = qa_from_video(item_search2)
    # print(post2)

    # item_search2 = "Anything related to homeless issue?"
    # post2 = qa_from_video(item_search2)
    # print(post2)

    # item_search2 = "What's the vote of ronen for ?"
    # post2 = qa_from_video(item_search2)
    # print(post2)

    # has tag test
    # tags = gen_tags_from_video()
    # print(tags)

    
