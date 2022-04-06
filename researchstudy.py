import setup
token = setup.nexus_token

from io import StringIO
import sys
import nexussdk as nexus
import json

# get script arguments
nexus_deployment = "https://reservoir.global/v1"
org = 'Test'
project = 'uhn_demo'

# create nexus connection
nexus.config.set_environment(nexus_deployment)
nexus.config.set_token(token)
nexus.permissions.fetch()

# read data from nifi
inputDataList = sys.stdin.readlines()
inputData = StringIO()
inputData = ''.join(list(inputDataList))
study_input_payload = json.loads(inputData)

print("The input data was:")
print(json.dumps(study_input_payload, indent=4))

resource_for_nexus = {
		"@context": [
			"https://bluebrain.github.io/nexus/contexts/metadata.json",
			{
				"fhir": "http://hl7.org/fhir/",
                "rdfs": "http://www.w3.org/2000/01/rdf-schema#"
			}
		],
		"@type": [
			"fhir:ResearchStudy"
		],
		"fhir:ResearchStudy.identifier": [
			{
				"@type": "fhir:Identifier",
				"fhir:Identifier.value": {
					"fhir:value": study_input_payload["project_id"]
				}
			}
		],
		"fhir:ResearchStudy.status": {
			"@type": "fhir:code",
			"fhir:value": study_input_payload["research_study_status"]
		},
		"fhir:ResearchStudy.title": {
			"@type": "fhir:string",
			"fhir:value": study_input_payload["project_title"]
		},
        "rdfs:label": f"Research Study - {study_input_payload['project_id']}"
	}

print("The data to be inserted is:")
print(json.dumps(resource_for_nexus, indent=4))
insert_payload = nexus.resources.create(org, project, resource_for_nexus)

print("The @id of the inserted resource:")
print(insert_payload['@id'])