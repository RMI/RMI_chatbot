#%%

import requests

url = 'https://app-backend-ruxl77zfofg3e.azurewebsites.net/chat'
data = {
    'messages': [
        {'content': 'Explain methane emissions from rice cultivation.', 'role': 'user'}
    ],
    'stream': True,
    'context': {
        'overrides': {
            'top': 3,
            'temperature': 0.3,
            'minimum_reranker_score': 0,
            'minimum_search_score': 0,
            'retrieval_mode': 'hybrid',
            'semantic_ranker': True,
            'semantic_captions': False,
            'suggest_followup_questions': False,
            'use_oid_security_filter': False,
            'use_groups_security_filter': False,
            'vector_fields': [],
            'use_gpt4v': False,
            'gpt4v_input': 'textAndImages'
        }
    },
    'session_state': None
}

response = requests.post(url, json=data)
print(response.text)

#%%