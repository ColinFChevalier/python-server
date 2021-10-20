EMPLOYEES = [
    {
        "id": 1,
        "name": "Diogenes",
        "locationId": 1,
        "position": "Manager"
    },
    {
        "id": 2,
        "name": "Kaftka",
        "locationId": 1,
        "position": "Groundskeeper"
    },
    {
        "id": 3,
        "name": "Socrates",
        "locationId": 2,
        "position": "Intern"
    }
]


def get_all_employees():
    return EMPLOYEES

def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee


def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee


def delete_employee(id):
    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)


def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break