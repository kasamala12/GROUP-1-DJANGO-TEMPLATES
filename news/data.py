"""
In-memory data store for the University News Portal.

Per the assignment, a database is optional — news data is kept in a
simple Python list of dictionaries. Each dictionary represents one
news article and is passed from the views to the templates as context.
"""

NEWS_ITEMS = [
    {
        'id': 1,
        'title': 'University Launches a Tree Planting Campaign',
        'summary': 'Ardhi University (ARU), together with TFS, TACSS, iBIG, and ARU Alumni, launched a tree-planting campaign to support environmental conservation and climate action. The initiative aims to plant 400 trees to reduce global warming and promote environmental sustainability..',
        'content': (
            'Ardhi University (ARU) in collaboration with Tanzania Forest Services Agency (TFS), Tanzania Alliance for Climate and Sustainable Society (TACSS), I believe in Green (iBIG) and ARU Alumni launched a tree planting campaign.'
'Speaking at the event, the Vice Chancellor of ARU Prof. Evaristo Liwa said that the tree planting campaign is part of supporting the President of the United Republic of Tanzania H.E. Dr. Samia Suluhu Hassan on her commitment to environmental conservation.'
'He said the ARU community will plant about four hundred trees (400) donated by their partners TFS, TACSS, and iBIG who are strong players in environmental conservation in the Country. “The exercise will help to combat global warming by absorbing carbon dioxide, removing and storing the carbon while releasing oxygen back into the air”, said Prof. Liwa.'
'Prof. Liwa said that, since ARU is the champion in teaching and training in areas of environmental sciences and management as well as land management and Valuation, the university will continue to spearhead issues of environmental protection including participating in various measures to ensure that Tanzania produces competent professionals in areas related to environmental protection and management.'
'Ardhi University, through the School of Architecture Construction Economics and Management (SACEM), as well as the School of Engineering and Environmental Studies, offers competitive Bachelor degrees, Postgraduate programmes as well as PhD programmes'
            
        ),
        'author': 'Eunice Likotiko',
        'date': '2026-06-20',
        'category': 'Technology',
    },
    {
        'id': 2,
        'title': 'Training On Gender and  Community based Monitoring (CBM) For Students Of Ardhi University',
        'summary': 'Ardhi University conducted a two-day training to equip students with community-based monitoring and evaluation skills. The program prepared students to promote gender inclusion, community participation, and sustainable development.'
                    ,
        'content': (
            'Sub-project 6 at Ardhi University, sponsored by the VLIR-UOS Project, organized a two-day training (13–14 August 2024) on gender and community participation. The training equipped students with community-based monitoring, evaluation, and project management skills to strengthen their role in supporting sustainable community development.'
        ),
        'author': 'Ardhi university',
        'date': '2026-04-24',
        'category': 'Campus Life',
    },
    {
        'id': 3,
        'title': 'New Library Wing Opens to Students',
        'summary': 'A modern extension to the main library adds 500 '
                    'new study spaces and a digital media lab.',
        'content': (
            'Students now have access to a newly constructed wing of '
            'the university library, featuring quiet study pods, group '
            'collaboration rooms, and a fully equipped digital media '
            'lab for video and podcast production. The wing was funded '
            'through a combination of alumni donations and a government '
            'education grant.'
        ),
        'author': 'David Kigoni',
        'date': '2026-06-15',
        'category': 'Campus Life',
    },
    {
        'id': 4,
        'title': 'Geographic Information System (GIS) Education Summit and GIS Day at Ardhi University',
        'summary': 'ARU and ESRI East Africa held a GIS Day summit to promote modern GIS technology and climate resilience. The program equipped students with geospatial skills for sustainable development ',
        'content': (
           'Ardhi University, in collaboration with ESRI East Africa, organized a GIS Day Educational Summit to train students on modern GIS technologies, climate change, and sustainable problem-solving. The event brought together experts, lecturers, and students to enhance geospatial knowledge and practical skills.'
        ),
        'author': 'Maria Francis',
        'date': '2026-06-02',
        'category': 'Academics',
    },
    {
        'id': 5,
        'title': 'University Football Team Advances to Regional Finals',
        'summary': 'A dramatic penalty shootout sends the team through '
                    'to the next round.',
        'content': (
            'The university football team secured a spot in the '
            'regional finals after a tense penalty shootout against '
            'their closest rivals. Coach Michael Tanko praised the '
            'squad\'s resilience, noting that the team trained through '
            'the holidays to prepare for the tournament.'
        ),
        'author': 'Bariki kasamala',
        'date': '2026-07-14',
        'category': 'Sports',
    },
]


def get_all_news():
    """Return the full list of news dictionaries, most recent first."""
    return sorted(NEWS_ITEMS, key=lambda item: item['date'], reverse=True)


def get_latest_news(count=3):
    """Return the most recent `count` news items for the home page."""
    return get_all_news()[:count]


def get_news_by_id(news_id):
    """Return a single news dictionary matching news_id, or None."""
    for item in NEWS_ITEMS:
        if item['id'] == news_id:
            return item
    return None
