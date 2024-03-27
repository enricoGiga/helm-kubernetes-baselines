This `README.md` file provides a step-by-step guide on how to deploy your application using Docker, Helm, and Kubernetes.
## Steps

1. **Build the Docker image**

   Run the following command to build a Docker image using the `Dockerfile` in the current directory. The `-t` flag is used to tag the image with a name and optionally a tag in the 'name:tag' format.

   ```shell
   docker build -t challenge-uncommon-imp:1.0.0 . 
   ```

2. **Package the Helm chart**
   Navigate to the `helm` directory in the project.
   Run the following command to package the Helm chart in the current directory. The `helm package` command creates a versioned chart archive file from the chart directory.

   ```shell
   helm package .
   ```
   This will create a file named `challenge-uncommon-imp-1.0.0.tgz`.

3. **Install the Helm chart**

   Run the following command to install the Helm chart in the current directory. The `helm install` command installs the chart in the Kubernetes cluster.

   ```shell
   helm install my-release ./challenge-uncommon-imp-1.0.0.tgz
   ```
   This will create the necessary Kubernetes resources (like Deployments, Services, etc.) as defined in your Helm chart.
4. **Port-forward**
   the service  Run the following command to forward connections from a local port to a port on the service. This allows you to access your application locally.  
   
   ```shell 
   kubectl port-forward svc/challenge-uncommon-imp 8080:8080
    ```
   Now, you can access your application at localhost:8080 or 0.0.0.0:8080 in your web browser.

## Metrics on /health endpoint
The output from the `/health` endpoint is in a Prometheus exposition format, which is a way to expose metrics data in a format that Prometheus can scrape and monitor. 

The `/health` endpoint is set up to generate the latest metrics in this format. The metrics include information about Python garbage collection, Python platform information, process information, and model prediction information.

Here's a brief explanation of some of the metrics:

- `python_gc_objects_collected_total`: The total number of objects that have been collected by Python's garbage collector, broken down by generation.
- `python_gc_objects_uncollectable_total`: The total number of uncollectable objects found during garbage collection, broken down by generation.
- `python_gc_collections_total`: The total number of times each generation has been collected by the garbage collector.
- `python_info`: Information about the Python platform, including the implementation and version.
- `process_virtual_memory_bytes`: The virtual memory size of the process in bytes.
- `process_resident_memory_bytes`: The resident memory size of the process in bytes.
- `process_start_time_seconds`: The start time of the process since the Unix epoch in seconds.
- `process_cpu_seconds_total`: The total user and system CPU time spent by the process in seconds.
- `process_open_fds`: The number of open file descriptors.
- `process_max_fds`: The maximum number of open file descriptors.
- `model_accuracy`: The accuracy of the model prediction.
- `model_prediction_time`: The time spent processing model predictions.

This is a standard way to expose metrics for monitoring in a microservices environment. 