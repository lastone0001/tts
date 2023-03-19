#!/bin/bash


# Get the selected text using xclip
selected_text=$(xclip -o)

# Copy the selected text to the clipboard using xclip
echo -n "$selected_text" | xclip -selection clipboard


# Run the Python script in the background
path=$(python '/home/kapil/PycharmProjects/coquiai-TTS/main.py')

gnome-terminal -- mpv $path

# echo $path