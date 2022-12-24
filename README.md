# Competitor Analysis

In e-commerce understanding your competition is key to sales performance, yet can be an extremely laborious and time-consuming process. As part of this process, we are attempting to understand how to position and place our products within the market and if there are any holes that we can tap for higher profit. In order to achieve this, we must understand and keep track of the competition. Over time and if done well, this can give us major leverage to capture more of the market.

Using ML we can automate the entire process. By finding similar products from competitors we can aim to categorize them and understand competitor’s pricing strategies in order to better position ourselves in the market.

# Demo

https://user-images.githubusercontent.com/63944541/209448463-11b88b4b-4da0-43da-bd12-bd70c97cbc9e.mov

##### The methods for achieving this would be the following:
1. Scrape similar products (e.g. by brand, category, size, color etc.)
2. Assess/score the similarity of the products in terms of e.g.
   - Text description embeddings
   - Image 
   - Price
   - SKU matching
3. Provide insight back to the user on price changes and positioning over time and the direct competitiveness of the products to your own, in order to inform pricing strategies
4. Given a product, the project aims to find similar products from competitors, categorise them and understand competitor’s pricing strategies in order to have a greater competitive advantage.


### Progress:

1. Web Scraped the nike shoes data:

    ![App Screenshot](https://github.com/prathameshparit/Dummy-Storage/blob/a2ee836e440ea5ecc013b09b5bc66d27ba44e891/readme%20images/fellowship/notebook_1.png?raw=true)

2. Built a web application to access nike shoes data
   
    - **Landing Page:**
    ![App Screenshot](https://github.com/prathameshparit/Dummy-Storage/blob/a2ee836e440ea5ecc013b09b5bc66d27ba44e891/readme%20images/fellowship/landing.png?raw=true)
    
    - **Input Data:**
    ![App Screenshot](https://github.com/prathameshparit/Dummy-Storage/blob/a2ee836e440ea5ecc013b09b5bc66d27ba44e891/readme%20images/fellowship/input.png?raw=true)
    
    - **Results:**
    ![App Screenshot](https://github.com/prathameshparit/Dummy-Storage/blob/a2ee836e440ea5ecc013b09b5bc66d27ba44e891/readme%20images/fellowship/results.png?raw=true)



## Tech

The website uses a number of open source projects to work properly:

- [Beautiful Soup] - Beautiful Soup is a Python package for parsing HTML and XML documents.
- [Flask] - Framework for creating web applications in Python easier.
- [Numpy] - Used for working with arrays
- [Pandas] - Used for data analysis and associated manipulation of tabular data in Dataframes

## Installation

Website requires these steps to install the application on your device


On terminal:

Download virtual env library
```sh
pip3 install -U pip virtualenv
```

Create a virtual environment on your device
```sh
virtualenv  -p python3 ./venv
```

Download all the dependencies provided on requirements.txt
```sh
pip install -r .\requirements.txt
```

Activated the virtual environment
```sh
.\venv\Scripts\activate
```

Run app.py after completing all the steps.






   
[Beautiful soup]: <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>
[Scikit-Learn]: <https://scikit-learn.org/stable/>
[Flask]: <https://flask.palletsprojects.com/en/2.1.x/>
[Numpy]: <https://numpy.org/>
[Pandas]: <https://pandas.pydata.org/>


