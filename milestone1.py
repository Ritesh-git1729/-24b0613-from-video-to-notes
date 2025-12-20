"""
Project: From Video to Notes
Author: Ritesh Srivastava

Milestone 1:
Accept a YouTube video link and simulate conversion to notes.
"""

def video_to_notes(video_link):
    """
    This function simulates converting a YouTube video into text notes.
    Actual audio extraction and NLP will be added in future milestones.
    """
    print("\nProcessing video...")
    print("Extracting audio from:", video_link)
    print("Converting audio to text...")
    print("Formatting text into notes...\n")
    print("Notes generated successfully!")

if __name__ == "__main__":
    link = input("Enter YouTube video link: ")
    video_to_notes(link
