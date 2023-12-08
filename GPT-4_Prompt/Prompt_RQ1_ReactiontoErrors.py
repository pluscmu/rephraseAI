#!/usr/bin/env python
# coding: utf-8

# - Step 1: Classifier to determine if the response if correct or incorrect
# - Step 2: Paraphrase with GPT4




import pandas as pd
import numpy as np
import os
import openai




inputresponse = "any Wrong Response"


# ########################################
# Step 1: Classifier to determine if the response if correct or incorrect
############################################


example_incorrect = """
Examples of Incorrected Responses:

1. Let's try solving the problem together.
2. Good effort.
3. I got a different answer. Let's look at this together.
4. Do you know about carrying the 1?
5. Kanye, let me show you how this should be done.
"""


example_correct = """
Examples of Corrected Responses:

1. Lucy, great start! Explain how you passed to the second column.
2. Thank you for showing me your work, Lucy. You worked hard on adding these numbers. I am going to work on this problem with you. Can you tell me how you added the numbers first?
3. Well done setting up the problem, Lucy. Can you tell me how you went about calculating the first few steps?
4. I like your effort, but show me what you are trying to do in the second step.
5. Kanye, very well done. Your effort was very valuable. Can you repeat how you arrived at this result? Let's do this problem together.
"""



instruction1 = """
Please determine according to the classifier schema, if the following 
response contains the correct reaction to the student's error? If it does, 
please respond YES; if it does not, please respond NO.
"""

principle = """"
The following is the principle that a correct response should follow:

Effective tutoring responses on reacting to student errors should be:

Avoid using direct words about the student’s error (e.g., “it is incorrect,” “I saw an issue in your attempt”).
Implicitly clearing up the misconception (e.g., “we have another way of doing the math problem”).
Focus on student metacognition instead of explicit answers (for example, ask leading questions to draw students' attention implicitly to the location of errors, “Can you explain to me how you approached this problem?”).
Using effective praise to motivate students' learning (praise on student effort).
Express the sense of working together towards the joint goal might be helpful to improve students' learning experience in the tutoring process (e.g., “we can repeat the math together, what do you think?”, “Let’s work on it”)."
"""

def zeroshot(p):
    res = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[
        {"role": "system", "content": "You are a binary classifier."},
        {"role": "user", "content": principle+ instruction1},
        {"role": "assistant", "content": "Sure, please enter the response from tutor"},
        {"role": "user", "content": p}
          ], 
      max_tokens=1
    )
    
    return res['choices'][0]['message']['content']




def fewshot(p):
    res = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[
        {"role": "system", "content": "You are a binary classifier."},
        {"role": "user", "content": principle+ instruction1},
        {"role": "assistant", "content": "please provide some examples of correct and incorrect response"},
        {"role": "user", "content": example_correct +example_incorrect },
        {"role": "assistant", "content": "Sure, please enter the response from tutor"},
        {"role": "user", "content": p}
          ], 
      max_tokens=1
    )
    
    return res['choices'][0]['message']['content']


classify1 = fewshot(inputresponse)



classify1

