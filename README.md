-----

## 🤖 Gonk Discord Bot

Gonk is a Utility Discord bot designed to enhance discord servers with **media manipulation tools**, an engaging **currency system**, **AI interaction**, and fun **mini-games**\!

-----

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| **Media Editing** | Add audio to videos/images, resize images, reverse videos, and convert media to GIFs. |
| **Media Download** | Easily download videos and images from popular platforms like **YouTube**, **Reddit**, and **Twitter**. |
| **AI Interaction** | Chat and get creative responses using the power of the **Gemini API**. |
| **Currency System** | A persistent server-wide currency for rewards, betting, and future features. |
| **Games** | Enjoy classic mini-games: **Tic-Tac-Toe**, **Rock Paper Scissors**, **Coin Flip**, and **8-Ball**. |

-----

## 🚀 How to Use

All commands are prefixed with `!` (or substitute with your actual prefix).

### 🎬 Media Commands

| Command | Description | Example Usage |
| :--- | :--- | :--- |
| `!add_audio` | Add an audio file (attachment) to a video or image (attachment). | `!add_audio` (attach both files) |
| `!resize` | Resize an attached image to specified dimensions. | `!resize 500 300` (resizes to 500px wide, 300px tall) |
| `!reverse_video` | Reverse an attached video. | `!reverse_video` (attach the video) |
| `!to_gif` | Convert an attached media file (video or image sequence) to a GIF. | `!to_gif` (attach the media) |
| `!download` | Download media from a given URL (YouTube, Reddit, Twitter, etc.). | `!download [url]` |

### 🧠 Gemini AI

| Command | Description | Example Usage |
| :--- | :--- | :--- |
| `!gemini` | Ask a question or give a prompt to the Gemini API. | `!gemini write a short poem about a robot` |

### 💰 Currency System

| Command | Description | Example Usage |
| :--- | :--- | :--- |
| `!balance` | Check your current currency balance. | `!balance` |
| `!daily` | Claim your daily currency reward. | `!daily` |
| `!leaderboard` | See the top currency earners on the server. | `!leaderboard` |

### 🎮 Games

| Command | Description | Example Usage |
| :--- | :--- | :--- |
| `!tictactoe @user` | Start a Tic-Tac-Toe game with a mentioned user. | `!tictactoe @JaneDoe` |
| `!rps [choice]` | Play Rock Paper Scissors against the bot. | `!rps rock` |
| `!coinflip` | Flip a coin (Heads or Tails). | `!coinflip` |
| `!8ball [question]` | Ask the 8-Ball a question. | `!8ball will the sun shine tomorrow?` |

-----

## 🛠️ Setup and Installation

**(For Developers/Self-Hosters)**

1.  **Clone the repository:**

    ```bash
    git clone [your-repo-link]
    cd MediaForge-Bot
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Configuration:**

      * Rename `config_example.py` to **`config.py`**.
      * Fill in your **Discord Bot Token** and **Gemini API Key** in `config.py`.
      * *Note: Media processing requires external tools like **FFmpeg** to be installed on the system path.*

4.  **Run the bot:**

    ```bash
    python bot.py
    ```

-----

## 🤝 Support and Contributions

If you find a bug or have a suggestion, please feel free to open an **issue** or submit a **pull request**\!
