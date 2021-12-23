# ubademy.gateway
[![codecov](https://codecov.io/gh/Ubademy/ubademy.gateway/branch/master/graph/badge.svg?token=WBSG1ZXWFL)](https://codecov.io/gh/Ubademy/ubademy.gateway) [![Tests](https://github.com/Ubademy/ubademy.gateway/actions/workflows/test.yml/badge.svg)](https://github.com/Ubademy/ubademy.gateway/actions/workflows/test.yml) [![Linters](https://github.com/Ubademy/ubademy.gateway/actions/workflows/linters.yml/badge.svg)](https://github.com/Ubademy/ubademy.gateway/actions/workflows/linters.yml) [![Deploy](https://github.com/Ubademy/ubademy.gateway/actions/workflows/deploy.yml/badge.svg)](https://github.com/Ubademy/ubademy.gateway/actions/workflows/deploy.yml)

Gateway for for [Ubademy](https://ubademy.github.io/)

It handles and routes requests to different microservices.

For further information visit [Ubademy Gateway](https://ubademy.github.io/services/gateway)

Deployed at: [ubademy--gateway](https://ubademy--gateway.herokuapp.com/docs#) :rocket:

## Technologies

* [FastAPI](https://fastapi.tiangolo.com/)
* [Poetry](https://python-poetry.org/)
* [Docker](https://www.docker.com/)
* [Heroku](https://www.heroku.com/)

## Architecture

```tree
├── main.py
├── app
│   ├── caller
│   │   ├── caller.py
│   │   ├── multi_service_caller.py
│   │   └── service_caller.py
│   └── router
│       ├── router.py
│       └── router_exception.py
└── tests
```

## Installation

### Dependencies:
* [python3.9](https://www.python.org/downloads/release/python-390/) and utils
* [Docker](https://www.docker.com/)
* [Docker-Compose](https://docs.docker.com/compose/)
* [Poetry](https://python-poetry.org/)

Once you have installed these tools, make will take care of the rest :relieved:

``` bash
make install
```
## Usage

### Build
``` bash
make build
```

### Run the API locally
``` bash
docker run -p 8000:8000 --env MICROSERVICES=<microservices_dict> GOOD_HEADERS=<good_headers_list>
```
Where: 
* <microservices_dict> is a dictionary like: '{"service":"service_url"}'
* <good_headers_list> is a list like: '\["good_header"\]'

### Run format, tests and linters
``` bash
make checks
```

### Access API Swagger
Once the API is running you can check all available endpoints at [http://127.0.0.1:8000/docs#/](http://127.0.0.1:8000/docs#/)
