from src.ad_keyword_plan import create_keyword_plan 
from src.ad_keyword_plan import create_keyword_plan_campaign
from src.ad_keyword_plan import create_keyword_plan_ad_group
from src.ad_keyword_plan import create_keyword_plan_ad_group_keywords

from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

import argparse
import sys
import uuid
import json 
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

googleads_client = GoogleAdsClient.load_from_storage("google-ads.yaml")
client=googleads_client
customer_id=1071190592
word=   "data"
customer_id=str(customer_id).encode("utf-8").decode("utf-8") 

keyword_list=[]
word_info={}

import json


with open("dict_word.json","r") as f:
    data = json.load(f)

for element in data:
    word=element['name']
    keyword_plan = create_keyword_plan(client, customer_id)
    keyword_plan_campaign = create_keyword_plan_campaign(
        client, customer_id, keyword_plan
    )
    keyword_plan_ad_group = create_keyword_plan_ad_group(
        client, customer_id, keyword_plan_campaign
    )
    new_word=create_keyword_plan_ad_group_keywords(
        client, customer_id, keyword_plan_ad_group, word
    )
    word_info['name']=new_word[0]
    word_info['ID']=new_word[1]
    
    keyword_plan_id=keyword_plan.split('/')[3]
    keyword_plan_id
    
    keyword_plan_service = client.get_service("KeywordPlanService")
    resource_name = keyword_plan_service.keyword_plan_path(
        customer_id, keyword_plan_id
    )

    response = keyword_plan_service.generate_forecast_metrics(
        keyword_plan=resource_name
    )
    for i, forecast in enumerate(response.keyword_forecasts):
            print(f"#{i+1} Keyword ID: {forecast.keyword_plan_ad_group_keyword}")

            metrics = forecast.keyword_forecast

            click_val = metrics.clicks
            clicks = f"{click_val:.2f}" if click_val else "unspecified"
            print(f"Estimated daily clicks: {clicks}")

            imp_val = metrics.impressions
            impressions = f"{imp_val:.2f}" if imp_val else "unspecified"
            print(f"Estimated daily impressions: {impressions}")

            cpc_val = metrics.average_cpc
            cpc = f"{cpc_val:.2f}" if cpc_val else "unspecified"
            print(f"Estimated average cpc: {cpc}\n")
            # [END generate_forecast_metrics]
    word_info['CPC']=cpc_val
    word_info['occurences']=element['occurences']
    keyword_list.append(word_info)
    word_info={}
    keyword_list

# create json object from dictionary
# open file for writing, "w" 
with open("dict_word_final.json","w") as f:
    json.dump(keyword_list, f)

for i, forecast in enumerate(response.keyword_forecasts):
        print(f"#{i+1} Keyword ID: {forecast.keyword_plan_ad_group_keyword}")

        metrics = forecast.keyword_forecast

        click_val = metrics.clicks
        clicks = f"{click_val:.2f}" if click_val else "unspecified"
        print(f"Estimated daily clicks: {clicks}")

        imp_val = metrics.impressions
        impressions = f"{imp_val:.2f}" if imp_val else "unspecified"
        print(f"Estimated daily impressions: {impressions}")

        cpc_val = metrics.average_cpc
        cpc = f"{cpc_val:.2f}" if cpc_val else "unspecified"
        print(f"Estimated average cpc: {cpc}\n")
        # [END generate_forecast_metrics]


word_info['CPC']=cpc_val

keyword_list.append(word_info)
word_info={}
keyword_list
