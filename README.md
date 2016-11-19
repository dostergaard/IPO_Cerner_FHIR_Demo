#IPO Cerner FHIR Demo 
This simple demo illustrates accessing and retrieving data from a Cerner EHR using **FHIR**. The demo is written to use the Cerner Open Sandbox server and does three simple things.

1. It retrieves the Server Conformance Statement and prints out a few bits of information to show it is indeed connected to the server.
2. It retrieves and prints information from the patient record for a patient with a particular ID that is known to have Medication Orders associated with it.
3. It performs a search for Medication Orders with status = 'active' for the identified patient and prints them out

Thats it! I told you it was simple.

###Dependencies
It is written in Python and uses the python [fhirclient](https://pypi.python.org/pypi/fhirclient/1.0.6) package which is maintained by the SMART on FHIR Team. You can also grab it from [their GitHub repository](https://github.com/smart-on-fhir/client-py).

###Python Version
As written this simple program runs under python 2.7.x mainly because of the print statements but also because at the time fhirclient had a [bug](https://github.com/smart-on-fhir/client-py/issues/20) that shows up under python version 3.4.x that results in an ImportError. The fhirclient seems to work fine for python version 3.5.x and if the print statements are addressed I am pretty sure this demo would work fine as well.

###Running the Demo
For anyone familar with Python development and python virtual environments it is a simple matter to download and run this demo.

1. Clone this project
2. Switch into the project directory on your system and create a python2 virtual environment (e.g., 'virtualenv -p python2 env2-ipodemo')
3. Activate the virtual environment
4. Run 'pip install -r requirements.txt'
5. Run the demo 'python ipodemo.py'

###Where this goes from here
There are many FHIR projects in many languages right here on GitHub and elsewhere. Most do much more than this simple demo. 

The purpose of this demo was simply to prove that standard FHIR resources and APIs could indeed be used to access data from a specific vendor's EHR. The fact is that if a vendor or product implements FHIR according to the specifications and guidelines it shouldn't matter which product is behind the API. That is, after all, the goal of FHIR. Isn't it?

I think this demo proves what it set out to and if so I don't see much reason to develop this much further.

###Credits
Thanks to the SMART on FHIR Team for creating a relatively easy to use FHIR client package.
