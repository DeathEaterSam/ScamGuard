
import os
import tempfile
import whisper

def transcribe_audio(file_stream):
    # Create a temporary file to store the uploaded file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
        # Write the uploaded file's content to the temporary file
        tmp_file.write(file_stream.getvalue())
        tmp_file_path = tmp_file.name

    # Load the Whisper model
    model = whisper.load_model("base")

    # Transcribe the audio using the temporary file path
    result = model.transcribe(tmp_file_path)

    # Clean up the temporary file
    os.remove(tmp_file_path)

    # Extract the transcription text
    transcription = result["text"]
    return transcription

