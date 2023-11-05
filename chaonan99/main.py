import json
from time import time

import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from streamlit_player import st_player


info = json.load(open("data/response.json"))
video_path = "data/sanfrancisco_bos_oct31_1.mp4"

# if st.checkbox('Show content'):
#     st.markdown('<span style="color:red">This is some content.</span>', unsafe_allow_html=True)
# else:
#     st.write('This is some content')
# from IPython import embed; embed(using=False); os._exit(0)


def video_comp():
    return components.html(open("video_comp/index.html").read(), width=320, height=240,)


def initialize():
    tags = info["hashtags"]
    st.session_state['concerned_tags'] = {t: False for t in tags}
    st.session_state['prev_time'] = -1


def page_1():
    st.header("What are you interested in?")
    tags = info["hashtags"]
    for tag in tags:
        st.session_state.concerned_tags[tag] = st.checkbox(tag, value=True)

    if st.button("Subscribe"):
        st.session_state.stage = 2
        st.session_state.page_2_start_time = time()
        st.experimental_rerun()


def page_2():
    # st.title(info["title"])
    ## Get the current chapter

    chapters = info["chapters"]

    # r1c1, r1c2 = st.columns(2)
    st.header(f"Live: {info['title']}")
    col1, col2 = st.columns(2)
    current_time = video_comp()
    # current_time = r1c1.number_input("Mock livestreaming time", min_value=1, max_value=600)
    print(current_time)
    # from IPython import embed; embed(using=False); os._exit(0)
    # for c in chapters:
    #     if c["start"] <= current_time and c["end"] > current_time:
    #         break

    # ## All tags
    # tags = info["hashtags"]
    # interested_tags = {k for k, v in st.session_state.concerned_tags.items() if v}

    # # Display video transcript in the left column
    # # col1.header("Happening now")
    # col1.subheader(c['chapter_title'])

    # # col1.header("Summary")
    # col1.caption(c["chapter_summary"])
    # tags_current_chapter = np.random.choice(tags, 3, replace=False)
    # # Display video in the right column
    # # col2.header("Video")
    # # if st.session_state.prev_time != current_time:
    # #     st.session_state.prev_time = current_time
    # #     st.experimental_rerun()
    # # else:
    # # if r1c2.button("Set livestreming time"):
    # #     col2.video(video_path, start_time=current_time)
    # col2.video(video_path, start_time=300)

    # st.subheader("Hashtags")
    # for tag in tags_current_chapter:
    #     if tag in interested_tags:
    #         st.markdown(f'<div style="color: red; font-size: 15px; border: 1px solid red; display: inline-block; padding: 5px; margin: 2px;">{tag}</div>', unsafe_allow_html=True)
    #     else:
    #         st.markdown(f'<div style="font-size: 15px; border: 1px solid black; display: inline-block; padding: 5px; margin: 2px;">{tag}</div>', unsafe_allow_html=True)
        
    # if len(set(tags_current_chapter) & set(interested_tags)) == 0:
    #     st.subheader("No interested topic.")
    # else:
    #     st.subheader("Have interested tags. Sending notification.")

    # if st.button("Hearing finished"):
    #     st.session_state.stage = 3
    #     st.experimental_rerun()


def page_3():
    st.write("Show some summarization video")


def main():
    if 'stage' not in st.session_state:
        initialize()
        st.session_state.stage = 1

    if st.session_state.stage == 1:
        page_1()
    elif st.session_state.stage == 2:
        page_2()
    elif st.session_state.stage == 3:
        page_3()



if __name__ == '__main__':
    main()