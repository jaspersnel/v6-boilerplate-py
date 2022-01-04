<h1 align="center">
  <br>
  <a href="https://vantage6.ai"><img src="https://github.com/IKNL/guidelines/blob/master/resources/logos/vantage6.png?raw=true" alt="vantage6" width="400"></a>
</h1>

<h3 align=center> A privacy preserving federated learning solution</h3>

--------------------

# v6_boilerplate_py
This algoithm is part of the [vantage6](https://vantage6.ai) solution. Vantage6 allowes to execute computations on federated datasets. This repository provides a boilerplate for new algorithms.

## Setup
First clone the repository.
```bash
# Clone this repository
git clone https://github.com/jaspersnel/v6-boilerplate-py
```

Rename the contained v6_boilerplate_py directory to something that fits your algorithm, we use the convention `v6_{name}_{langauge}`. Then you can edit the following files:

### Dockerfile
Update the `ARG PKG_NAME=...` to the name of your algorithm (preferable the same as the directory name).

### LICENCE
Determine which license suits your project.

### setup.py
In order for the Docker image to find the methods the algorithm needs to be installable. Make sure the *name* matches the `ARG PKG_NAME` in the Dockerfile. This is also where any additional packages can be specified for installing into the image that will be produced.

## Development
The actual algorithms are written in `{algorithm_name}/methods.py`. Beforehand, it is useful to install the necessary vantage6 packages (including pandas, which is used in the example here and is likely to appear in most algorithms):

```bash
# (OPTIONAL) set up a virtual environment and activate it
python3 -m venv venv
source venv/bin/activate

# Install the requirements
pip install -r requirements.txt
```

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
After writing a new algorithm, it is useful to test it. The `test.py` script has been provided to do this. Simply edit line 3 in this file to point to two different CSV files and change the algorithm name. This will serve as a preliminary test for the algorithm.

```bash
python test.py
```

## Publishing for real-world use

### Building the image
If everything has been entered correctly in the setup stage, you should only have to build the image and push it to docker hub to be able to use it:

```bash
docker build -t your_username/algorithm_name .
docker push your_username/algorithm_name
```

### Running the train
At this stage much will depend on how the infrastructure has been set up - the correct URLs have to be entered and login details need to be correct. As an example, the `run.py` file has been provided. This has been taken from [this repository](https://gitlab.com/UM-CDS/pht/vantage6-docker-demo/-/blob/master/researcher/python/run.py), which also contains an example infrastructure that can be used to simulate a real-world scenario (it also works with the example `method.py` file provided). The details in the `run.py` file are in place to use this sample infrastructure and have to be changed for a production environment. The main changes that will have to be made are the `image` name and any `(kw)args`. Then simply run the file using:

```bash
python run.py
```

## Read more
See the [documentation](https://docs.vantage6.ai/) for detailed instructions on how to install and use the server and nodes.

------------------------------------
> [vantage6](https://vantage6.ai)