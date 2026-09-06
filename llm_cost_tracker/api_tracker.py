from openai import OpenAI
import os
from dotenv import load_dotenv


from llm_cost_tracker.tracker import calculate_cost
from llm_cost_tracker.logger import log_usage

# Load env variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def tracked_chat(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        # 🔍 Extract usage
        usage = response.usage

        prompt_tokens = usage.prompt_tokens
        completion_tokens = usage.completion_tokens
        total_tokens = usage.total_tokens

        # 💰 Calculate cost
        cost = calculate_cost(total_tokens)

        # 📝 Log usage
        log_usage({
            "tokens": total_tokens,
            "cost": cost,
            "model": "gpt-4o-mini"
        })

        return response.choices[0].message.content

    except Exception as e:
        print("Error:", e)