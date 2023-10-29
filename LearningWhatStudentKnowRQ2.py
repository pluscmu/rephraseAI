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

Research demonstrates by learning what a student knows a coach can leverage student responses to efficiently diagnose their level of understanding at the start of the session and use this as a launching point for the rest of the session. In addition, asking a student to explain what they already know will also uncover misconceptions they have so that coaches can correct them. Lastly, a coach should ask questions and offer support as a student attempts the problem themselves. This effortful learning is called productive struggle. It's important to empower a student to find the answer themselves based on their prior knowledge and logic before teaching them a concept explicitly. To summarize, researchers suggest a coach should: Assess a student’s prior knowledge. Guide the conversation to catch student's misconceptions or errors. Support productive struggle (YUP, 2021).

Tutors' responses need to have elements of the bold phrases above. If the response is asking a specific content-related question, and in particular if it is a yes or no question, they are marked as incorrect. For example, “Do you know what PEMDAS means?” or “Do you know what the tick marks on the triangle indicate?” Tutors’ responses can contain questions to students but they must be “open” and not specific to assess student’s knowledge of an individual knowledge component. There is an exception- for the order of operation scenario, the student wrote PEMDAS on his paper, therefore, a correct response from a tutor may elude to explaining what it means to gauge student’s understanding

Effective tutoring responses on determining what student know should be:
- The question (assessing student knowledge) should be backward and open-ended. “What have you done so far?”
- The question should avoid specific content 
- Forward question (next step on the problem) might be not learning what students know, but about promoting student independent learning skills, “what is the next step”)
- If backward open-ended questions (assessing student knowledge) in the tutor response, we can consider it as the correct response
- If a tutor asking a forward question about the learning concept that a student has already known, it should be Learning what students know, e.g., “You correctly wrote down "PEMDAS" for the order of operations, and just did the "P" part. That's great!  Based on what you already wrote, what do you think should come next?”
"""




lesson_Name = "Determing What Student Know"




senario = """
The scenario is: You are working with a student named Cindy on her math homework. She is having trouble solving a geometry problem dealing with triangles. She shows you the following diagram displaying a triangle and states that she has to determine the value of angle x. Cindy says, 'I don't know what to do.'
What exactly would you say to Cindy to begin helping her solve the math problem
"""




examples_paraphrase = """
First Example:
Incorrect Response: To begin, Cindy, do you know what type of triangle is this? 
Rephrased Response: "Let's talk about how to begin, Cindy. What do you know about the triangle?"

Second Example:
Incorrect Response: Roberto, what do you think is the coefficient of x in this problem?
Rephrased Response: "Roberto, upon looking at this problem, what do you know?"
"""




instruction = lesson_principle + "The provided response attempts to answer to the following scenario." + senario + "\n Please rephrase the tutor's response according to the principle mentioned above to create a better example of" + lesson_Name + "Retain words and ideas from the tutor’s response. Limit changes to the original tutor's response to a minimum.   Maintain the same length as the original tutor's response.    Please rephrase as less words as possible from the original tutor's response.    Highest priority is to make sure to follow the principle of the correct response when rephrasing."
 
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
            {"role": "assistant", "content": "Please provide some examples of how you will re-write the given incorrect response to make it correct"},
            {"role": "user", "content":examples_paraphrase},
            {"role": "assistant", "content": "Sure, please enter the tutor's response you would like to rephrase"},
            {"role": "user", "content": inputresponse}
                ], 
           # max_tokens=60,
            temperature = 1
        )
    
    return res['choices'][0]['message']['content']




rq2fewshot(inputresponse)

