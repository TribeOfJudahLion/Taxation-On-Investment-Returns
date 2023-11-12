<br/>
<p align="center">
  <h3 align="center">Maximize Your Wealth: Navigating the Maze of Taxation on Investment Returns</h3>

  <p align="center">
    Empower Your Investments - Decode Tax, Amplify Gains!
    <br/>
    <br/>
  </p>
</p>



## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

**Background**: Investors often struggle to understand the real returns on their investments after accounting for taxes. Taxes can significantly impact the final value of an investment, but calculating these impacts can be complex, especially when considering both capital gains and dividends, each potentially taxed at different rates.

**Challenge**: Develop a tool that can calculate the after-tax return of an investment over a specific period, considering the following factors:
- The initial amount invested.
- The annual rate of return on the investment.
- Annual dividend yield.
- The duration of the investment.
- The tax rate on capital gains.
- The tax rate on dividends.
- Whether taxes on gains are applied annually or only at the end of the investment period.

The tool should provide a detailed breakdown of the final investment value after taxes, including the portion from dividends.

### Solution

**Approach**: Create a Python program with two functions: `after_tax_return` and `format_output`.

1. **`after_tax_return` Function**:
   - **Purpose**: To calculate the total after-tax value of an investment, considering capital gains and dividends.
   - **Parameters**:
     - `initial_investment`: The principal amount put into the investment.
     - `annual_return_rate`: The yearly percentage gain from the investment.
     - `annual_dividend_yield`: The yearly dividend payout as a percentage of the investment value.
     - `duration_years`: How long the investment is held.
     - `capital_gains_tax_rate`: The percentage of tax applied to profits from the investment.
     - `dividend_tax_rate`: The percentage of tax applied to dividends.
     - `tax_annually`: A flag indicating if taxes are applied each year or just at the end.
   - **Logic**:
     - The function iterates over each year of the investment, calculating annual gains and dividends, and applying taxes accordingly.
     - Accumulates the total value of dividends after tax.
     - Applies capital gains tax at the end if taxes are not assessed annually.
   - **Output**: Returns the final value of the investment and the total dividends after tax.

2. **`format_output` Function**:
   - **Purpose**: To format the results from `after_tax_return` into a professional and readable format.
   - **Parameters**:
     - `initial_investment`: The initial amount invested.
     - `final_value`: The value of the investment after taxes.
     - `total_dividends`: The total dividends received after taxes.
     - `duration_years`: The investment duration.
   - **Logic**: Constructs a formatted string that includes the duration, initial investment, final value after taxes, and the total dividends after taxes.
   - **Output**: A string that presents the investment outcome in a clear and professional manner.

**Example Usage**:
- An initial investment of $10,000, with a 7% annual return rate, a 2% annual dividend yield, held for 5 years.
- Capital gains and dividend tax rates are both set at 15%, and taxes are applied at the end of the investment period.
- The program calculates and displays the final investment value and total dividends after taxes.

**Output Explanation**:
- The output provides a clear view of the investment's performance over the 5-year period, detailing the final value after tax and the contribution of dividends to the overall return. This information is crucial for investors to understand the true effectiveness of their investment strategies.



## Built With

This investment return calculator is a concise yet powerful tool designed to provide insights into the after-tax returns of investments. It's built using Python, a versatile and widely-used programming language known for its readability and efficiency. Below are the key components and technologies used in the development of this project:

