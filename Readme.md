# Sentimentenal Analysis API :relaxed:

## Demo

![Demo](asset/demo.gif)


## Test Live
[Link](https://api-sentimental-analysis-service.onrender.com/)


## Setup:

### Follow the steps


### Requirements 
* Python

## Setting up with Python ### 

**Clone Repo**
```
git clone https://github.com/Arnold-git/Sentiment-Analysis-Api
```

**Set Path to sentimental_analysis_api directory**
```
cd sentimenatal_analysis_api
```

**Create a virtual environment**
```
python -m venv .venv

or

First install virtualenv by running command

pip install virtualenv
then

virtualenv venv
```

**Activate virutual Environment**
```
#windows
source .venv/Scripts/activate

#linux
source .venv/bin/activate
```

**Install dependencies for project**
```
pip install -r app/requirements.txt
```

**Start Server**

```
uvicorn main:app --reload
```

