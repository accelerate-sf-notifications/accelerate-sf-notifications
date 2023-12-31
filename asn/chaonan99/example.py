import requests

# Variables
BASE_URL = "https://api.twelvelabs.io/v1.2"
api_key = "tlk_0HQGKRC3F8AKG02810PHV2ZBP09S"
data = {
    "video_id": "6545f931195730422cc38329",
    "type": "chapter"
}

# Send request
response = requests.post(f"{BASE_URL}/summarize", json=data, headers={"x-api-key": api_key})


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
    {
      "chapter_number": 2,
      "start": 375,
      "end": 555,
      "chapter_title": "Challenges and Personal Stories of Advocacy",
      "chapter_summary": "This chapter focuses on the challenges faced by advocates at San Francisco City Hall, including online attacks and misogyny. Personal stories of resilience and determination are shared, emphasizing the need for public advocacy and supporting the LGBTQ+ community. The video also highlights the importance of recognizing the needs of transgender individuals and addressing mental health issues."
    },
    {
      "chapter_number": 3,
      "start": 555,
      "end": 795,
      "chapter_title": "Addressing City Hall Influences and Advocacy Efforts",
      "chapter_summary": "The final chapter discusses the influence of Wyoming and other states on decision-making in San Francisco. The need for public action and advocating for changes in law enforcement strategy to address crime rates are emphasized. It also covers concerns about CDC quarantine stations, homelessness, corruption, and the importance of public safety and the role of advocacy efforts in shaping policies."
    },
    {
      "chapter_number": 4,
      "start": 795,
      "end": 823,
      "chapter_title": "Civic Proceedings and In Memoriam",
      "chapter_summary": "This chapter showcases the adoption of resolutions at city council meetings and the adjournment in memory of a beloved individual. It provides a glimpse into the civic proceedings and the important role of the San Francisco City Council in addressing city-wide issues."
    }
  ]
}

import requests

# Variables
BASE_URL = "https://api.twelvelabs.io/v1.2"
api_key = "tlk_0HQGKRC3F8AKG02810PHV2ZBP09S"
data = {
    "video_id": "6545f931195730422cc38329",
    "types": [
        "title",
        "hashtag",
        "topic"
    ]
}

# Send request
response = requests.post(f"{BASE_URL}/gist", json=data, headers={"x-api-key": api_key})


{
  "id": "94f894ab-7d1b-480f-9404-9ec9be1335a3",
  "title": "Championing Change: Advocating for Safety, Democracy, and LGBTQ+ Rights at San Francisco City Hall",
  "topics": [
    "City Hall Advocacy"
  ],
  "hashtags": [
    "safety concerns",
    "harassment",
    "trans femme",
    "right-wingers",
    "law enforcement",
    "police officers",
    "death threats",
    "political arena",
    "charter reform",
    "council manager system",
    "elected auditor controller",
    "good government",
    "homelessness",
    "behavioral health",
    "clean streets",
    "crime rates",
    "law enforcement staffing",
    "CDC quarantine stations",
    "public health",
    "public safety",
    "COVID-19",
    "public comment",
    "formal attire",
    "San Francisco City Hall",
    "City Hall Advocacy",
    "City Hall Challenges"
  ]
}


import requests

# Variables
BASE_URL = "https://api.twelvelabs.io/v1.2"
api_key = "tlk_0HQGKRC3F8AKG02810PHV2ZBP09S"
data = {
    "video_id": "6545f931195730422cc38329",
    "type": "highlight"
}

# Send request
response = requests.post(f"{BASE_URL}/summarize", json=data, headers={"x-api-key": api_key})


{
  "id": "99f69c94-0446-4155-9af1-6f5ea9accf98",
  "highlights": [
    {
      "start": 0,
      "end": 105,
      "highlight": "A woman in a wheelchair passionately speaks at a public meeting, addressing safety concerns for all individuals, not just the wealthy. She bravely discusses her own experiences with harassment from right-wing individuals in San Francisco, highlighting the need for change.",
      "highlight_summary": "The video captures a woman in a wheelchair addressing safety concerns for all individuals and sharing her experiences with harassment from right-wing individuals in San Francisco, advocating for change."
    },
    {
      "start": 120,
      "end": 135,
      "highlight": "The woman shares her personal experience of coming out as transgender in December 2021 and quickly educating herself on what it means to be trans. She emphasizes the importance of being informed and actively supporting the LGBTQ+ community.",
      "highlight_summary": "A woman shares her personal journey of coming out as transgender and emphasizes the need for education and support within the LGBTQ+ community."
    },
    {
      "start": 525,
      "end": 555,
      "highlight": "Woman recounts horrifying experiences at Sutter House Hospital, calls for change and public advocacy in powerful speech",
      "highlight_summary": "A woman courageously shares her traumatic experiences at Sutter House Hospital and advocates for change and public advocacy."
    }
  ]
}


import requests

# Variables
BASE_URL = "https://api.twelvelabs.io/v1.2"
api_key = "tlk_0HQGKRC3F8AKG02810PHV2ZBP09S"
data = {
    "video_id": "6545f931195730422cc38329",
    "type": "summary"
}

# Send request
response = requests.post(f"{BASE_URL}/summarize", json=data, headers={"x-api-key": api_key})


{
  "id": "966e1259-b6b1-4da9-92db-5e1a24813243",
  "summary": "An impassioned video captures the challenges faced by advocates at San Francisco City Hall. The video features a diverse group of individuals, including a woman in a wheelchair, discussing various issues and advocating for change. They address safety concerns, harassment from right-wing individuals, and the need for better government. The video also highlights topics such as charter reform, transitioning to a council manager system, and the importance of electing better leaders. Personal stories of resilience and determination are shared, emphasizing the need for public advocacy. The video ends with a city council meeting where resolutions are considered, and the meeting is adjourned in memory of a beloved individual. Throughout the video, the audience witnesses the passion and dedication of these advocates as they strive for a better future for their community."
}