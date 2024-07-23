# _*_ coding: utf-8 _*_

import os
from dotenv import load_dotenv

load_dotenv()
openai_organization = os.getenv('OPENAI_ORGANIZATION')
openai_api_key = os.getenv('OPENAI_API_KEY')
