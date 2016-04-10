# AAR 2015-2016 - From Text to Information
Messing around with NLP for high school research program during 2015-2016 school year. Experimenting with a lot of interesting libraries, algorithms, techniques, and ideas.

Project by [Gautam Mittal](http://www.gautam.cc).
Mentor: [Robert Cheung](https://www.linkedin.com/in/robertkcheung)

### Installation
Clone the project on your local machine:
```shell
$ git clone https://github.com/gmittal/aar-nlp-research-2016
```

In the root of the project, create a ```.env``` file and populate it with the following information:
```
BING_SEARCH_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```
You can obtain a Bing Search API key [here](http://www.bing.com/toolbox/bingsearchapi).

Create a new Python 2.7 virtual environment and activate it:
```shell
$ virtualenv venv
$ source venv/bin/activate
```

Install all of the dependencies:
```shell
$ pip install -r requirements.txt
```

Finally, run the webserver:
```shell
$ python app.py
```

This will start the Flask server, but it will only be internally accessible from your machine. If you want to allow remote source to externally connect to your server, you'll have to open a localhost tunnel via [```ngrok```](https://ngrok.com/).
```shell
$ ngrok http 5000
```



### License ([TL;DR](https://tldrlegal.com/license/mit-license))
The MIT License (MIT)

Copyright (c) 2016 Gautam Mittal

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
