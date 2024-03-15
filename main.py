from os import getenv

import yaml
from openai import OpenAI
from pygame import mixer

client = OpenAI(
  base_url=getenv("OPENAI_API_URI"),
  api_key=getenv("OPENAI_API_KEY"),
)

# Load the config file
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Initialize the audio mixer
mixer.init()


def play_song(song_file):
    mixer.music.load("music/" + song_file)
    mixer.music.play()


def get_song_recommendation(story_state, message_history):
    messages = message_history + [{"role": "user",
                                   "content": f"Given the current story state:\n{story_state}\n\nWhich song from the config file would be most appropriate to play now? Respond with only the filename of the song."}]

    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=messages,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )

    song_filename = response.choices[0].message.content.strip()
    message_history.append({"role": "assistant", "content": song_filename})
    return song_filename, message_history


def main():
    current_song = None
    message_history = [{"role": "system",
                        "content": f"You are a helpful assistant that recommends appropriate songs based on the current story state." +
                        f"The songs are {str(config['songs'])}"}]

    while True:
        story_state = input("Enter the current state of the story (or 'quit' to exit): ")

        if story_state.lower() == "quit":
            break

        recommended_song, message_history = get_song_recommendation(story_state, message_history)

        if recommended_song != current_song:
            if recommended_song in config["songs"]:
                play_song(recommended_song)
                current_song = recommended_song
                print(f"Now playing: {recommended_song}")
            else:
                print(f"Song not found in config: {recommended_song}")


if __name__ == "__main__":
    main()
