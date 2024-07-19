This is a cute small example showing how powerful Docker is.

1) Make sure you have Docker installed.

2) Navigate to the repo.

3) Build the docker image:

`docker build -t docker-minimal-example .`

4) Run the container:

`docker run --rm docker-minimal-example --length 5 --low 0 --high 100 --seed 42`

You should see:

```
Train: [60 14 51 71]
Test: [92]
```

