#IPO Cerner FHIR Demo 
This simple demo illustrates accessing and retrieving data from Cerner Millenium using **FHIR**. The demo is written to use the Cerner Open Sandbox server and does three simple things.

1. It retrieves the Server Conformance Statement and prints out a few bits of information to show it is indeed connected to the server.
2. It retrieves and prints information from the patient record for a patient with a particular ID that is known to have Medication Orders associated with it.
3. It performs a search for Medication Orders with status = 'active' for the identified patient and prints them out

Thats it!

###Dependencies
It is written in Python and uses the python [fhirclient](https://pypi.python.org/pypi/fhirclient/1.0.6) package which is maintained by the SMART on FHIR Team.

###Python Version
As written this simple program runs under puthon 2.7

###Running the Demo
For anyone familar with Python development and python virtual environments it is a simple matter to download and run this demo.

1. Clone this project
2. Switch into the project directory on your system and create a python2 virtual environment (e.g., 'virtualenv -p python2 ipodemo2')
3. Activate the virtual environment
4. Run 'pip install -r requirements.txt'
5. Run the demo 'python ipodemo.py'

###Credit
Thanks to the SMART on FHIR Team for creating a relatively easy to use FHIR client package.