- **Python**: The core programming language used for the development of the tool. Python's vast ecosystem and straightforward syntax make it an ideal choice for financial calculations and modeling.
  - **Version**: [Python 3.x](https://www.python.org/downloads/) (It is recommended to use the latest version of Python 3 for optimal performance and compatibility).

- **Python Standard Library**: This project exclusively utilizes Python's built-in libraries, ensuring that it's lightweight and has no dependencies on external packages. Key features such as string formatting, mathematical operations, and looping constructs are leveraged from the standard library.

- **Development Environment**: While this tool is environment-agnostic, it has been developed and tested using popular IDEs such as [PyCharm](https://www.jetbrains.com/pycharm/) and [Visual Studio Code](https://code.visualstudio.com/). These environments provide excellent support for Python development, including syntax highlighting, code completion, and debugging tools.

- **Source Control**: Managed using [Git](https://git-scm.com/), with the repository hosted on [GitHub](https://github.com/). This ensures robust version control and collaboration features, making it easier to track changes, manage updates, and collaborate with other developers.

- **Documentation and Formatting**: Inline documentation is provided within the code for clarity and ease of understanding. Python's docstring conventions are followed, making it straightforward to generate documentation using tools like [Sphinx](https://www.sphinx-doc.org/en/master/) or [pydoc](https://docs.python.org/3/library/pydoc.html).

- **Testing**: Simple manual testing has been performed to validate the functionality. For more extensive testing and to ensure accuracy in various scenarios, the integration of a testing framework like [pytest](https://docs.pytest.org/en/stable/) or [unittest](https://docs.python.org/3/library/unittest.html) is recommended.

---

### Note to Collaborators and Users

This tool is designed to be a starting point for investment return analysis. It can be expanded with additional features like varying tax structures, more complex investment scenarios, or integration with financial data APIs. Contributions, bug reports, and suggestions for improvements are always welcome. Please refer to the [CONTRIBUTING.md](https://github.com/YOUR-REPOSITORY-URL/CONTRIBUTING.md) file for guidelines on contributing to this project.

Remember, this calculator provides an estimation and should not be used as the sole tool for making investment decisions. Always consult with a financial professional for detailed investment advice.

---

[Back to Top](#built-with)Here are a few examples.

## Getting Started

This section guides you through setting up and using the Investment Return Calculator, a Python tool designed to estimate the after-tax returns on investments considering capital gains and dividends.

---

## Prerequisites

Before you begin, ensure you have the following installed:

1. **Python**: The project is developed in Python, so you need to have Python installed on your machine. It's recommended to use Python 3.x. You can download it from [here](https://www.python.org/downloads/).
   
2. **Git** (optional): If you wish to clone the repository, you need Git installed. However, you can also download the project directly from GitHub. Git can be downloaded from [here](https://git-scm.com/downloads).

---

## Installation

1. **Clone/Download the Repository**:
   - If using Git: 
     ```
     git clone https://github.com/YOUR-REPOSITORY-URL.git
     ```
   - Alternatively, download the ZIP file of the project from GitHub and extract it.

2. **Navigate to the Project Directory**:
   - Open your terminal (or command prompt) and navigate to the directory where you have cloned or downloaded the project.

---

## Usage

1. **Understanding the Code**:
   - The `after_tax_return` function is the core of this project. It takes parameters like initial investment, annual return rate, annual dividend yield, investment duration, and tax rates to calculate the after-tax return of an investment.
   - The `format_output` function is used to format and display the results in a readable manner.

2. **Running the Script**:
   - You can run the script using a Python interpreter. If you're using an IDE like PyCharm or Visual Studio Code, they come with built-in options to run Python scripts.
   - Alternatively, you can run the script from the command line:
     ```
     python path/to/your/script.py
     ```

3. **Modifying Parameters**:
   - Open the script in a text editor or IDE.
   - You will find the 'Example usage' section at the bottom of the script. Modify the parameters like `initial_investment`, `annual_return_rate`, etc., according to your needs.

4. **Viewing the Results**:
   - After running the script with your parameters, the results will be displayed in the console. It will show you the final value of the investment after the specified duration, accounting for taxes on both capital gains and dividends.

---

## Contributing

If you're interested in contributing to this project, your input is welcome. Whether you're fixing bugs, improving the documentation, or suggesting new features, your contribution is appreciated. Please refer to the [CONTRIBUTING.md](https://github.com/YOUR-REPOSITORY-URL/CONTRIBUTING.md) file for guidelines on how to contribute.

---

## Support

For support, please open an issue in the GitHub issue tracker or contact the repository maintainers.

[Back to Top](#getting-started)

---

Remember, this tool is a model and should not be used as the sole basis for any financial decisions. Always consult with a financial professional for such matters.

## Roadmap

See the [open issues](https://github.com//Taxation-On-Investment-Returns/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com//Taxation-On-Investment-Returns/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com//Taxation-On-Investment-Returns/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com//Taxation-On-Investment-Returns/blob/main/LICENSE.md) for more information.

## Authors

* **Robbie** - *PhD Computer Science Student* - [Robbie](https://github.com/TribeOfJudahLion/) - **

## Acknowledgements

* []()
* []()
* []()
