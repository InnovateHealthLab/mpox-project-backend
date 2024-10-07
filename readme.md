$\textit{Mpox Project Backend}$

$\texttt{Overview}$

$\texttt{This project is a backend service for managing case records. 
It is built with Django and Django REST Framework (DRF). 
The system allows you to create and retrieve case details, including age, gender, outcome, test status, location, and other relevant information.}$
$\texttt{Features
}$
$\texttt{
  + Create new case records
  + Retrieve all case records
  + Supports custom fields for location, outcome, and additional information
  + Age field restricted to two digits (0-99)
}$

### Models
#### NewCase

##### The NewCase model stores information about individual cases:
|Field	|Type	|Description |
|-------|-----|------------|
|case_code|	CharField	|Case identification code (max 9 characters)|
|age	|PositiveIntegerField	|Age of the case subject (0-99)|
|gender	|CharField	|Gender of the case subject (male, female)|
|date	|DateField	|Auto-generated date of case creation|
|outcome	|CharField	|Outcome of the case (suspended, confirmed)|
|test_status|	CharField|	Test result (pending, confirmed positive, confirmed negative)|
|location	|CharField	|City and Country information for the case|
|additional_information | TextField	|Optional details such as occupation and travel history|

> Endpoints
> URL	Method	Description
> /create-case/	POST	Create a new case record
> /get-all-case/	GET	Retrieve all case records
>
> ## Setup Instructions
>
>    Clone the repository:
>
>   bash
>
>> git clone https://github.com/InnovateHealthLab/mpox-project-backend.git
>> cd mpox-project-backend
>>
>> Install dependencies using Poetry:
>
> bash
>
>> poetry install
>>
>> Run migrations:
>
> bash
>
>> python manage.py migrate
>>
>> Run the server:
>
> bash
>>
>>   python manage.py runserver
>
>### Serializers
>>  FillNewCaseSerializer: Used to serialize and validate the data when creating a new case.
>>  GetAllCaseSerializer: Used to serialize the data when retrieving all cases.

Usage

    Create a new case (POST /create-case/):

    json

``` {
  "case_code": "ABC123",
  "age": 25,
  "gender": "male",
  "outcome": "suspended",
  "test_status": "pending",
  "location": "New York, USA",
  "additional_information": "Occupation: Engineer"
}
```

Retrieve all cases (GET /get-all-case/): Response format:

json

```    [
      {
        "case_code": "ABC123",
        "age": 25,
        "gender": "male",
        "date": "2024-10-06",
        "outcome": "suspended",
        "test_status": "pending",
        "location": "New York, USA",
        "additional_information": "Occupation: Engineer"
      }
    ]
```
License

This project is licensed under the MIT License.