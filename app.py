import streamlit as st
import json
import pandas as pd
from datetime import datetime
import urllib.parse

# File to store events
EVENTS_FILE = 'events.json'

# Load events from JSON file
def load_events():
    try:
        with open(EVENTS_FILE, 'r') as file:
            events = json.load(file)
    except FileNotFoundError:
        events = []
    return events

# Save events to JSON file
def save_events(events):
    with open(EVENTS_FILE, 'w') as file:
        json.dump(events, file, indent=4)

# Generate WhatsApp link
def get_whatsapp_link(event):
    message = f"Event: {event['title']}\nDate: {event['date']}\nZoom Link: {event['zoom_link']}"
    encoded_message = urllib.parse.quote(message)
    whatsapp_url = f"https://wa.me/?text={encoded_message}"
    return whatsapp_url

# Display events in a table with deletion and sharing options
def display_events(events):
    st.header("Event Calendar")
    if events:
        # Ensure all events have the 'zoom_link' key
        for event in events:
            if 'zoom_link' not in event:
                event['zoom_link'] = ""
        # Convert events to DataFrame for better table display
        df = pd.DataFrame(events)
        
        # Handle date-time parsing with mixed formats
        def parse_date(date_str):
            try:
                return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                return datetime.strptime(date_str, '%Y-%m-%d')

        df['date'] = df['date'].apply(parse_date)
        df['date'] = df['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
        
        # Add a selection column for deletion
        df['delete'] = False
        
        # Display the DataFrame with checkboxes and sharing options
        for i in range(len(df)):
            cols = st.columns((1, 1, 2, 1, 1))
            cols[0].write(df.at[i, 'title'])
            cols[1].write(df.at[i, 'date'])
            cols[2].write(f'<a href="{df.at[i, "zoom_link"]}" target="_blank">Join Meeting</a>', unsafe_allow_html=True)
            df.at[i, 'delete'] = cols[3].checkbox("Delete", key=f"delete_{i}")

            # WhatsApp link generation
            if cols[4].button("WhatsApp", key=f"whatsapp_{i}"):
                whatsapp_url = get_whatsapp_link(events[i])
                st.write(f"WhatsApp link: [Click here to send via WhatsApp]({whatsapp_url})")
                
        # Delete selected events
        if st.button("Delete Selected Events"):
            df = df[~df['delete']]
            events = df.drop(columns=['delete']).to_dict('records')
            save_events(events)
            st.success("Selected events deleted successfully!")
            st.experimental_rerun()
    else:
        st.write("No events available.")

# Add a new event
def add_event():
    st.sidebar.header("Add New Event")
    title = st.sidebar.text_input("Event Title")
    date = st.sidebar.date_input("Event Date")
    time = st.sidebar.time_input("Event Time")
    zoom_link = st.sidebar.text_input("Meeting Link if any")
    if st.sidebar.button("Add Event"):
        events = load_events()
        event_datetime = datetime.combine(date, time)
        events.append({"title": title, "date": event_datetime.strftime('%Y-%m-%d %H:%M:%S'), "zoom_link": zoom_link})
        save_events(events)
        st.sidebar.success("Event Added")
        st.experimental_rerun()

# Main function
def main():
    st.title("JSON Event-Based Calendar with Streamlit")
    events = load_events()
    display_events(events)
    add_event()

if __name__ == "__main__":
    main()
