# AI Trading Strategies

A comprehensive portfolio of data analysis and machine learning projects focused on financial markets, featuring both data engineering pipelines and advanced investment strategy evaluation. This project demonstrates practical applications of quantitative finance, risk management, and portfolio optimization techniques.

## 🎯 Project Overview

This repository contains two main components that work together to provide a complete framework for AI-driven trading strategy development:

### 1. Data Transformation for Trading Models
A robust data engineering pipeline that processes macroeconomic indicators and stock market data to create clean, analysis-ready datasets for machine learning models.

### 2. Dynamic Investment Strategy Evaluation
An advanced risk-parity portfolio analysis system that implements and backtests sophisticated investment strategies using real-time financial data.

## 📁 Project Structure

```
AI-Trading-Strategies/
├── 1 Data Transformation for Trading Models/
│   ├── README.md                                    # Component documentation
│   ├── Preparing-for-data-analysis-project-student.ipynb  # Main data pipeline
│   ├── apple_historical_data.csv                    # Apple stock price data
│   ├── microsoft_historical_data.csv                # Microsoft stock price data
│   ├── GDP.csv                                      # Gross Domestic Product data
│   ├── inflation_monthly.csv                        # Monthly inflation data
│   ├── consumer_price_index.csv                     # Consumer Price Index data
│   ├── Apple&Microsoft.csv                          # Combined stock data
│   ├── Applepp.csv                                  # Processed Apple data
│   ├── Microsoftpp.csv                              # Processed Microsoft data
│   ├── GDPpp.csv                                    # Processed GDP data
│   ├── Inflationpp.csv                              # Processed inflation data
│   ├── InflationQ.csv                               # Quarterly inflation data
│   ├── InflationW.csv                               # Weekly inflation data
│   └── Applel3m.csv                                # Apple 3-month data
│
└── 2 Evaluating and Backtesting a Dynamic Investment Strategy/
    └── Evaluating and Backtesting a Dynamic Investment Strategy.ipynb  # Risk-parity analysis
```

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- Jupyter Notebook or JupyterLab
- Git (for cloning the repository)
- Internet connection (for downloading financial data)

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
conda install pandas matplotlib seaborn jupyter numpy yfinance
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
pip install pandas matplotlib seaborn jupyter numpy yfinance
```

### Step 3: Launch Jupyter Notebook

```bash
# Launch Jupyter Notebook
jupyter notebook
```

## 📊 Component 1: Data Transformation for Trading Models

### Purpose
This component focuses on building robust data engineering pipelines for financial analysis, specifically designed to:

- **Process macroeconomic indicators** (GDP, inflation, consumer price index) and analyze their correlation with stock market performance
- **Clean and prepare historical stock data** for Apple and Microsoft to identify patterns and trends
- **Demonstrate data engineering best practices** including data ingestion, cleaning, imputation, and exploratory data analysis
- **Create analysis-ready datasets** for machine learning model development

### Key Features
- **Data Ingestion**: Automated loading of multiple CSV files from various sources
- **Data Cleaning**: Handling missing values, data type conversions, and format standardization
- **Data Imputation**: Advanced techniques for filling missing economic indicators
- **Exploratory Data Analysis**: Comprehensive visualization and statistical analysis
- **Time Series Analysis**: Examination of stock price trends and economic indicator patterns

### Usage
1. Navigate to the `1 Data Transformation for Trading Models/` directory
2. Open `Preparing-for-data-analysis-project-student.ipynb`
3. Run cells sequentially to execute the data analysis pipeline

## 📈 Component 2: Dynamic Investment Strategy Evaluation

### Purpose
This component implements and evaluates advanced investment strategies, specifically:

- **Risk-Parity Portfolio Analysis**: Equalizes risk contribution across different asset classes
- **Real-time Data Processing**: Downloads and processes live financial data using Yahoo Finance
- **Performance Evaluation**: Comprehensive backtesting with key financial metrics
- **Portfolio Optimization**: Dynamic weight allocation based on risk characteristics

### Key Features
- **Multi-Asset Portfolio**: Analyzes S&P500 futures, 10-year Treasuries, gold, and US dollar
- **Risk-Parity Implementation**: Sophisticated portfolio allocation strategy
- **Performance Metrics**: Annualized return, volatility, Sharpe ratio calculations
- **Dynamic Rebalancing**: Monthly portfolio rebalancing based on risk characteristics
- **Visualization**: Comprehensive charts and graphs for strategy analysis

### Data Sources
- **S&P500 Futures (ES=F)**: Equity market exposure
- **10-Year Treasury Futures (ZN=F)**: Fixed income exposure
- **Gold Futures (GC=F)**: Commodity exposure
- **US Dollar Index Futures (DX=F)**: Currency exposure

### Usage
1. Navigate to the `2 Evaluating and Backtesting a Dynamic Investment Strategy/` directory
2. Open `Evaluating and Backtesting a Dynamic Investment Strategy.ipynb`
3. Execute cells to download data and perform risk-parity analysis

## 🛠️ Technologies Used

### Core Libraries
- **Python**: Primary programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib & Seaborn**: Data visualization
- **Jupyter Notebook**: Interactive development environment

### Financial Libraries
- **yfinance**: Real-time financial data download
- **Financial calculations**: Custom implementations for portfolio metrics

## 📋 Getting Started

### For Beginners
1. Start with **Component 1** to understand data engineering fundamentals
2. Learn about data cleaning, visualization, and basic financial analysis
3. Progress to **Component 2** for advanced portfolio strategies

### For Advanced Users
1. Jump directly to **Component 2** for sophisticated investment strategy evaluation
2. Modify parameters and add new assets to test different strategies
3. Extend the framework with additional risk metrics and optimization techniques

## 🔧 Customization

### Adding New Assets
In the risk-parity notebook, you can easily add new assets by:
1. Adding symbols to the `symbols` list
2. The system will automatically download and process new data
3. Portfolio weights will be recalculated to include new assets

### Modifying Parameters
- **Rolling Window**: Adjust the time period for risk calculations
- **Rebalancing Frequency**: Change from monthly to weekly or quarterly
- **Risk Metrics**: Implement additional risk measures (VaR, CVaR, etc.)

## 📊 Performance Metrics

The project calculates and tracks:
- **Annualized Return**: Total portfolio performance over time
- **Volatility**: Standard deviation of returns
- **Sharpe Ratio**: Risk-adjusted return measure
- **Maximum Drawdown**: Largest peak-to-trough decline
- **Risk Contribution**: Individual asset risk allocation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Data sources provided by Yahoo Finance API
- Economic indicators from public financial databases
- Risk-parity methodology based on academic research
- Educational framework inspired by quantitative finance courses

## 📞 Contact

For questions or support, please open an issue in the GitHub repository or contact the project maintainers.

---

**⚠️ Important Disclaimer**: This project is for educational and research purposes only. Always conduct thorough analysis and consider risk management before implementing any trading strategies in real markets. Past performance does not guarantee future results, and all investments carry inherent risks. 