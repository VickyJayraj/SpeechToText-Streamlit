from main import mic_index
import streamlit as st
import speech_recognition as sr

def recognize_speech():
    # Initialize recognizer
    r = sr.Recognizer()
    
    # Create a placeholder for status updates
    status_text = st.empty()
    
    try:
        # Use the default microphone
        with sr.Microphone(mic_index=0) as source:
            status_text.info("Adjusting for ambient noise... Please wait.")
            r.adjust_for_ambient_noise(source, duration=0.2)
            
            status_text.info("Listening... Speak now!")
            # Listen for audio
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            
            status_text.info("Processing audio...")
            
            # Recognize speech using Google Speech Recognition
            text = r.recognize_google(audio)
            return text, None
            
    except sr.WaitTimeoutError:
        return None, "Listening timed out. No speech detected."
    except sr.UnknownValueError:
        return None, "Could not understand audio."
    except sr.RequestError as e:
        return None, f"Could not request results; {e}"
    except Exception as e:
        return None, f"An error occurred: {e}"
    finally:
        status_text.empty()

def main():
    st.set_page_config(page_title="Speech to Text App", page_icon="🎙️")
    
    st.title("🎙️ Speech to Text Converter")
    st.write("Click the button below and speak to convert your speech to text.")
    
    if st.button("Start Recording", type="primary"):
        with st.spinner("Listening..."):
            text, error = recognize_speech()
            
        if error:
            st.error(error)
        elif text:
            st.success("Recognition Successful!")
            st.markdown("### You said:")
            st.info(text)

if __name__ == "__main__":
    main()
