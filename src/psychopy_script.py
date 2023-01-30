# -*- coding: utf-8 -*-
"""
Psychopy Script for Embody experiment.
"""
import random
from psychopy import visual, core, event

# Create a window to display the stimuli
win = visual.Window(size=(800, 600), color="white", units="pix")

# Create an output file to save the responses
output_file = open("responses.txt", "w")


# Create a text stimulus for the instructions screen
instructions = visual.TextStim(win, text="Please watch the video carefully and answer the questions afterwards.", pos=(0, 0))

# Display the instructions for 5 seconds
instructions.draw()
win.flip()
core.wait(5)

# Load and play the video for the first practice screen
video = visual.MovieStim(win, "path/to/video.mp4", size=(800, 600))
video.play()
while video.status != visual.FINISHED:
    video.draw()
    win.flip()

# Create a list of questions and randomize their order
questions = ["How positive you found this video?", 
             "How negative you found this video?", 
             "How hungry this video made you feel?", 
             "How disgusting you found this video?", 
             "How arousing was this video?", 
             "How boring was this video"]
random.shuffle(questions)

# Create a list of sliders for the practice screen
sliders = []
for i in range(6):
    slider = visual.Slider(win, size=(300, 30), pos=(0, -200 + i * 50), labels=["0", "10"], granularity=0.1)
    sliders.append(slider)

# Ask the questions and record the responses
responses = {}
for i, question in enumerate(questions):
    question_stim = visual.TextStim(win, text=question, pos=(0, 0))
    question_stim.draw()
    sliders[i].draw()
    win.flip()
    event.waitKeys(keyList=["return"])
    responses[question] = sliders[i].getRating()


# Create a text stimulus for the second instructions screen
instructions = visual.TextStim(win, text="When you're ready, click on the X button to begin the experiment.", pos=(0, 0))

# Display the instructions for 5 seconds
instructions.draw()
win.flip()
event.waitKeys(keyList=["x"])

# Create a list of blocks
blocks = ["P", "N", "NU", "H", "D"]
random.shuffle(blocks)

# Randomize the list of questions again
random.shuffle(questions)

# Create a list of sliders for the experiment
sliders = []
for i in range(6):
    slider = visual.Slider(win, size=(300, 30), pos=(0, -200 + i * 50), labels=["0", "11"], granularity=0.1)
    sliders.append(slider)

# Repeat the experiment for each block
for block in blocks:
    # Load the videos for the block
    videos = []
    for i in range(7):
        videos.append(visual.MovieStim(win, f"path/to/{block}{i+1}.mp4", size=(800, 600)))
    random.shuffle(videos)
    output_file.write(f"Block: {block}\n")
    # Present the videos and the questions
    for video in videos:
        video.play()
        while video.status != visual.FINISHED:
            video.draw()
            win.flip()
        for i, question in enumerate(questions):
            question_stim = visual.TextStim(win, text=question, pos=(0, 0))
            question_stim.draw()
            sliders[i].draw()
            win.flip()
            event.waitKeys(keyList=["return"])
            response = sliders[i].getRating()
            output_file.write(f"{question}: {response}\n")


# Close the window and end the experiment
win.close()
core.quit()
