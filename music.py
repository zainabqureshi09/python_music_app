import tkinter as tk
from tkinter import filedialog, Listbox, messagebox
from pygame import mixer

# Initialize the main window
root = tk.Tk()
root.title("Python Music Player")
root.geometry("400x300")

# Initialize pygame mixer
mixer.init()

# List to hold songs
playlist = []

# Function to load songs into the playlist
def load_songs():
    songs = filedialog.askopenfilenames(title="Choose songs", filetypes=[("MP3 Files", "*.mp3")])
    for song in songs:
        playlist.append(song)
        song_list.insert(tk.END, song.split("/")[-1])

# Function to play the selected song
def play_song():
    selected_song = song_list.curselection()
    if selected_song:
        song = playlist[selected_song[0]]
        mixer.music.load(song)
        mixer.music.play()
    else:
        messagebox.showwarning("Warning", "Please select a song to play.")

# Function to pause the song
def pause_song():
    mixer.music.pause()

# Function to resume the song
def resume_song():
    mixer.music.unpause()

# Function to stop the song
def stop_song():
    mixer.music.stop()

# Function to set the volume
def set_volume(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)

# Create UI elements
load_button = tk.Button(root, text="Load Songs", command=load_songs)
play_button = tk.Button(root, text="Play", command=play_song)
pause_button = tk.Button(root, text="Pause", command=pause_song)
resume_button = tk.Button(root, text="Resume", command=resume_song)
stop_button = tk.Button(root, text="Stop", command=stop_song)
volume_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=set_volume, label="Volume")
song_list = Listbox(root, selectmode=tk.SINGLE)

# Place UI elements on the window
load_button.pack(pady=5)
song_list.pack(pady=10, fill=tk.BOTH, expand=True)
play_button.pack(pady=5)
pause_button.pack(pady=5)
resume_button.pack(pady=5)
stop_button.pack(pady=5)
volume_slider.pack(pady=5)

# Set default volume
volume_slider.set(70)
mixer.music.set_volume(0.7)

# Start the main loop
root.mainloop()
