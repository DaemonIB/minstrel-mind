# Minstrel Mind - AI-Powered Music Recommendation for Story-Driven Games

This application utilizes the OpenAI Chat Completion API to recommend and play appropriate songs based on the current state of a story in a game. It reads a configuration file (`config.yaml`) containing song information and uses the OpenAI API to determine which song should be played given the current story state.

## Features

- Reads song information (filename, tags) from a YAML configuration file
- Uses the OpenAI Chat Completion API to recommend songs based on the current story state
- Plays the recommended song using the Pygame mixer library
- Maintains a conversation history for context-aware song recommendations

## Prerequisites

- Python 3.x
- OpenAI API key

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/DaemonIB/minstrel-mind.git
   ```

2. Install the required libraries:

   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:

   - Sign up for an OpenAI account and obtain an API key.
   - Set the environment variable `OPENAI_API_URI` to your actual API key.
   - Set the environment variable `OPENAI_API_KEY` to your actual API key.

4. Create a `config.yaml` file in the same directory as the script with the following structure:

   ```yaml
   songs:
     song1.mp3:
       tags: [tag1, tag2]
     song2.mp3:
       tags: [tag3, tag4]
   ```

   Make sure to provide the correct song filenames, tags, and descriptions.

## Usage

1. Run the script:

   ```
   python music_recommendation.py
   ```

2. Enter the current state of the story when prompted. The script will recommend an appropriate song based on the story state and play it using the Pygame mixer.

3. To exit the script, enter 'quit' when prompted for the story state.

## Configuration

The `config.yaml` file contains the song information used by the script. Each song entry should have the following structure:

```yaml
song_filename.mp3:
  tags: [tag1, tag2, ...]
```

- `song_filename.mp3`: The filename of the song file (including the extension).
- `tags`: A list of tags associated with the song (optional).

Make sure to update the `config.yaml` file with your own song information.

All songs in the list must exist in the `music` folder so that they can be played. The name must verbatim match the yaml.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under [Apache-2.0](LICENSE).