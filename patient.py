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
patient_input_payload = json.loads(inputData)

print("The input data was:")
print(json.dumps(patient_input_payload, indent=4))

resource_for_nexus = {
    "@context": {
        "fhir": "http://hl7.org/fhir/",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#"
    },
    
    "@type": "fhir:Patient",
    
    "rdfs:label": f"PatientID - {patient_input_payload['patientid']}",
    
    "fhir:Patient.address": {
        "@type": "fhir:Address",
        "fhir:Address.postalCode": {
            "@type": "fhir:string",
            "fhir:value": patient_input_payload['postalcode']
        }
    },
    
    "fhir:Patient.gender": {
        "@type": "fhir:code",
        "fhir:value": patient_input_payload['gender']
    },
    
    "fhir:Patient.identifier": {
        "@type": "fhir:Identifier",
        "fhir:Identifier.type": {
            "@type": "fhir:CodeableConcept",
            "fhir:CodeableConcept.text": {
                "fhir:value": "PatientID"
            }
        },
        "fhir:Identifier.value": {
            "fhir:value": patient_input_payload['patientid']
        }
    }
}

print("The data to be inserted is:")
print(json.dumps(resource_for_nexus, indent=4))
insert_payload = nexus.resources.create(org, project, resource_for_nexus)

print("The @id of the inserted resource:")
print(insert_payload['@id'])