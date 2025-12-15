# AI Trading Strategies

A comprehensive data analysis and machine learning pipeline project focused on exploring the relationship between macroeconomic indicators and stock market performance. This project demonstrates data engineering best practices for financial analysis and trading strategy development.

## 🎯 Project Purpose

This project serves as a practical implementation of data engineering pipelines for financial analysis, specifically designed to:

- **Analyze macroeconomic indicators** (GDP, inflation, consumer price index) and their correlation with stock market performance
- **Process historical stock data** for Apple and Microsoft to identify patterns and trends
- **Demonstrate data engineering best practices** including data ingestion, cleaning, imputation, and exploratory data analysis
- **Build a foundation for trading strategy development** by establishing robust data pipelines

## 📁 Project Structure

```
AI-Trading-Strategies/
└── Data Transformation for Trading Models/
    ├── README.md                                    # Project documentation
    ├── Preparing-for-data-analysis-project-student.ipynb  # Main analysis notebook
    ├── apple_historical_data.csv                    # Apple stock price data
    ├── microsoft_historical_data.csv                # Microsoft stock price data
    ├── GDP.csv                                      # Gross Domestic Product data
    ├── inflation_monthly.csv                        # Monthly inflation data
    ├── consumer_price_index.csv                     # Consumer Price Index data
    ├── Apple&Microsoft.csv                          # Combined stock data
    ├── Applepp.csv                                  # Processed Apple data
    ├── Microsoftpp.csv                              # Processed Microsoft data
    ├── GDPpp.csv                                    # Processed GDP data
    ├── Inflationpp.csv                              # Processed inflation data
    ├── InflationQ.csv                               # Quarterly inflation data
    ├── InflationW.csv                               # Weekly inflation data
    └── Applel3m.csv                                # Apple 3-month data
```

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- Jupyter Notebook or JupyterLab
- Git (for cloning the repository)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Trading-Strategies.git
cd AI-Trading-Strategies
```

### Step 2: Set Up Python Environment

#### Option A: Using Conda (Recommended)

```bash
# Create a new conda environment
conda create -n ai-trading python=3.9

# Activate the environment
conda activate ai-trading

# Install required packages
conda install pandas matplotlib seaborn jupyter numpy
```

#### Option B: Using pip

```bash
# Create a virtual environment
python -m venv ai-trading-env

# Activate the virtual environment
# On macOS/Linux:
source ai-trading-env/bin/activate
# On Windows:
# ai-trading-env\Scripts\activate

# Install required packages
pip install pandas matplotlib seaborn jupyter numpy
```

### Step 3: Launch Jupyter Notebook

```bash
# Navigate to the project directory
cd "Data Transformation for Trading Models"

# Launch Jupyter Notebook
jupyter notebook
```

### Step 4: Open the Analysis Notebook

1. In the Jupyter interface, click on `Preparing-for-data-analysis-project-student.ipynb`
2. Run the cells sequentially to execute the data analysis pipeline

## 📊 Data Sources

The project utilizes the following datasets:

- **Stock Data**: Historical price data for Apple (AAPL) and Microsoft (MSFT)
- **Economic Indicators**: 
  - Gross Domestic Product (GDP) data
  - Monthly inflation rates
  - Consumer Price Index (CPI)
- **Processed Data**: Various preprocessed datasets for different time frequencies

## 🔧 Key Features

### Data Engineering Pipeline
- **Data Ingestion**: Automated loading of multiple CSV files from various sources
- **Data Cleaning**: Handling missing values, data type conversions, and format standardization
- **Data Imputation**: Advanced techniques for filling missing economic indicators
- **Exploratory Data Analysis**: Comprehensive visualization and statistical analysis

### Analysis Capabilities
- **Time Series Analysis**: Examination of stock price trends and economic indicator patterns
- **Correlation Analysis**: Understanding relationships between macroeconomic factors and stock performance
- **Data Visualization**: Interactive charts and graphs for pattern identification
- **Feature Engineering**: Creation of derived features for machine learning models

## 🛠️ Technologies Used

- **Python**: Primary programming language
- **Pandas**: Data manipulation and analysis
- **Matplotlib & Seaborn**: Data visualization
- **Jupyter Notebook**: Interactive development environment
- **NumPy**: Numerical computing

## 📈 Usage

1. **Start with the main notebook**: Open `Preparing-for-data-analysis-project-student.ipynb`
2. **Follow the data pipeline**: Execute cells in order to understand the data engineering process
3. **Explore the visualizations**: Analyze the generated charts and graphs
4. **Modify and extend**: Use the established pipeline for your own trading strategies

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Data sources provided by Udacity's CD13649 course
- Economic indicators from public financial databases
- Stock data from historical market records

## 📞 Contact

For questions or support, please open an issue in the GitHub repository or contact the project maintainers.

---

**Note**: This project is for educational and research purposes. Always conduct thorough analysis and consider risk management before implementing any trading strategies in real markets. 