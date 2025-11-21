# Weather Query & AI Assistant Project

A Python-based weather query application that integrates real-time weather information retrieval and AI-powered assistant functionality. Users can obtain weather information by entering city names and receive AI-provided weather suggestions and Q&A services.

## Features

- 🌤️ **Real-time Weather Query**: Get real-time weather information for specified cities through the wttr.in API
- 🤖 **AI Weather Assistant**: Provides intelligent weather suggestions and Q&A services based on OpenAI API
- 💬 **Interactive Conversation**: Supports multi-turn conversations with the AI assistant to get weather-related advice
- 📍 **Multi-city Support**: Supports querying weather information for any city worldwide

## Project Structure

```
Team_project/
├── main.py          # Main program entry point
├── get_info.py      # Weather information retrieval module
├── AI_info.py       # AI assistant functionality module
└── README.md        # Project documentation
```

## Installation Requirements

### Python Version
- Python 3.7 or higher

### Dependencies

Install the required Python libraries:

```bash
pip install requests openai python-dotenv
```

Or use requirements.txt (if available):

```bash
pip install -r requirements.txt
```

## Configuration

### 1. Get OpenAI API Key

1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Register an account and create an API key
3. Copy your API key

### 2. Configure Environment Variables

Create a `.env` file in the project root directory and add the following content:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

**Note**: Make sure to add the `.env` file to `.gitignore` and do not commit API keys to version control systems.

## Usage

### 1. Run the Program

```bash
python main.py
```

### 2. Usage Flow

1. **Enter City Name**
   - After the program starts, enter the name of the city or location you want to query (supports both English and Chinese)
   - Examples: `Beijing`, `New York`, `Shanghai`

2. **View Weather Information**
   - The program will automatically display the current weather information for that city, including:
     - Weather condition
     - Actual temperature
     - Local time

3. **Get AI Suggestions (Optional)**
   - When asked if you need AI weather suggestions, enter `yes` or `no`
   - If you choose `yes`, the AI assistant will provide suggestions based on the current weather

4. **Chat with AI (Optional)**
   - In AI suggestion mode, you can continue asking any questions about the weather in that area
   - Enter `exit` to exit the conversation

### Usage Example

```
Please input A city or a place: Beijing

Current time: 2024-01-15 14:30 Beijing Information:
Weather condition: Clear
Temperature (Actual): +15°C

Do you need today's BEIJING weather AI suggestion? (yes/no) yes
AI assistant: Today's weather in Beijing is clear with a temperature of 15°C, perfect for outdoor activities...

You can ask any question about the weather in this place....
input "exit" to exit
User: Will it rain tomorrow?
AI assistant: Based on the current weather conditions...
User: exit
```

## Module Description

### main.py
Main program file, responsible for:
- Receiving user input for city names
- Calling weather API to retrieve information
- Managing the interaction flow between users and the AI assistant

### get_info.py
Weather information retrieval module, functions include:
- Calling wttr.in API to get weather data
- Data cleaning and formatting
- Error handling

### AI_info.py
AI assistant functionality module, functions include:
- Connecting to OpenAI API
- Processing user queries and generating AI responses
- Providing friendly weather assistant services

## Important Notes

1. **API Key Security**
   - Please keep your OpenAI API key secure
   - Do not commit the `.env` file containing API keys to public code repositories

2. **Network Connection**
   - The program requires a stable network connection to access the weather API and OpenAI API
   - If API access fails, the program will display corresponding error messages

3. **API Usage Limits**
   - OpenAI API may have rate limits and cost restrictions
   - Please use it reasonably according to your API plan

4. **City Name Format**
   - It is recommended to use English city names for best results
   - Some Chinese city names may not be correctly recognized

## Error Handling

The program includes basic error handling mechanisms:
- Displays error messages when API access fails
- Prompts users to retry when city information cannot be retrieved
- Network timeout is set to 10 seconds

## Future Improvements

- [ ] Add more weather information (humidity, wind speed, atmospheric pressure, etc.)
- [ ] Support weather forecast functionality (weather for the next few days)
- [ ] Add graphical user interface (GUI)
- [ ] Support multi-language city name recognition
- [ ] Add weather historical data query
- [ ] Implement weather data visualization

## License

This project is a course assignment project for learning and research purposes only.

## Contributors

Team Members: [Add team member names here]

## Contact

For questions or suggestions, please contact the project maintainer.

---

**Note**: This project is a team assignment for the "Programming for Data Analysis" course.
