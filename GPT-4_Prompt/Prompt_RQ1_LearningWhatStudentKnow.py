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
Examples of Incorrect Responses: 
1. Hi Roberto, we will figure this problem together , okay? 
2. after parenthesis and then exponents, perform the indicated multiplication or divison, follow the order, from left to right.  So for example, looking at your problem, perform the 5/5 first before the multiplication by 2  See how we did the division first then multiplication?
3. Sure no problem.  So 2 sides of the triangle are of equal length, correct?  (An isosceles triangle.)
4. on scale from 1-4 (1-easy, 4- difficult ) , how difficult is that question ?
5. Sure no problem.  So 2 sides of the triangle are of equal length, correct?  (An isosceles triangle.)
"""



example_correct = """
Examples of Correct Responses: 
1. What information can you get from the figure above? 
2. Looks like you've started solving the problem. Can you share a little bit more about how you came up with the first part of your answer?
3. What ideas do you have on how to start this problem?
4. That looks great so far.  Can you explain what is the meaning of the letters?
5. This is a solid start. It looks like you\'re using \'PEMDAS,\' the acronym for the \'order of operations\' in math, and \'P\' stands for \'parentheses.\' Sine you already identified and simplified the parenthese well in that first step, what do you think the next step, "E," stands for? Is that something you have in your notes from class?
"""




instruction1 = """
Please determine according to the training lesson principle, if the following response contains the correct question to learn what the student knows. If it does, please respond YES; if it does not, please respond NO.
"""


principle = """

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



def zeoshot(p):
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

