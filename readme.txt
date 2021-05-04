project - api_project
app - api_app

A simple API with CRUD functions, built using Django web and Django rest framework.
Realworld use:  Api lets people add supplies like availability of oxygen cylinders, beds, food ,medicines nto the
                database so that people in need may get help as soon as possile.

The app that uses the api can add/update the data in JSON format.
The fields are:
                {
                    "Name": "your_name",
                    "Phone_number": your_number,
                    "State": "name_of_the_state_in_which_the_supplies_are_available",
                    "City": "name_of_the_city_in_which_the_supplies_are_available",
                    "Supply_address": "address_of_the_place",
                    "Description": "kind_of_supplies_availabe",
                    "Approx_quantity_available": quantity_of_supplies
                }

:Only the values of the template must be changed and not the keys, also the 'phone number' and 'quantty available'
must be integers

updating and deleting can be done by passing the id of the record to the url
    example:    http://127.0.0.1:8000/api/update-supplies/2,
                http://127.0.0.1:8000/api/delete-supplies/2

