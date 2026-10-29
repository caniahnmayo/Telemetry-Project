Project: Fleet Data REST JSON Quickstart

Name:
rest-json-quickstart - Quarkus-based REST JSON application for processing fleet and equipment telemetry data

Synopsis:
mvn quarkus:dev

Description:
This project is a Java-based backend service built with Quarkus designed to parse, analyze, and output equipment and fleet telematics JSON payloads through REST endpoints. It includes data models for engine parameters, machine states, batteries, and diagnostic trouble codes, along with utility scripts for key and fuel value extraction.

Files Included:
pom.xml
README.md
mvnw / mvnw.cmd
src/main/java/org/acme/
src/main/resources/
src/test/java/tests/
find_keys.py
find_fuel_values.py
san_take_home_json_2.json
san_take_home_json_3.json
san_take_home_json_4.json
san_take_home_json_5.json

How to Compile:
1. ./mvnw compile
2. mvn clean install

How to Run:
./mvnw quarkus:dev

Known Bugs:
N/A

Endpoints & Features:
/fleet - retrieves parsed JLG fleet equipment information and status updates.
Use: curl http://localhost:8080/fleet

/fleet/fuel - exposes fuel level statistics and consumption data.
	Use: curl http://localhost:8080/fleet/fuel


Python Utilities:
find_keys.py - scans JSON files to extract and map unique keys/telemetry attributes.
Use: python3 find_fuel_values.py

find_fuel_values.py - extracts fuel-specific telemetry data from raw JSON logs.
	Use: python3 find_keys.py


Environment Configuration:
application.properties configures HTTP transport, Quarkus development services, and JSON serialization defaults.
