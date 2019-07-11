# pipe-without-vital
Test repo to demonstrate the feasibility of transmitting a user defined python type between two python process in KWIVER

#### Requirements
1. Fletch
2. Kwiver

#### Building instructions
From project source directory
```bash
mkdir -p build
cd build
cmake ../ -Dkwiver_DIR=<path to kwiver build directory> -Dfletch_DIR=<path to fletch build directory>
```

#### Instructions for running the pipeline
From your build directory
```bash
pipeline_runner -p example/sender-receiver.pipe
```
