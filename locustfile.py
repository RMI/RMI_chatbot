import random
import time

from locust import HttpUser, between, task


class ChatUser(HttpUser):
    wait_time = between(5, 20)

    @task
    def ask_question(self):
        self.client.get("/")
        time.sleep(5)
        self.client.post(
            "/chat",
            json={
                "messages": [
                    {
                        "content": random.choice(
                            [
                                "Explain emissions from steel production.",
                                "How do landfills create methane?",
                                "What are the sources of emissions from solar power?",
                                "Explain upstream, midstream, and downstream oil and gas emissions.",
                            ]
                        ),
                        "role": "user",
                    },
                ],
                "context": {
                    "overrides": {
                        "retrieval_mode": "hybrid",
                        "semantic_ranker": True,
                        "semantic_captions": False,
                        "top": 3,
                        "suggest_followup_questions": False,
                    },
                },
            },
        )
        time.sleep(5)
        self.client.post(
            "/chat",
            json={
                "messages": [
                    {"content": "How do landfills create methane?", "role": "user"},
                    {
                        "content": "Landfills contain organic material that breaks down. If this happens in the abscence of oxygen because the landfill is deep or covered, it will create methane instead of carbon dioxide. [report-1.pdf]. This process happens over months, years, and even decades, depending on the material. [report-1.pdf].",
                        "role": "assistant",
                    },
                    {"content": "Explain hydrogen cars.", "role": "user"},
                ],
                "context": {
                    "overrides": {
                        "retrieval_mode": "hybrid",
                        "semantic_ranker": True,
                        "semantic_captions": False,
                        "top": 3,
                        "suggest_followup_questions": False,
                    },
                },
            },
        )
