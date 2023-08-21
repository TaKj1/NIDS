# Python NIDS Tool

A simple Network Intrusion Detection System (IDS) built with Python and Scapy.

## Features

- Monitors FTP packets on port 21.
- Heuristic analysis to detect suspicious patterns.
- Detects common nmap scans like SYN, NULL, and Xmas Tree scans.
- Extensible to support other protocols and detection rules.

## Linux Installation

1. Ensure you have Python 3.x installed.
2. Clone the repository :
3. Navigate to the project directory cd/path/to/NIDS:

4.Install the required packages: pip install -r requirements.txt:


## Docker Installation
1.Ensure you have Docker installed. If not, follow the instructions https://docs.docker.com/get-docker/.
2. Navite to the root directory: cd /path/to/your/NIDS
3.Build the image: docker build -t ids_tool .
4.Run the container :
docker run -it --net=host --privileged ids_tool:latest
it:
- "-i" (interactive): Keeps the standard input (STDIN) open even if not attached. This means that you can interact with the container's terminal.
-"t" (pseudo-TTY): Allocates a pseudo-TTY or terminal inside the new container. This allows you to see a terminal-like interface when you're interacting with the running container.
"--net=host": Uses the host network mode
5. Inside the container , you can now start from terminal : python3 -m src.sniffing.sniffer

## Future Features

As this project evolves, we aim to include a range of new features to enhance its capabilities and provide more in-depth analysis. Here are some features planned for future releases:

1. **Expanded Protocol Support:** Besides FTP, we plan to incorporate handlers for other commonly targeted protocols such as SSH, Telnet, and HTTP.

2. **Machine Learning-based Analysis:** By employing machine learning algorithms, we hope to identify complex attack patterns and improve false-positive rates.

3. **User Interface:** A web-based dashboard or a GUI application to visualize the traffic and potential threats in real-time.

4. **Integration with Threat Intelligence Platforms:** This will allow our IDS tool to cross-reference detected traffic with known malicious IP addresses and domains.

5. **Alerting Mechanisms:** Instead of just logging, the system will be able to send alerts via email, SMS, or integrate with popular platforms like Slack or Discord.

6. **Traffic Encryption Analysis:** Detecting threats within encrypted traffic by integrating SSL/TLS decryption capabilities.

7. **Custom Rule Engine:** Allowing users to define their custom rules for detecting specific patterns or behaviors in the network traffic.

8. **Distributed Monitoring:** Enabling deployment on multiple nodes and aggregating the analysis centrally for monitoring large networks.

Remember that this project is open-source, and contributions are welcome! If you'd like to suggest a feature or contribute to an existing one, please create an issue or submit a pull request.

