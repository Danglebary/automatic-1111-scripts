import math
import os
import sys
import traceback

# Remove this line when adding this script to your automatic-1111 installation
sys.path.append("automatic-1111")

import modules.scripts as scripts
import gradio as gr

from modules.processing import Processed, process_images

class Script(scripts.Script):
    def title(self):
        return "Multi-run"

    def ui(self, is_img2img):
        nTimes = gr.Textbox(label="Number of times to run", placeholder="1")
        increment = gr.Textbox(label="Value to increment seed by", placeholder="1")
        incrementDir = gr.Radio(["Positive", "Negative"], label="Increment direction")
        return [nTimes, increment, incrementDir]

    def run(self, p, nTimes, increment, incrementDir):
        for x in range(int(nTimes)):
            p.seed = increment if incrementDir == "Positive" else -increment
            proc = process_images(p)
            image = proc.images
        return Processed(p, image, p.seed, proc.info)