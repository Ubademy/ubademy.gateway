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
│   ├── router
│   │   ├── router.py
│   │   └── router_exception.py
│   └── service_caller
│       └── service_caller.py
└── tests
```

## Build docker image
``` bash
make build
```

## Run with docker
``` bash
docker run -p 8000:8000 --env MICROSERVICES=<microservices_dict>
```
Where <microservices_dict> is a dictionary like: '{"service":"service_url"}'


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
