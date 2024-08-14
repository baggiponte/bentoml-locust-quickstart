# 🚀 BentoML and Locust Demo

This demo showcases how to deploy a machine learning model using BentoML and perform load testing with Locust.

## 🏁 Install dependencies

The guide uses [uv](https://github.com/astral-sh/uv), as it is a fast, reliable, and feature-rich Python package installer and resolver. But you can use any other package manager you prefer.

1. Install [uv](https://github.com/astral-sh/uv#getting-started):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Create a new virtual environment and install dependencies:

 ```bash
 # if you want to use package management features
 uv sync

 # the old requirements way
 uv venv --python=3.11
 uv pip install -r pyproject.toml
 ```

## 🤔 What are BentoML and Locust?

### BentoML 📦

BentoML is an open-source platform for machine learning model serving. It simplifies the process of packaging, deploying, and managing machine learning models in production environments. Key features include:

- Model packaging and versioning
- API server generation
- Microservice architecture support
- Scalable model serving (on BentoCloud)

### Locust 🦗

Locust is an open-source load testing tool. It allows you to write Python code to define the behavior of your users and then swarm your system with millions of simultaneous users. Features include:

- Python-based test scripts
- Web-based UI for real-time test monitoring
- Distributed testing across multiple machines
- Customizable metrics and reporting

## 🚀 Starting the Services

### 1. Start the BentoML Service

1. Ensure your model is saved as a BentoML service (refer to BentoML documentation for details).

2. Run the BentoML service:

```bash
uv run bentoml serve service:Summarization
```

3. Your BentoML service should now be running on `http://localhost:3000`.

### 2. Run Locust for Load Testing

1. Ensure you have the `locustfile.py` in your project directory.

2. Start Locust:

```bash
uv run locust -f locustfile.py
```

3. Open a web browser and go to `http://localhost:8089`.

4. In the Locust web interface:
   - Set the number of users to simulate
   - Set the spawn rate (users started per second)
   - Enter the host URL of your BentoML server (e.g., `http://localhost:3000`)
   - Click "Start swarming"

5. Monitor the performance metrics in real-time through the Locust web interface.

## 📊 Analyzing Results

After running your load tests, you can analyze the results in the Locust web interface. Look for metrics such as:

- Response times (average, median, 95th percentile)
- Requests per second
- Number of failures

Use these insights to optimize your BentoML service for better performance under load.

## 🤝 Contributing

Contributions to improve this demo are welcome! Please feel free to submit pull requests or open issues for any enhancements, bug fixes, or documentation improvements.

## 📝 License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.
