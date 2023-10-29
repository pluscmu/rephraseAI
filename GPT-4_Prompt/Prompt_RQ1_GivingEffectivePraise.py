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
Examples of Corrected Responses:
1. You got it! There are many ways to solve math problems and learn math. Now that we have connected, let's solve some more problems.
2. You can do this! Just take it one step at a time.
"""

example_correct = """
Examples of Corrected Responses:

1. Kevin, you didn't give up, and you managed to learn. Congratulations! Let's finish your math homework together so you can still get a good grade and learn how this kind of homework will be easier sooner.
2. You're doing a great job working on this paragraph! It can be tricky to find the right words, and I think you're doing really well working through it.
"""

instruction1 = """According to the lesson principle, please determine if the following response contains praising for learning effort. If the following response contains praising for learning effort, please respond YES; if not, please respond NO."""



principle = """


The following is the principle that a correct response should follow: 

Studies show praise is most effective when it has certain qualities.
Praise should be:

perceived as sincere, earned, and truthful.
specific by giving details of what the student did well.
immediate with praise given right after the student action.
authentic and is not repeated often, such as "great job" which loses meaning and becomes predictable.
focused on the learning process, not ability

Giving students consistent, specific praise when they perform in a desired manner is important to motivate students and increase their engagement to learn. Expert tutors and research suggest giving praise that focuses on the process and not merely student ability. Process-focused praise recognizes students for putting forth effort and persevering through the learning process instead of focusing on whether a student got the problem correct or pure ability. Process-focused praise motivates students to learn and fosters a growth mindset (Dweck, 2008).

Some common examples of ability-focused praise are shown on the left in the table below with a corresponding more effective process-focused praise shown on the right. It is important to note that praise can be given throughout the learning process, not only upon getting the correct answer or finishing a problem or assignment. Oftentimes, encouragement and praise can be given while the student is going through the learning process to increase motivation and maintain engagement.

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
      max_tokens=10
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
      max_tokens=10
    )
    
    return res['choices'][0]['message']['content']






classify1 = fewshot(inputresponse)


classify1


