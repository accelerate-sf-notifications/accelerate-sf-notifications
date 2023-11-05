import os
import json
import time
from flask.templating import _default_template_ctx_processor

import numpy as np
import streamlit as st
from mastodon import Mastodon, MastodonAPIError
from twilio.rest import Client

from asn.ai.detect_events import qa_from_video
from asn.ai.twitter_generator import generate_twitter_post
from asn.config import vars
from asn.const import BASE_PATH, DATA_PATH

account_sid = vars["twilio"]["account_sid"]
auth_token = vars["twilio"]["auth_token"]
tw_client = Client(account_sid, auth_token)

mastodon = Mastodon(
    client_id=vars["mastodon"]["client_id"],
    client_secret=vars["mastodon"]["client_secret"],
    access_token=vars["mastodon"]["access_token"],
    api_base_url=vars["mastodon"]["api_base_url"]
)


info = json.load(open(BASE_PATH / "asn" / "chaonan99/data/response.json"))
video_path = DATA_PATH / "demo_video_30min.mp4"
assert video_path.exists()
video_path = str(video_path)
video_path_template = BASE_PATH / "asn" / "chaonan99/data/" / "chapter_{}.mp4"
np.random.seed(42)


# if st.checkbox('Show content'):
#     st.markdown('<span style="color:red">This is some content.</span>', unsafe_allow_html=True)
# else:
#     st.write('This is some content')
# from IPython import embed; embed(using=False); os._exit(0)


# def video_comp():
#     return components.html(open("video_comp/index.html").read(), width=320, height=240,)


def initialize():
    tags = info["hashtags"]
    st.session_state['stage'] = 1
    st.session_state['concerned_tags'] = {t: False for t in tags}
    st.session_state['prev_time'] = -1
    st.session_state['current_section'] = 0
    st.session_state['messages'] = []
    st.session_state['video_path'] = ''
    st.session_state['phone_number'] = ''


def post_on_mastodon(text, video_filename):
    media = mastodon.media_post(
        video_filename,
        "video/mp4",
    )

    # Initialize variables for retry logic
    max_retries = 10  # Maximum number of retries
    retry_count = 0   # Current retry count
    wait_time = 10    # Time to wait between retries in seconds
    posted = False    # Flag to check if the post was successful

    # Retry loop
    while not posted and retry_count < max_retries:
        try:
            # Attempt to post the status
            mastodon.status_post(
                text, 
                media_ids=[media['id']]
            )
            posted = True
        except MastodonAPIError as e:
            # Print out the contents of the error to understand its structure
            print(e)
            print(vars(e))

            # Check if the error message contains 'processing'
            if 'processing' in str(e):
                # If media is still processing, wait and then try again
                print(f"Media not processed yet, waiting {wait_time} seconds. Retry {retry_count + 1}/{max_retries}.")
                time.sleep(wait_time)
                retry_count += 1
            else:
                # If there is a different error, raise it
                raise


def page_1():
    st.header("What are you interested in?")
    tags = info["hashtags"]
    for tag in tags:
        st.session_state.concerned_tags[tag] = st.checkbox(tag, value=True)
    
    phone_number = st.text_input("Your phone number")
    if phone_number:
        st.session_state['phone_number'] = phone_number

    if st.button("Subscribe"):
        st.session_state.stage = 2
        st.session_state.page_2_start_time = time.time()
        st.experimental_rerun()


def page_2():
    # st.title(info["title"])
    ## Get the current chapter

    chapters = info["chapters"]

    # r1c1, r1c2 = st.columns(2)
    st.header(f"[Live] {info['title']}")
    col1, col2 = st.columns(2)
    # current_time = int((time.time() - st.session_state.page_2_start_time) / 10)
    # print(current_time)
    # current_time = video_comp()
    # current_time = r1c1.number_input("Mock livestreaming time", min_value=1, max_value=600)
    # from IPython import embed; embed(using=False); os._exit(0)
    if st.session_state.current_section < len(chapters):
        c = chapters[st.session_state.current_section]
    else:
        st.session_state.stage = 3
        st.experimental_rerun()
    # for c in chapters:
    #     if c["start"] <= current_time and c["end"] > current_time:
    #         break

    ## All tags
    tags = info["hashtags"]
    interested_tags = {k for k, v in st.session_state.concerned_tags.items() if v}

    # Display video transcript in the left column
    # col1.header("Happening now")
    col1.subheader(c['chapter_title'])
    # curr_video_path = video_path_template.format(number=c['chapter_number'])
    # if not os.path.exists(curr_video_path):
    #     os.symlink(video_path, curr_video_path)
        # col2.video(curr_video_path)
    col2.video(video_path, start_time=c["start"])

    # col1.header("Summary")
    col1.write(c["chapter_summary"])
    tags_current_chapter = np.random.choice(tags, 3, replace=False)
    # Display video in the right column
    # col2.header("Video")
    # if st.session_state.prev_time != current_time:
    #     st.session_state.prev_time = current_time
    #     st.experimental_rerun()
    # else:
    # if r1c2.button("Set livestreming time"):
    #     col2.video(video_path, start_time=current_time)

    st.subheader("Hashtags")
    for tag in tags_current_chapter:
        if tag in interested_tags:
            st.markdown(f'<div style="color: red; font-size: 15px; border: 1px solid red; display: inline-block; padding: 5px; margin: 2px;">{tag}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div style="font-size: 15px; border: 1px solid black; display: inline-block; padding: 5px; margin: 2px;">{tag}</div>', unsafe_allow_html=True)
        
    if len(set(tags_current_chapter) & set(interested_tags)) == 0:
        st.subheader("No interested topic.")
    else:
        with st.spinner(text="In progress..."):
            ## TODO: oyzh: actually send notification
            background_info = c["chapter_summary"]
            post = generate_twitter_post(background_info)
            if len(st.session_state.phone_number) == 10:
                pn = f'+1{st.session_state.phone_number}'
                message = tw_client.messages.create(
                    from_=vars["twilio"]["message_from"],
                    body=post,
                    to=pn,
                )
            st.subheader(f"Notification sent.")
            # st.subheader(message.sid)
            st.write(post)
        # if "video_filename" in c:
        #     vp = c["video_filename"]
        #     post_on_mastodon(post, f"data/{vp}")

    # if st.button("Hearing finished"):
    #     st.session_state.stage = 3
    if st.button("next section"):
        print(c['start'])
        st.session_state.current_section += 1
        # st.experimental_rerun()


def page_3():
    # st.subheader("Watch the video recoding and ask your questions")
    st.subheader("Highlight")
    st.video("data/video1/gen_video_summary.mp4")
    ## TODO: chaonan99
    ## put a short video
    ## implement search
    for m in st.session_state.messages:
        with st.chat_message(m['role']):
            st.markdown(m['content'])

    msg = st.chat_input("Ask questions about the hearing")
    if msg:
        with st.chat_message('user'):
            st.markdown(msg)
            st.session_state.messages.append({'role': 'user', 'content': msg})
        with st.spinner(text='In progress...'):
            res = qa_from_video(msg)
        with st.chat_message('ai'):
            print(res)
            # from IPython import embed; embed(using=False); os._exit(0)
            st.markdown(res)
            st.session_state.messages.append({'role': 'ai', 'content': res})

def main():
    if 'stage' not in st.session_state:
        initialize()

    if st.session_state.stage == 1:
        page_1()
    elif st.session_state.stage == 2:
        page_2()
    elif st.session_state.stage == 3:
        page_3()



if __name__ == '__main__':
    main()