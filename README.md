# JSON Event-Based Calendar with Streamlit

This is a simple event-based calendar application built with Streamlit, allowing users to manage events stored in a JSON file. Users can add new events, view them in a table format, delete events, and share event details via WhatsApp.

## Features

- **Add Event**: Users can add new events by providing a title, date, time, and an optional Zoom meeting link.
- **View Events**: Events are displayed in a tabular format showing title, date, and a link to join a Zoom meeting (if provided).
- **Delete Events**: Users can select and delete events from the calendar.
- **Share via WhatsApp**: Each event has a button to generate a WhatsApp message with event details for easy sharing.
- **Responsive UI**: The user interface adapts to different screen sizes, making it accessible on various devices.

## Prerequisites

- Python 3.7+
- Streamlit
- pandas
- datetime

Install required packages using pip:

```bash
pip install streamlit pandas
```

## How to Run

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd Event_based_calendar
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. Open your browser and go to `http://localhost:8501` to view the application.

## Usage

- **Adding Events**: Fill out the fields in the sidebar and click "Add Event".
- **Deleting Events**: Check the events you want to delete and click "Delete Selected Events".
- **Sharing via WhatsApp**: Click the "WhatsApp" button next to each event to generate a WhatsApp link.

## File Structure

- `app.py`: Main Streamlit application code.
- `events.json`: JSON file to store events.
- `README.md`: Documentation file.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
