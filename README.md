# ubademy.gateway
[![codecov](https://codecov.io/gh/Ubademy/ubademy.gateway/branch/master/graph/badge.svg?token=WBSG1ZXWFL)](https://codecov.io/gh/Ubademy/ubademy.gateway) [![Tests](https://github.com/Ubademy/ubademy.gateway/actions/workflows/test.yml/badge.svg)](https://github.com/Ubademy/ubademy.gateway/actions/workflows/test.yml) [![Linters](https://github.com/Ubademy/ubademy.gateway/actions/workflows/linters.yml/badge.svg)](https://github.com/Ubademy/ubademy.gateway/actions/workflows/linters.yml) [![Deploy](https://github.com/Ubademy/ubademy.gateway/actions/workflows/deploy.yml/badge.svg)](https://github.com/Ubademy/ubademy.gateway/actions/workflows/deploy.yml)

This is a gateway. It handles and routes requests to different microservices.

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

## Calling multiple services
* Endpoint /service1.service2. ... . servicen
* Body should be:

      "methods": ["method1","method2", ... , "methodn"],

      "paths": ["path1","path2", ... , "pathn"],

      "params": [{"param":"value"},{"param":"value"}, ... ,{"param":"value"}]

  

## Build docker image
``` bash
make build
```

## Run with docker
``` bash
docker run -p 8000:8000 --env MICROSERVICES=<microservices_dict> GOOD_HEADERS=<good_headers_list>
```
Where: 
* <microservices_dict> is a dictionary like: '{"service":"service_url"}'
* <good_headers_list> is a list like: '\["good_header"\]'

## Tests
``` bash
make test
```

## Reformat
``` bash
make fmt
```

## Lint
``` bash
make lint
```
