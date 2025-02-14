import pvporcupine
import pyaudio
import struct

# Load your Porcupine model file
ACCESS_KEY = "pvghMekcTAl9x7qOpNQ94CoIRCilY4m2IzwB++YqlbS13QAomizzAQ=="  # Replace with your actual key
MODEL_PATH = "Catherine_en_windows_v3_0_0.ppn"  # Your wake word model

def detect_wake_word():
    porcupine = pvporcupine.create(
        access_key=ACCESS_KEY,
        keyword_paths=[MODEL_PATH]
    )
    
    pa = pyaudio.PyAudio()
    stream = pa.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=porcupine.sample_rate,
        input=True,
        #input_device_index=None,
        frames_per_buffer=porcupine.frame_length
    )

    print("Listening for 'Catherine'...")
    
    while True:
        pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        if porcupine.process(pcm) >= 0:
            print("Wake word detected!")
            break

    stream.close()
    pa.terminate()
    porcupine.delete()

detect_wake_word()
