#!/usr/bin/env python
# coding: utf-8

# - Step 1: Classifier to determine if the response if correct or incorrect
# - Step 2: Paraphrase with GPT4




import pandas as pd
import numpy as np
import os
import openai




inputresponse = "any Wrong Response"



# ############################
# Step 2: Paraphrase with GPT4
# ###########################




systemheader = "You are rephrasing tutor's response."



lesson_principle = """

The following is the principle that a correct response should follow: 

Praising students for working hard and putting forth effort is a great way to increase student motivation. When the learning gets tough, giving effective praise is a powerful strategy to encourage students to keep going.
The correct response should be : 
-perceived as sincere, earned, and truthful.
-specific by giving details of what the student did well.
-immediate with praise given right after the student action.
-authentic and is not repeated often, such as “great job” which loses meaning and becomes predictable.
-focused on the learning process, not ability
(AJTutoring.com, 2022)

Tutor responses must follow some, but not all the above. To receive full credit they cannot just say “great job” and praise with no specific reasoning. They need to be praised for effort or the process AND be positive and encouraging.


"""



lesson_Name = "Giving Effective Praise"




senario = """
The scenario is: You're tutoring a student named Kevin. He is struggling to understand a math problem. When he doesn't get the answer correct the first time, he wants to quit. After trying several different approaches, Kevin gets the problem correct. As Kevin's tutor, you want him to continue working through solving more problems on his math assignment.

What exactly would you say to Kevin to provide effective praise that will increase his motivation to complete his math assignment and increase engagement?"

"""

examples_paraphrase = """
First Example:
Incorrect Response: Kevin, fantastic job! I’m impressed with your smartness and completing the problem. 
Rephrased Response: Kevin, fantastic job solving the math problem. I'm impressed with your hard work in persevering through the problem!

Second Example:
Incorrect Response: Carla, you are doing a great job! You understand it correctly, you are so smart!
Rephrased Response: Carla, you are doing a great job in continuing on the assignment. Your understanding is improving as we work through it.
"""




instruction = lesson_principle + 
"The provided response attempts to answer to the following scenario." + senario + 
"\n Please rephrase the tutor's response according to the principle mentioned above to create a better example of" + 
lesson_Name + "Retain words and ideas from the tutor’s response. Limit changes to the original tutor's response to a minimum.   Maintain the same length as the original tutor's response.    Please rephrase as less words as possible from the original tutor's response.    Highest priority is to make sure to follow the principle of the correct response when rephrasing."

def rq2zeroshot(inputresponse):
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": systemheader},
            {"role": "user", "content": instruction},
            {"role": "assistant", "content": "Sure, please enter the tutor's response you would like to rephrase"},
            {"role": "user", "content": inputresponse}
                ], 
           # max_tokens=60,
            temperature = 1
        )
    
    return res['choices'][0]['message']['content']


def rq2fewshot(inputresponse):
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": systemheader},
            {"role": "user", "content": instruction},
            {"role": "assistant", "content": "Please provide some examples of how you will rephrase the given incorrect response to make it correct"},
            {"role": "user", "content":examples_paraphrase},
            {"role": "assistant", "content": "Sure, please enter the tutor's response you would like to rephrase"},
            {"role": "user", "content": inputresponse}
                ], 
           # max_tokens=60,
            temperature = 1
        )
    
    return res['choices'][0]['message']['content']




newresponse = rq2fewshot(inputresponse)

newresponse

classify2 = fewshot(newresponse)


