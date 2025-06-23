# E-commerce Data Collection and Analytics

This project implements AI-powered agents for e-commerce data collection and analytics, using local Ollama models for intelligent scraping, Firebase for storage, and a data warehouse for analytics.

## Project Structure

```
src/
├── agents/           # AI agents for web scraping
├── database/        # Firebase integration
└── warehouse/       # Data warehouse and analytics
```

## Requirements

- Python 3.9+
- Firebase account and credentials
- Ollama installed locally
- Required Python packages (see requirements.txt)

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
Create a `.env` file with:
```
FIREBASE_CREDENTIALS_PATH=path/to/your/credentials.json
COUNTRY_CODE=BR  # Target country code
```

3. Install Ollama (if not already installed):
Visit https://ollama.ai for installation instructions

## Usage

1. Start the data collection:
```bash
python src/main.py collect
```

2. Run the ETL process:
```bash
python src/main.py etl
```

3. Launch the dashboard:
```bash
python src/main.py dashboard
```

## Components

### AI Agents
- Uses Ollama for local AI processing
- Intelligent product data extraction
- Automatic category classification

### Database
- Firebase Realtime Database integration
- Structured product data storage
- Real-time updates

### Data Warehouse
- ETL processes for data transformation
- Analytics-ready data structures
- Efficient querying capabilities

### Dashboard
- Interactive data visualization
- Product insights
- Market analysis

## Contributing

1. Fork the repository
2. Create your feature branch
3. Submit a pull request

## License

This project is licensed under the MIT License.
