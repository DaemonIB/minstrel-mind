# Music Folder

This folder contains all the audio files that can be loaded and played by the Minstrel Mind application.

## Audio File Naming Convention

To ensure that the Minstrel Mind application can correctly match the audio files with their corresponding entries in the `config.yaml` file, it is crucial to follow a specific naming convention:

- The name of the audio file in this folder should match verbatim the song name specified in the `config.yaml` file.
- The audio files should be placed directly in the "music" folder, without any subfolders.

## Example

Here's an example of how the audio file should be named and placed in the "music" folder:

```
music/test1.mp3
```

This audio file should have a corresponding entry in the `config.yaml` file, like this:

```yaml
songs:
  test1.mp3:
    tags: [calm, town, light]
```

In this example, the audio file "test1.mp3" is placed in the "music" folder, and its corresponding entry in the `config.yaml` file has the same name "test1.mp3" under the "songs" section.

## Supported Audio Formats

The Minstrel Mind application supports various audio formats, including:

- MP3 (.mp3)
- WAV (.wav)
- OGG (.ogg)

Make sure your audio files are in one of these supported formats.

## Adding New Audio Files

To add a new audio file to the Minstrel Mind application:

1. Place the audio file in the "music" folder, ensuring that it follows the naming convention described above.
2. Open the `config.yaml` file and add a new entry under the "songs" section for the newly added audio file. Specify the tags and any other relevant information for the song.
3. Save the `config.yaml` file.