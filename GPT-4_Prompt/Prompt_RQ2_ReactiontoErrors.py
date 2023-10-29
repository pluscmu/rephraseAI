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

Effective tutoring responses on reacting to student errors should be:

Avoid using direct words about the student’s error (e.g., “it is incorrect,” “I saw an issue in your attempt”).
Implicitly clearing up the misconception (e.g., “we have another way of doing the math problem”).
Focus on student metacognition instead of explicit answers (for example, ask leading questions to draw students' attention implicitly to the location of errors, “Can you explain to me how you approached this problem?”).
Using effective praise to motivate students' learning (praise on student effort).
Express the sense of working together towards the joint goal might be helpful to improve students' learning experience in the tutoring process (e.g., “we can repeat the math together, what do you think?”, “Let’s work on it”)."
"""




lesson_Name = "Reacting to Error"



senario = """

The scenario is: Imagine you are a tutor to a student, Aaron, who has a long history of struggling with math. Aaron is not particularly motivated to learn math. He just finished a math problem adding a 3-digit and 2-digit number and has made a common mistake (shown below).
What exactly would you say to Aaron regarding his mistake to effectively respond in a way that increases his motivation to learn?
"""



examples_paraphrase = """
First Example:
Incorrect Response: I appreciate your effort, but your answer is wrong. Can you tell me what you did first?
Rephrased Response: I appreciate your effort. Let's try solving the problem together. Can you tell me what you did first?

Second Example:
Incorrect Response: Hi Carl, go ahead and finish working on the problem. You have made an error on the first step.
Rephrased Response: Hi Carl, I like how hard and focused you are working on this problem. Please explain to me how you approached the first step.
"""



instruction = lesson_principle + "The provided response attempts to answer to the following scenario." + senario + "\n Please rephrase the tutor's response according to the principle mentioned above to create a better example of" + lesson_Name + "Retain words and ideas from the tutor’s response. Limit changes to the original tutor's response to a minimum.   Maintain the same length as the original tutor's response.    Please rephrase as less words as possible from the original tutor's response.    Highest priority is to make sure to follow the principle of the correct response when rephrasing.    If the response does not answer the senario question, please return 'Your Answer Does Not Make Sense'."

def rq2zeroshot(inputresponse):
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": systemheader},
            {"role": "user", "content": instruction},
            {"role": "assistant", "content": "Sure, please enter the tutor's response you would like to rephrase"},
            {"role": "user", "content": inputresponse}
                ], 
            temperature = 0
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
            temperature = 0
        )
    
    return res['choices'][0]['message']['content']



rq2fewshot(inputresponse)



classify2 = rq2fewshot(newresponse)



classify2



