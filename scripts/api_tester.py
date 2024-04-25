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

x = response.text

#%%



url = 'http://127.0.0.1:50506/chat'
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

y = response.text
import json
data_dict = json.loads(y)

#%%

import aiohttp
import asyncio
import json

async def fetch_stream(url, data):
    results = []
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            # Ensure the response is valid
            response.raise_for_status()

            # Process each line of the response as it arrives
            async for line in response.content:
                if line.strip():  # Ignore empty lines
                    data = json.loads(line.decode('utf-8'))
                    print(data)  # Handle each JSON object as needed
                    results.append(data)
    return results

async def main():
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

    response = await fetch_stream(url, data)
    return response

response = await main()

# %%

import aiohttp
import asyncio
import json

async def fetch_stream(url, data):
    results = []
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            # Ensure the response is valid
            response.raise_for_status()

            # Process each line of the response as it arrives
            async for line in response.content:
                if line.strip():  # Ignore empty lines
                    data = json.loads(line.decode('utf-8'))
                    print(data)  # Handle each JSON object as needed
                    results.append(data)
    return results

async def main():
    url = 'http://127.0.0.1:50506/chat'
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

    response = await fetch_stream(url, data)
    return response

response2 = await main()

#%%

def compare_keys_recursively(dict1, dict2, parent_key=''):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        return False

    # Combine keys from both dictionaries and eliminate duplicates
    all_keys = set(dict1.keys()) | set(dict2.keys())
    keys_match = True

    for key in all_keys:
        # Construct the full key path
        full_key = f"{parent_key}.{key}" if parent_key else key

        # Check if both dictionaries have the key
        if key in dict1 and key in dict2:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                # Recursively compare nested dictionaries
                if not compare_keys_recursively(dict1[key], dict2[key], full_key):
                    keys_match = False
            elif isinstance(dict1[key], dict) or isinstance(dict2[key], dict):
                print(f"Key structure mismatch at '{full_key}': one is a dictionary and the other is not.")
                keys_match = False
        else:
            # Key is missing in one of the dictionaries
            missing_in = "dict1" if key not in dict1 else "dict2"
            print(f"Missing key '{key}' in {missing_in} at path '{full_key}'")
            keys_match = False

    return keys_match

are_keys_same = compare_keys_recursively(response[0], response2[0])
print(f"Are keys the same: {are_keys_same}")
# %%

