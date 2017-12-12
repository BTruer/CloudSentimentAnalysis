# CloudSentimentAnalysis
Sentiment analysis of entities on the cloud using Twitter data

## Start application
1. `virtualenv venv`
2. `source venv/bin/activate`
3. `pip install -r requirments.txt`
5. add env vars [stackoverflow](https://askubuntu.com/questions/58814/how-do-i-add-environment-variables) add lines to .bashrc
4. `sudo service mongod start`
5. `python3 app.py`
6. requires tensorflow backend
7. requires kerias
8. requires pyspark
8. To use: GET http://127.0.0.1:5000/search?query=apple

Note: the producation environment for the demo does not use caching for ease of reading. 