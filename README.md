# YouTube Audio Mashup 🎵

A powerful command-line utility that downloads videos from YouTube, extracts the audio, cuts them to a specific duration, and merges them into a single, seamless audio mashup.

Created by **Gurdarshan Singh** (Roll No: 102303217).

## 🚀 Features
- **Automated Searching:** Pass the singer/artist name, and it automatically finds the top videos.
- **Direct Audio Extraction:** Uses `yt-dlp` to download high-quality audio directly.
- **Precision Trimming:** Cuts the first `Y` seconds from every downloaded track using `pydub`.
- **Seamless Merging:** Combines all trimmed clips into one clean `.mp3` output file.

## 🛠 Prerequisites
This tool relies on `pydub` to process audio, which requires **FFmpeg** to be installed on your system.

**Mac:**
```bash
brew install ffmpeg
```
**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install ffmpeg
```
**Windows:** Download from [FFmpeg official site](https://ffmpeg.org/download.html) and add it to your system PATH.

## 📦 Installation

You can install this package directly from PyPI:

```bash
pip install Mashup-Gurdarshan-102303217
```

## 💻 Usage

Once installed, you can use the globally available `mashup` command in your terminal.

**Syntax:**
```bash
mashup <SingerName> <NumberOfVideos> <AudioDurationInSeconds> <OutputFileName.mp3>
```

**Example:**
```bash
mashup "Arjan Dhillon" 15 20 my_mashup.mp3
```

### Constraints:
* The Number of Videos ($N$) must be **greater than 10**.
* The Audio Duration ($Y$) must be **greater than 20 seconds**.

## 📝 License
This project is for educational purposes as part of a university assignment.
