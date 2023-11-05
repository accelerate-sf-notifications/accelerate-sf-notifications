'''
Given the video and chapter_json, please genearate video segments and store the segments on to the device.

{
  "id": "d86b48d6-f505-4c4f-ba5b-4294116fbd51",
  "chapters": [
    {
      "chapter_number": 0,
      "start": 0,
      "end": 165,
      "chapter_title": "City Hall Advocates: Challenges and Safety Concerns",
      "chapter_summary": "This chapter focuses on the challenges faced by advocates at San Francisco City Hall. It covers a diverse range of issues, including safety concerns for all individuals, harassment by right-wing individuals, and the need for better government. Personal stories of resilience and determination are shared, highlighting the importance of public advocacy."
    },
    {
      "chapter_number": 1,
      "start": 165,
      "end": 375,
      "chapter_title": "Advocacy for Change: Political Topics and LGBTQ+ Rights",
      "chapter_summary": "In this chapter, the video delves into political topics such as charter reform and transitioning to a council manager system. It also highlights the importance of electing better leaders and advocates for the protection of transgender, lesbian, gay, bisexual, and queer individuals. The challenges faced by LGBTQ+ activists and the need for educating people and protecting trans rights are discussed."
    },
    ...
}

working_dir = '/Users/ouyangzhihao/Desktop/sf_hackathon/accelerate-sf-notifications/data/video1/short_videos'
def gen_video_segments(input_video_path: str) -> list:
    segment_paths = []
    return segment_paths

'''

import json
import os
from concurrent.futures import ThreadPoolExecutor

import ffmpeg

file_path = "/Users/ouyangzhihao/Desktop/sf_hackathon/accelerate-sf-notifications/data/video1/chapter.json"
with open(file_path, 'r') as json_file:
    data = json.load(json_file)
chapter_json = data


working_dir = '/Users/ouyangzhihao/Desktop/sf_hackathon/accelerate-sf-notifications/data/video1/short_videos'


# Your chapter JSON and working_dir would be defined here as before

def process_segment(chapter, input_video_path, working_dir):
    chapter_number = chapter['chapter_number']
    start_time = chapter['start']
    end_time = chapter['end']
    segment_file_name = f"chapter_{chapter_number}.mp4"
    segment_path = os.path.join(working_dir, segment_file_name)

    try:
        (
            ffmpeg
            .input(input_video_path, ss=start_time, to=end_time)
            .output(segment_path, c='copy')
            .run(capture_stdout=True, capture_stderr=True)
        )
    except ffmpeg.Error as e:
        # This will print the error to your console
        print(e.stderr.decode())
        raise e

    return segment_path

def gen_video_segments(input_video_path: str) -> list:
    # Ensure the working directory exists
    if not os.path.exists(working_dir):
        os.makedirs(working_dir)
    
    # Load chapters from the JSON data
    chapters = chapter_json.get('chapters', [])
    
    with ThreadPoolExecutor() as executor:
        segment_paths = list(executor.map(process_segment, chapters, [input_video_path]*len(chapters), [working_dir]*len(chapters)))
    
    return segment_paths

# Example usage
# input_video = '/Users/ouyangzhihao/Desktop/Screen Recording 2023-02-28 at 11.00.34.mov'
input_video = '/Users/ouyangzhihao/Downloads/San Francisco Board Meeting.mp4'
generated_segments = gen_video_segments(input_video)

# Optionally print the paths of the generated segments
for segment_path in generated_segments:
    print(segment_path)
