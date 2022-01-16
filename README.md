## Data-Parser

### Installation Requirement

```python
1. Python 3.6 or greater (this code is tested with 3.6 and 3.9)
2. Python module present in requirements.txt
```

### How to run

1. Install the necessary dependencies. Use the following command to install the libraries
```python
pip install -r requirements.txt
```

2. Run the main file. Please go through `help` to know about argument
```python
python main.py -h
```

Provide the arguments and run to get the result
```python
python .\main.py --csvFilePath .\stock_data.csv --sort asc --stockName EFX --startDate 2013-02-01 --endDate 2013-02-11
```