{'choices': [{'delta': {'role': 'assistant'},
   'context': {'data_points': {'text': ['Agriculture sector-  Rice Cultivation Emission Estimates using MODIS methodology.pdf#page=18: Version:Fall2022 18Figure 12a shows the temporal variation of summed annual methane emissions from rice cultivation in 23 major producing rice countries that derived from this study (available from 2015 to 2021) and FAOSTAT data (available from 2015 to 2021). The methane emission from rice cultivation in this study is lower than FAOSTAT data for all years. The 2015 to2021mean value for Paddy Watch data from this study was 20 million tonnes CH 4while the 2015 to 2019 mean value for FAOSTAT data was 23.8 million tonnes CH 4. The methane emission from rice cultivationrangesbetween18.9to21.6milliontonnesforPaddyWatchdataduring2015to2021 and23.4to24.0milliontonnesforFAOSTATdataduring2015to2019. For India and China, temporal variation of annual methane emission from this study and FAOSTAT data are presented in Figure 12b and c, respectively. For whole years, it shows that China methane emissions from this study (7.5 million tonnes CH 4) are higher than the data in FAOSTAT data (5.3 million tonnes CH 4), while methane emissions for India in this study (2.7 million tonnes CH 4) are lower than FAOSTAT data (4.',
      'Agriculture sector- Rice Cultivation Emissions Estimates using FAOSTAT methodology.pdf#page=1:  Introduction The following methodology estimates methane (CH 4 ) emissions from rice production using regional emissions factors (EFs) and nationally reported harvested rice area estimates, for countries where spatial delineation of rice paddies have not yet been independently modeled. Emissions modeling by Paddy Watch/ Universiti Malaysia Terengganu and WattTime. Version: Fall 2023 1 Climate TRACE member Universiti Malaysia Terengganu modeled rice cultivation emissions for 23 major rice producing countries globally , for years 2015 to 2022, using methods that incorporated local emissions factors, satellite imagery , and other independent approaches to detect where rice production occurred, the number of harvests in each paddy , and annual methane emissions. For the remaining countries that have rice cultivation but were not modeled, an approach was developed using emission factors from Universiti Malaysia Terengganu methodology (Table S1) and T he Food and Agriculture Organization (FAO) FAOST AT reported country-level rice paddy area harvested.',
      'Agriculture sector-  Rice Cultivation Emission Estimates using MODIS methodology.pdf#page=4: Version:Fall2022 4calculated at Tier 1 based on IPCC, 1997 Vol. 3, Ch. 4 and IPCC, 2002. For Asia countries, an area-weighted average EF was used, i.e., 15.7 g CH 4/m2/yr. For all other regions, the IPCC EF value was set either based on a neighboring country (where one existed), or the IPCC global defaultEFvalue(20gCH 4/m2/yr). In addition, global methane emission from rice cultivation reported by Saunois et al.(2016), Zhangetal.(2016) and Carlson etal.(2017) were also compared to the results fromthisstudy. Note that all three studies used FAOSTAT harvested rice area data as the main source data for theiremissionestimates. 2.2 Model CH4emissions from rice cultivation strongly depend on the harvested rice extent (IPCC, 1997). To generate methane emissions for this study, a simple approach was used to estimate CH 4 emissionsfromricecultivationatregionorcountry-i whichisgivenbyequation1(IPCC,1997): Emission i=AixEFi(Eq.1) TotalEmission= (Eq.2) 𝑖=1𝑁 ∑ 𝐸𝑚𝑖𝑠𝑠𝑖𝑜𝑛𝑖    WhereEmissionis the CH 4emissions (g CH 4year-1),Ais the rice paddy annual harvested area (m2) from MODIS-derived indices, and EFis the emission factor for seasonally rice ']},
    'thoughts': [{'title': 'Prompt to generate search query',
      'description': ['{\'role\': \'system\', \'content\': "Below is a history of the conversation so far, and a new question asked by the user that needs to be answered by searching in a knowledge base.\\n    You have access to Azure AI Search index with 100\'s of documents.\\n    Generate a search query based on the conversation and the new question.\\n    Do not include cited source filenames and document names e.g info.txt or doc.pdf in the search query terms.\\n    Do not include any text inside [] or <<>> in the search query terms.\\n    Do not include any special characters like \'+\'.\\n    If the question is not in English, translate the question to English before generating the search query.\\n    If you cannot generate a search query, return just the number 0.\\n    "}',
       "{'role': 'user', 'content': 'How did crypto do last year?'}",
       "{'role': 'assistant', 'content': 'Summarize Cryptocurrency Market Dynamics from last year'}",
       "{'role': 'user', 'content': 'What are my health plans?'}",
       "{'role': 'assistant', 'content': 'Show available health plans'}",
       "{'role': 'user', 'content': 'Generate search query for: Explain methane emissions from rice cultivation.'}"],
      'props': {'model': 'gpt-35-turbo', 'deployment': 'chat'}},
     {'title': 'Search using generated search query',
      'description': 'Explain methane emissions from rice cultivation',
      'props': {'use_semantic_captions': False,
       'use_semantic_ranker': True,
       'top': 3,
       'filter': None,
       'has_vector': True}},
     {'title': 'Search results',
      'description': [{'id': 'file-Agriculture_sector-__Rice_Cultivation_Emission_Estimates_using_MODIS_methodology_pdf-4167726963756C7475726520736563746F722D2020526963652043756C7469766174696F6E20456D697373696F6E20457374696D61746573207573696E67204D4F444953206D6574686F646F6C6F67792E706466-page-28',
        'content': 'Version:Fall2022 18Figure 12a shows the temporal variation of summed annual methane emissions from rice\ncultivation in 23 major producing rice countries that derived from this study (available from\n2015 to 2021) and FAOSTAT data (available from 2015 to 2021). The methane emission from\nrice cultivation in this study is lower than FAOSTAT data for all years. The 2015 to2021mean\nvalue for Paddy Watch data from this study was 20 million tonnes CH 4while the 2015 to 2019\nmean value for FAOSTAT data was 23.8 million tonnes CH 4. The methane emission from rice\ncultivationrangesbetween18.9to21.6milliontonnesforPaddyWatchdataduring2015to2021\nand23.4to24.0milliontonnesforFAOSTATdataduring2015to2019.\nFor India and China, temporal variation of annual methane emission from this study and\nFAOSTAT data are presented in Figure 12b and c, respectively. For whole years, it shows that\nChina methane emissions from this study (7.5 million tonnes CH 4) are higher than the data in\nFAOSTAT data (5.3 million tonnes CH 4), while methane emissions for India in this study (2.7\nmillion tonnes CH 4) are lower than FAOSTAT data (4.',
        'embedding': '[0.011604725, -0.020889822 ...+1534 more]',
        'imageEmbedding': None,
        'category': None,
        'sourcepage': 'Agriculture sector-  Rice Cultivation Emission Estimates using MODIS methodology.pdf#page=18',
        'sourcefile': 'Agriculture sector-  Rice Cultivation Emission Estimates using MODIS methodology.pdf',
        'oids': [],
        'groups': [],
        'captions': [],
        'score': 0.03226646035909653,
        'reranker_score': 3.539675235748291},
       {'id': 'file-Agriculture_sector-_Rice_Cultivation_Emissions_Estimates_using_FAOSTAT_methodology_pdf-4167726963756C7475726520736563746F722D20526963652043756C7469766174696F6E20456D697373696F6E7320457374696D61746573207573696E672046414F53544154206D6574686F646F6C6F67792E706466-page-2',
        'content': '\nIntroduction\nThe\nfollowing\nmethodology\nestimates\nmethane\n(CH\n4\n)\nemissions\nfrom\nrice\nproduction\nusing\nregional\nemissions\nfactors\n(EFs)\nand\nnationally\nreported\nharvested\nrice\narea\nestimates,\nfor\ncountries\nwhere\nspatial\ndelineation\nof\nrice\npaddies\nhave\nnot\nyet\nbeen\nindependently\nmodeled.\nEmissions\nmodeling\nby\nPaddy\nWatch/\nUniversiti\nMalaysia\nTerengganu\nand\nWattTime.\nVersion:\nFall\n2023\n1\nClimate\nTRACE\nmember\nUniversiti\nMalaysia\nTerengganu\nmodeled\nrice\ncultivation\nemissions\nfor\n23\nmajor\nrice\nproducing\ncountries\nglobally ,\nfor\nyears\n2015\nto\n2022,\nusing\nmethods\nthat\nincorporated\nlocal\nemissions\nfactors,\nsatellite\nimagery ,\nand\nother\nindependent\napproaches\nto\ndetect\nwhere\nrice\nproduction\noccurred,\nthe\nnumber\nof\nharvests\nin\neach\npaddy ,\nand\nannual\nmethane\nemissions.\nFor\nthe\nremaining\ncountries\nthat\nhave\nrice\ncultivation\nbut\nwere\nnot\nmodeled,\nan\napproach\nwas\ndeveloped\nusing\nemission\nfactors\nfrom\nUniversiti\nMalaysia\nTerengganu\nmethodology\n(Table\nS1)\nand\nT\nhe\nFood\nand\nAgriculture\nOrganization\n(FAO)\nFAOST AT\nreported\ncountry-level\nrice\npaddy\narea\nharvested.',
        'embedding': '[0.007677273, -0.029087035 ...+1534 more]',
        'imageEmbedding': None,
        'category': None,
        'sourcepage': 'Agriculture sector- Rice Cultivation Emissions Estimates using FAOSTAT methodology.pdf#page=1',
        'sourcefile': 'Agriculture sector- Rice Cultivation Emissions Estimates using FAOSTAT methodology.pdf',
        'oids': [],
        'groups': [],
        'captions': [],
        'score': 0.02454819157719612,
        'reranker_score': 3.358149528503418},
       {'id': 'file-Agriculture_sector-__Rice_Cultivation_Emission_Estimates_using_MODIS_methodology_pdf-4167726963756C7475726520736563746F722D2020526963652043756C7469766174696F6E20456D697373696F6E20457374696D61746573207573696E67204D4F444953206D6574686F646F6C6F67792E706466-page-9',
        'content': 'Version:Fall2022 4calculated at Tier 1 based on IPCC, 1997 Vol. 3, Ch. 4 and IPCC, 2002. For Asia countries, an\narea-weighted average EF was used, i.e., 15.7 g CH 4/m2/yr. For all other regions, the IPCC EF\nvalue was set either based on a neighboring country (where one existed), or the IPCC global\ndefaultEFvalue(20gCH 4/m2/yr).\nIn addition, global methane emission from rice cultivation reported by Saunois et al.(2016),\nZhangetal.(2016) and Carlson etal.(2017) were also compared to the results fromthisstudy.\nNote that all three studies used FAOSTAT harvested rice area data as the main source data for\ntheiremissionestimates.\n2.2 Model\nCH4emissions from rice cultivation strongly depend on the harvested rice extent (IPCC, 1997).\nTo generate methane emissions for this study, a simple approach was used to estimate CH 4\nemissionsfromricecultivationatregionorcountry-i whichisgivenbyequation1(IPCC,1997):\nEmission i=AixEFi(Eq.1)\nTotalEmission= (Eq.2)\n𝑖=1𝑁\n∑ 𝐸𝑚𝑖𝑠𝑠𝑖𝑜𝑛𝑖   \nWhereEmissionis the CH 4emissions (g CH 4year-1),Ais the rice paddy annual harvested area\n(m2) from MODIS-derived indices, and EFis the emission factor for seasonally rice ',
        'embedding': '[0.017560944, -0.021627828 ...+1534 more]',
        'imageEmbedding': None,
        'category': None,
        'sourcepage': 'Agriculture sector-  Rice Cultivation Emission Estimates using MODIS methodology.pdf#page=4',
        'sourcefile': 'Agriculture sector-  Rice Cultivation Emission Estimates using MODIS methodology.pdf',
        'oids': [],
        'groups': [],
        'captions': [],
        'score': 0.026916220784187317,
        'reranker_score': 3.3175551891326904}],
      'props': None},
     {'title': 'Prompt to generate answer',
      'description': ['{\'role\': \'system\', \'content\': "Assistant answers questions from users that are interested in information contained in Climate TRACE documents.\\n        Answer ONLY with the facts listed in the list of sources below. If there isn\'t enough information below, say you don\'t know. Do not generate answers that don\'t use the sources below. If asking a clarifying question to the user would help, ask the question.\\n        For tabular information return it as an html table. Do not return markdown format. If the question is not in English, answer in the language used in the question.\\n        Each source has a name followed by colon and the actual information, always include the source name for each fact you use in the response. Use square brackets to reference the source, for example [info1.txt]. Don\'t combine sources, list each source separately, for example [info1.txt][info2.pdf].\\n        \\n        \\n        "}',
       "{'role': 'user', 'content': 'Explain methane emissions from rice cultivation.\\n\\nSources:\\nAgriculture sector-  Rice Cultivation Emission Estimates using MODIS methodology.pdf#page=18: Version:Fall2022 18Figure 12a shows the temporal variation of summed annual methane emissions from rice cultivation in 23 major producing rice countries that derived from this study (available from 2015 to 2021) and FAOSTAT data (available from 2015 to 2021). The methane emission from rice cultivation in this study is lower than FAOSTAT data for all years. The 2015 to2021mean value for Paddy Watch data from this study was 20 million tonnes CH 4while the 2015 to 2019 mean value for FAOSTAT data was 23.8 million tonnes CH 4. The methane emission from rice cultivationrangesbetween18.9to21.6milliontonnesforPaddyWatchdataduring2015to2021 and23.4to24.0milliontonnesforFAOSTATdataduring2015to2019. For India and China, temporal variation of annual methane emission from this study and FAOSTAT data are presented in Figure 12b and c, respectively. For whole years, it shows that China methane emissions from this study (7.5 million tonnes CH 4) are higher than the data in FAOSTAT data (5.3 million tonnes CH 4), while methane emissions for India in this study (2.7 million tonnes CH 4) are lower than FAOSTAT data (4.\\nAgriculture sector- Rice Cultivation Emissions Estimates using FAOSTAT methodology.pdf#page=1:  Introduction The following methodology estimates methane (CH 4 ) emissions from rice production using regional emissions factors (EFs) and nationally reported harvested rice area estimates, for countries where spatial delineation of rice paddies have not yet been independently modeled. Emissions modeling by Paddy Watch/ Universiti Malaysia Terengganu and WattTime. Version: Fall 2023 1 Climate TRACE member Universiti Malaysia Terengganu modeled rice cultivation emissions for 23 major rice producing countries globally , for years 2015 to 2022, using methods that incorporated local emissions factors, satellite imagery , and other independent approaches to detect where rice production occurred, the number of harvests in each paddy , and annual methane emissions. For the remaining countries that have rice cultivation but were not modeled, an approach was developed using emission factors from Universiti Malaysia Terengganu methodology (Table S1) and T he Food and Agriculture Organization (FAO) FAOST AT reported country-level rice paddy area harvested.\\nAgriculture sector-  Rice Cultivation Emission Estimates using MODIS methodology.pdf#page=4: Version:Fall2022 4calculated at Tier 1 based on IPCC, 1997 Vol. 3, Ch. 4 and IPCC, 2002. For Asia countries, an area-weighted average EF was used, i.e., 15.7 g CH 4/m2/yr. For all other regions, the IPCC EF value was set either based on a neighboring country (where one existed), or the IPCC global defaultEFvalue(20gCH 4/m2/yr). In addition, global methane emission from rice cultivation reported by Saunois et al.(2016), Zhangetal.(2016) and Carlson etal.(2017) were also compared to the results fromthisstudy. Note that all three studies used FAOSTAT harvested rice area data as the main source data for theiremissionestimates. 2.2 Model CH4emissions from rice cultivation strongly depend on the harvested rice extent (IPCC, 1997). To generate methane emissions for this study, a simple approach was used to estimate CH 4 emissionsfromricecultivationatregionorcountry-i whichisgivenbyequation1(IPCC,1997): Emission i=AixEFi(Eq.1) TotalEmission= (Eq.2) 𝑖=1𝑁 ∑ 𝐸𝑚𝑖𝑠𝑠𝑖𝑜𝑛𝑖    WhereEmissionis the CH 4emissions (g CH 4year-1),Ais the rice paddy annual harvested area (m2) from MODIS-derived indices, and EFis the emission factor for seasonally rice '}"],
      'props': {'model': 'gpt-35-turbo', 'deployment': 'chat'}}]},
   'session_state': None,
   'finish_reason': None,
   'index': 0}],
 'object': 'chat.completion.chunk'}

{'choices': [{'delta': {'role': 'assistant'},
   'context': {'thoughts': [{'title': 'Prompt to generate answer',
      'description': ["{'role': 'system', 'content': 'Assistant answers questions, do your best.\\n        \\n        \\n        '}",
       "{'role': 'user', 'content': 'Explain methane emissions from rice cultivation.'}"],
      'props': {'model': 'gpt-35-turbo', 'deployment': 'chat'}}]},
   'session_state': None,
   'finish_reason': None,
   'index': 0}],
 'object': 'chat.completion.chunk'}