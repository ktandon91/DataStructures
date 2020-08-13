note = """
Issue is related To : Others

Issue Sub-Category : MISC Data request

Issue Description : 
Due to system issue my Leaves were deducted and my leaves lead to -4 hence as an impact it lead to LOP and my salary got deducted could you please help me to re

"""

import re

issue_category = r"Issue is related To : (.*?)\n"
issue_sub_category = r"Issue Sub-Category : (.*?)\n"
issue_desc  = r"Issue Description : \n(.*?)\n"

result = re.search(issue_desc, note)

print(result.group(1))

