#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
get_ipython().run_line_magic('run', './LinkTest.ipynb')

while True:
    try:
        publica_test_account = """
        SELECT s.id as site_id from sites s
        join publishers p on p.id = s.publisher_id
        where p.id = 1"""
        publica_test_account = model_query(publica_test_account)
        publica_test_account = pd.DataFrame(publica_test_account)
        publica_test_account = list(publica_test_account['site_id'])
        site_id = int(input('Enter site/channel id (limited to sites in test account): '))
        assert site_id in publica_test_account
        num_of_requests = int(input('Enter number of endpoint requests to be made: '))
        publica_base_url = "https://pbs.getpublica.com/v1/s2s-hb?site_page=boris_jira_123&format=vast&site_id="
        get_ipython().system('ab -n "$num_of_requests" -c 10 "$publica_base_url$site_id"')
        break
    except AssertionError:
        print('Site ID not found under test account, please try again.')


# In[ ]:




