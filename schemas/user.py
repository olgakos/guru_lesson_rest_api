from voluptuous import Schema, Required, PREVENT_EXTRA

# required=True,  # фиксируем, что все перечисленыне поля ОБЯЗАТЕЛЬНЫ
 # extra=PREVENT_EXTRA,  # уточнить?

#----------------3-----------------------------------------------
get_single_user_schema = Schema(
    {
        "data": {
                "id": int,
                "email": str,
                "first_name": str,
                "last_name": str,
                "avatar": str
            },
            "support": {
                "url": str,
                "text": str
            }
    },
    required=True,
    extra=PREVENT_EXTRA
)

#---------3------------------
# этот объхект, вынесенный во вне (важно, ПЕРЕД ВЫЗОВОМ)
user = Schema(
    {
        "id": int,
        "email": str,
        "first_name": str,
        "last_name": str,
        "avatar": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

# этот объхект, вынесенный во вне (важно, ПЕРЕД ВЫЗОВОМ)
support = Schema(
    {
        "url": str,
        "text": str,
    },
    extra=PREVENT_EXTRA,
    required=True
)


users_list_schema = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": [user], #! см вынос для переиспользования, НО оставили скобки списка, т.к. их много (https://reqres.in/ -- LIST USERS)
        "support": support #! см вынос для переиспользования
    },
    extra=PREVENT_EXTRA,
    required=True
)


#------2---------------------

create_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

#---------2------------------
update_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "updatedAt": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

#-----------2----------------

successful_register_user_schema = Schema(
    {
        "id": int,
        "token": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

