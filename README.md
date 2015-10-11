# highlight


## to do list

* ~~capture url~~
* ~~make api call~~
* NLP daemon process
* feedback screen from plugin
* login
* persist saved url state
* change icon color based on url index

### browser extension features

* display all matches on browser extension html, ask user to pick the relevent event, also use it to obtain feedback
* google analytics?

### extraction features

modularize components for our event NLP pipeline

* fetch (scrape)
* cleanse
* parse
* extract
* structure

each component should be a pluggable module, where each component can be individually swapped out, maybe a micro-service at some point.

* secondary crawl, detect links and scrape those lines

### feature generation

need to be able to extract features and sample labels

* graph event -> location -> people, basically, if you like food event, or celebrity chef xxx, you'll like this

### application feature

* api for site to
