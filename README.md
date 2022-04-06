# nexus_demo_obi
This repository contains code and slides shared with the OBI team during a Blue Brain Nexus demo.  

The demo was related to the CFI grant and showing how we load REDCap data into our data warehouse and then into Nexus.

This patient.py and researchstudy.py files create records in the reservoir.global instance of Nexus. They are strictly 'inserting' records so duplicates are possible.  See the Nexus SDK documentation on how to perform updates, deletes and other operations.

The repository contains a setup.py file.  Replace the empty string with your Nexus token.  

## Links:
- Documentation: https://bluebrainnexus.io/docs/index.html
- reservoir.global project: https://reservoir.global/admin/Test/uhn_demo
