<h1 align="center">
  <br>
  <a href="https://vantage6.ai"><img src="https://github.com/IKNL/guidelines/blob/master/resources/logos/vantage6.png?raw=true" alt="vantage6" width="400"></a>
</h1>

<h3 align=center> A privacy preserving federated learning solution</h3>

--------------------

# v6_boilerplate_py
This algoithm is part of the [vantage6](https://vantage6.ai) solution. Vantage6 allowes to execute computations on federated datasets. This repository provides a boilerplate for new algorithms based on GraphDB (SPARQL) databases.

## Setup
First clone the repository.
```bash
# Clone this repository
git clone https://github.com/jaspersnel/v6-boilerplate-py
```

Rename the contained v6_boilerplate_rdf_py directory to something that fits your algorithm. Then you can edit the following files:

### Dockerfile
Update the `ARG PKG_NAME=...` to the name of your algorithm (preferable the same as the directory name).

### LICENCE
Determine which license suits your project.

### setup.py
In order for the Docker image to find the methods the algorithm needs to be installable. Make sure the *PACKAGE_NAME* variable matches the `ARG PKG_NAME` in the Dockerfile. This is also where any additional packages can be specified for installing into the image that will be produced.

## Development
The actual algorithms are written in `{algorithm_name}/methods.py`. Beforehand, it is useful to install the necessary vantage6 packages (including pandas, which is used in the example here and is likely to appear in most algorithms):

```bash
# (OPTIONAL) set up a virtual environment and activate it
python3 -m venv venv
source venv/bin/activate

# Install the requirements
pip install -r requirements.txt
```

### {algorithm_name}/query.sparql
Contains the SPARQL query sent to the graph database to retrieve data. The data queried here is then stored in a pandas dataframe with matching column names (and datatypes, if properly indicated in the graph data).

### {algorithm_name}/methods.py
Contains all the methods that can be called at the nodes. All __regular__ definitions in this file that have the prefix `RPC_` are callable by an external party. If you define a __master__ method, it should *not* contain the prefix! The __master__ and __regular__ definitions both have their own signature. __Master__ definitions have a __client__ and __data__ argument (and possible some other arguments), while the __regular__ definition only has the __data__ argument. The data argument is a [pandas dataframe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html?highlight=dataframe#pandas.DataFrame) and the client argument is a `ClientContainerProtocol` or `ClientMockProtocol` from the [vantage6-toolkit](https://github.com/IKNL/vantage6-toolkit). Examples of the __master__ and __regular__ methods are provided in the `methods.py` file, their signatures should look like this:

```python
def some_master_name(client, data, *args, **kwargs):
    # do something
    pass

def RPC_some_regular_method(data, *args, **kwargs):
    # do something
    pass
```

### Testing
As the data for algorithms based on this boilerplate code are to come from a graph database, testing can (currently) only be done on a live vantage6 infrastructure with a graph database attached. Currently, a number of problems around this are present in the vantage6 ecosystem. Currently, the easiest way to set up an infrastructure is by setting up a local server and node following the vantage6 documentation. Then start a docker container for a graph database, and connect it to the node's docker network:

```bash
docker connect vantage6-{nodename}-user-net {graphdb-docker-name}
```

## Publishing for real-world use

### Building the image
If everything has been entered correctly in the setup stage, you should only have to build the image and push it to docker hub to be able to use it:

```bash
docker build -t your_username/algorithm_name .
docker push your_username/algorithm_name
```

### Running the train
At this stage much will depend on how the infrastructure has been set up - the correct URLs have to be entered and login details need to be correct. As an example, the `run.py` file has been provided.

## Read more
See the [documentation](https://docs.vantage6.ai/) for detailed instructions on how to install and use the server and nodes.

------------------------------------
> [vantage6](https://vantage6.ai)