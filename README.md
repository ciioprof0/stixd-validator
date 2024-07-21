# STIX Description Validator (stixd-validator)
The STIX Description Validator ensures that STIX 2.1 description instances adhere to the STIX Description controlled natural language (stixd-cnl). This validator is non-normative tool. In cases of conflict with the STIX 2.1 specification, the specification takes precedence.

**Note:** In the initial proof-of-concept phase, we will focus on the `indicator` object ([SDO 4.7](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_muftrcpnf89v)) for describing MITRE ATT&CK Technique [T1204.003](https://attack.mitre.org/techniques/T1204/003/) - User Execution: Malicious Image.

#### Table 1. List of Project Repositories

| No. | Repository | Description |
|-----|------------|-------------|
| 1-1. | [stixd](https://github.com/ciioprof0/stixd) | Main repository for the project. | 
| 1-2. | [stixd-cnl](https://github.com/ciioprof0/stixd-cnl) | Definitions for the Controlled Natural Language (CNL). To be developed.|
| 1-3. | [stixd-validator](https://github.com/ciioprof0/stixd-validator) | Application to verify if a string is a member of the CNL. To be developed.|


#### Table 2. List of Related Third-Party Repositories

| No. | Repository | Description |
|-----|------------|-------------|
| 2-1. | [attack-stix-data](https://github.com/mitre-attack/attack-stix-data) | MITRE ATT&CK dataset represented in STIX 2.1 JSON collections. | 
| 2-2. | [cti-pattern-validator](https://github.com/oasis-open/cti-pattern-validator) | A software tool for checking the syntax of the Cyber Threat Intelligence (CTI) STIX Pattern expressions |
| 2-3. | [cti-python-stix2](https://github.com/oasis-open/cti-python-stix2) | Python APIs for serializing and de-serializing STIX2 JSON content, along with higher-level APIs for common tasks, including data markings, versioning, and for resolving STIX IDs across multiple data sources. |
| 2-4. | [cti-stix2-json-schemas](https://github.com/oasis-open/cti-stix2-json-schemas) | JSON schemas and examples for STIX 2 |
| 2-5. | [cti-stix-validator](https://github.com/oasis-open/cti-stix-validator) | The STIX Validator checks that STIX JSON content conforms to the requirements specified in the STIX 2.1 specification. |

## ToDo List

- Week 1
  - ☑ Use Cases Document (10pts)

- Week 2
  - ☑ UML Class Diagrams (10pts)

- Week 3
  - ☑ Code uses a test and OOP (20pts)
  - ☐ BONUS - Code to obtain data via a web scraper (10pts)

- Week 4
  - ☐ Code uses a database (20pts)
    - ☐ A database implemented in SQL with at least one correctly formed SQL statement
    - ☐ A repository interface that isolates all SQL-specific dependencies
    - ☐ An effective test for the db code

- Week 5
  - ☐ Code has at least 1 function that implements a use case from #1 (20pts)
    - ☐ Code produces the intended output from the input specified in the Use Cases Document
    - ☐ A proper service layer that calls the separate domain model and database layers

- Week 6
  - ☐ Code has a Flask API server (20pts)
    - ☐ A working Flask API server that can be called with Postman or curl
    - ☐ API calling the separate Service layer to execute the Use Case
  - ☐ Deliverable: Documentation Page (20pts)
    - Document the functionality of the Flask API, including endpoints and expected input/output

- Week 7
  - ☐ Code is complete and has a simple HTTP form page (20pts)
    - ☐ Complete code that passes at least 1 end-to-end test
    - ☐ An HTTP form page that acts as the UI for the project

- End of Course
  - ☐ Deliverable: Demo Video (30pts)
    - ☐ Clearly explain the use cases
    - ☐ Show the code correctly executing the use case
    - ☐ Explain the design of the project using Object Oriented Programming
    - ☐ Explain how the code interacts with the database
    - ☐ Explain the tests


- ☐ Unchecked checkbox
- ☑ Checked checkbox 
