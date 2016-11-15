"""
IPO Cerner FHIR Demo

This simple program was written to demonstrate for the IPO a method of 
retrieving health data in FHIR format from Cerner Millenium, known as 
MHS Genesis in the DoD.
"""
# This demo uses the SMART on FHIR python FHIR Client package
from fhirclient import client

# The API base URL is set to the Cerner Open Sandbox Server
settings = {
    'app_id': 'ipoDemo_app',
    'api_base': 'https://fhir-open.sandboxcernerpowerchart.com/dstu2/d075cf8b-3261-481d-97e5-ba6c48d3b41f'
}
smart = client.FHIRClient(settings=settings)

# Since the server is open we won't have to worry about authentication

print "Retrieving server's conformance statement..."
smart.prepare()
#print smart.server.conformance.as_json()
print 'Retrieved conformance statement from ' + smart.server.conformance.url
print smart.server.conformance.name
print 'Server publisher: ' + smart.server.conformance.publisher
print '    FHIR Version: ' + smart.server.conformance.fhirVersion
print '------------------------------------------------------'


# Retrieve Patient data for ID 2744010 (Chosen because it has medication orders)
import fhirclient.models.patient as pat
patient = pat.Patient.read('2744010', smart.server)

# Print some info to show we have retrieved data about the patient
print 'Retrieved patient record. . .'
print '  Patient ID: ' + patient.id
print '  Birth date: ' + patient.birthDate.isostring
print 'Patient name: ' + smart.human_name(patient.name[0])
print 'Medications with status=active: '
print '------------------------------------------------------'

# Search for medication orders for the patient we just retrieved
import fhirclient.models.medicationorder as mo
search = mo.MedicationOrder.where(struct={'patient': patient.id, 'status': 'active'})
medOrders = search.perform_resources(smart.server)

# Print out info about each order in the list.
for medOrder in medOrders:
    print 'Date written: ' + medOrder.dateWritten.isostring
    print '  Medication: ' + medOrder.medicationCodeableConcept.text
    print '------------------------------------------------------'
