# Dash-Skellington

## Overview
Dash-Skellington is a skeleton project for the Dash framework,
designed to serve as a foundational template for creating customizable
Dash applications. Dash, built on the MVC (Model-View-Controller)
design framework, benefits from this project's structured approach,
offering best-practice conventions suitable for both advanced and
beginner users. While the code may seem extensive relative to the data
and analysis complexity, it serves an illustrative purpose,
demonstrating how to build reliable and scalable Dash
applications. This skeleton project is intended to be extended and
adapted to fit the specific data and functional needs of your
application.

## Getting Started

### Setting Up the Environment

1. **Create a Virtual Environment**
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```
   
2. **Install Requirements** 
   ```bash 
   pip install -r requirements.txt
   ```
   
3. **Run the Application**
   ```bash
   cd app
   python3 index.py
   ```

## Key Components

### app.py
- Core Dash module using `dash.Dash()` with Flask.
- Adjusted default parameters for optimal setup.
- Configuration details are separated for ease of use and replication in `config.py`.

### config.py
- Utilizes `types.SimpleNamespace` for storing configuration constants.
- Ideal for multi-page apps with `suppress_callback_exceptions=True`.

## index.py
The `index` module serves as the central hub for routing and
displaying content in the Dash-Skellington application. It is
responsible for defining the app's layout and handling URL routing to
render different pages based on the user's navigation.

## Page Directory Structure
The `page` directory in Dash-Skellington adopts a modular
architecture, where each page of the application is organized into its
own directory. 

- This structure can be easily scaled up or down based on the
  complexity of each page.

- It allows for the addition of more pages with their specific MVC
  components, facilitating the expansion of the application.

Each of these directories contains three key files:
- `model.py`: Handles data manipulation and business logic.
- `controller.py`: Manages the logic and user interactions for the page.
- `view.py`: Defines the layout and visual presentation of the page.

### Directory Layout
```plaintext
page
├── home
│   ├── controller.py
│   ├── model.py
│   └── view.py
├── movies
│   ├── controller.py
│   ├── model.py
│   └── view.py
└── not_found
    └── view.py
```

# Credits and Inspiration

I would like extend our thanks to the individuals and resources that
have inspired and contributed to the development of this
project. Their work in the Dash ecosystem has been invaluable in
shaping my understanding and approach to building reliable Dash
applications.

| Type         | Name                          | URL                                                                                             |
|--------------|-------------------------------|-------------------------------------------------------------------------------------------------|
| Data Source  | Rounak Banik                  | [GitHub](https://github.com/rounakbanik)                                                        |
| Reference    | Plotly Dash                   | [Plotly Dash](https://dash.plotly.com/)                                                         |
| Reference    | Dash Bootstrap Components     | [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)           |
| Reference    | The Book of Dash              | [The Book of Dash](https://nostarch.com/book-dash/)                                             |
| Reference    | A Comprehensive Guide to Building Enterprise-Level Plotly Dash Apps | [Towards Data Science Article](https://towardsdatascience.com/a-comprehensive-guide-to-building-enterprise-level-plotly-dash-apps-bd40dfe1313c) |

## References
- [Dash Documentation](https://dash.plotly.com/reference)
- [Flask API](https://flask.palletsprojects.com/en/3.0.x/api/#application-object)


